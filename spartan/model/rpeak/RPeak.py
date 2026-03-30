import numpy as np
from scipy.signal import butter, filtfilt, find_peaks

from .._model import DMmodel
from . import param_default, DTensor

param_default_dict = {
    'sampling_rate': 360,
    'left_size': 120,
    'right_size': 136,
    'out_path': None
}


def _pan_tompkins_rpeaks(signal, sampling_rate):
    """Detect R-peaks using a simplified Pan-Tompkins algorithm via scipy."""
    # Bandpass filter 5-15 Hz to isolate QRS complex
    nyq = 0.5 * sampling_rate
    b, a = butter(4, [5 / nyq, 15 / nyq], btype='band')
    filtered = filtfilt(b, a, signal)

    # Differentiate, square, and apply moving average
    diff = np.diff(filtered)
    squared = diff ** 2
    win = int(0.15 * sampling_rate)
    kernel = np.ones(win) / win
    integrated = np.convolve(squared, kernel, mode='same')

    # Find peaks with minimum distance of ~200 ms
    min_dist = int(0.2 * sampling_rate)
    r_peaks, _ = find_peaks(integrated, distance=min_dist, height=np.mean(integrated))
    return r_peaks


class RPeak(DMmodel):
    def __init__(self, time_series, *args, **para_dict):
        self.series_data = time_series.val_tensor
        self.sampling_rate = param_default(para_dict, 'sampling_rate', param_default_dict)
        self.left_size = param_default(para_dict, 'left_size', param_default_dict)
        self.right_size = param_default(para_dict, 'right_size', param_default_dict)
        self.out_path = param_default(para_dict, 'out_path', param_default_dict)
        self.length = time_series.length
        self.segments = None

    def _find_rpeaks(self):
        # Extract raw 1D numpy signal from DTensor (shape: channels x samples)
        raw = self.series_data._data
        signal = np.asarray(raw[0], dtype=float)
        r_peaks = _pan_tompkins_rpeaks(signal, self.sampling_rate)

        segments = []
        for r_peak in r_peaks:
            if r_peak - self.left_size >= 0 and r_peak + self.right_size < self.length:
                ts = self.series_data._data[:, r_peak - self.left_size:r_peak + self.right_size]
                segments.append(ts)
        self.segments = DTensor.from_numpy(np.array(segments))
        if self.out_path is not None:
            np.save(self.out_path, np.array(segments))
        return self.segments

    def run(self):
        return self._find_rpeaks()
