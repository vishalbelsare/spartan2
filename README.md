
# spartan2

![](https://img.shields.io/badge/language-python-yellow.svg)
[![](https://img.shields.io/badge/pypi-0.1.3-brightgreen.svg)](https://pypi.org/project/spartan2/)
![](https://img.shields.io/github/forks/BGT-M/spartan2.svg?color=blue)
![](https://img.shields.io/github/stars/BGT-M/spartan2.svg?color=blue)
[![](https://readthedocs.org/projects/spartan2/badge/?version=latest)](https://spartan2.readthedocs.io/en/latest/)
[![](https://github.com/BGT-M/spartan2/actions/workflows/python-publish.yml/badge.svg)](https://github.com/BGT-M/spartan2/actions)
[![](https://img.shields.io/github/license/BGT-M/spartan2.svg)](https://github.com/BGT-M/spartan2/blob/master/LICENSE)

**spartan2** is a toolkit of data mining algorithms for **big graphs** and **time series**, covering three core tasks:

- **Anomaly Detection** — spot fraud, surges, and outliers
- **Forecasting** — predict future patterns in time series
- **Summarization** — compress and describe large graph/time-series structures

> Docs: [readthedocs](https://spartan2.readthedocs.io/en/latest/) | Tutorials: [spartan2-tutorials](https://github.com/BGT-M/spartan2-tutorials)

---

## Why spartan2?

Graphs and time series appear across many domains — social networks, finance, sensor networks, and healthcare. Treating them as **sparse tensors** (matrices are 2-mode tensors) enables algorithms that are:

- **Efficient** — near-linear complexity by exploiting sparsity
- **Interpretable** — results backed by mathematical guarantees
- **Accurate** — validated on real-world benchmarks

The name **spartan** = **spar**se **t**ensor **an**alytics.

---

## Installation

Requires Python ≥ 3.7. We recommend using a Conda environment.

```bash
conda create -n spartan python=3.7
conda activate spartan
```

### For users

```bash
pip install spartan2
```

### For contributors / running from source

```bash
# 1. Clone the repo
git clone git@github.com:BGT-M/spartan2.git

# 2. Install dependencies
conda install --force-reinstall -y --name spartan -c conda-forge --file requirements

# 3. Install in editable mode
pip install -e spartan2
```

<details>
<summary>Setting PYTHONPATH (if needed)</summary>

Add to `~/.bashrc`:

```bash
export PYTHONPATH=/<path-to>/spartan2:$PYTHONPATH
```

Or inside Python:

```python
import sys
sys.path.append("/<path-to>/spartan2")
```

</details>

---

## Quick Start

```python
import spartan as st

# Load a graph as a sparse tensor
graph = st.loadGraph("your_edge_list.csv", col_types=[int, int, float])

# Run anomaly detection (e.g. HoloScope)
model = st.HoloScope(graph)
model.run()
model.result()
```

See the [tutorials repo](https://github.com/BGT-M/spartan2-tutorials) for runnable Jupyter notebooks for each algorithm.

---

## Algorithms

### Graph Mining

| Algorithm | Task | Paper | Year | Tutorial |
| :-------- | :--- | :---- | :--- | :------- |
| [HoloScope](https://github.com/BGT-M/spartan2/tree/master/spartan/model/holoscope) | Anomaly Detection | [[1]](#ref1) HoloScope: Topology-and-Spike Aware Fraud Detection [[pdf]](https://shenghua-liu.github.io/papers/cikm2017-holoscope.pdf) | 2017 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/Holoscope.ipynb) |
| [Eigenspokes](https://github.com/BGT-M/spartan2/tree/master/spartan/model/eigenspokes) | Anomaly Detection | [[3]](#ref3) Eigenspokes: Surprising Patterns in Large Graphs [[pdf]](https://www.cs.cmu.edu/~christos/PUBLICATIONS/pakdd10-eigenspokes.pdf) | 2010 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/EigenSpokes.ipynb) |
| [EagleMine](https://github.com/BGT-M/spartan2/tree/master/spartan/model/eaglemine) | Anomaly Detection | [[4]](#ref4) EagleMine: Vision-guided Micro-cluster Anomaly Detection [[pdf]](https://shenghua-liu.github.io/papers/FGCS2021-eaglemine.pdf) | 2021 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/EagleMine.ipynb) |
| [Fraudar](https://github.com/BGT-M/spartan2/tree/master/spartan/model/fraudar) | Anomaly Detection | [[5]](#ref5) Fraudar: Bounding Graph Fraud in the Face of Camouflage [[pdf]](https://www.kdd.org/kdd2016/papers/files/rfp0110-hooiA.pdf) | 2016 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/Fraudar.ipynb) |
| [EigenPulse](https://github.com/BGT-M/spartan2/tree/master/spartan/model/eigenpulse) | Anomaly Detection | [[7]](#ref7) EigenPulse: Detecting Surges in Large Streaming Graphs [[pdf]](https://link.springer.com/chapter/10.1007/978-3-030-16145-3_39) | 2019 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/EigenPulse.ipynb) |
| [FlowScope](https://github.com/BGT-M/spartan2/tree/master/spartan/model/flowscope) | Anomaly Detection | [[8]](#ref8) FlowScope: Spotting Money Laundering Based on Graphs [[pdf]](https://ojs.aaai.org/index.php/AAAI/article/view/5906) | 2020 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/FlowScope.ipynb) |
| [CubeFlow](https://github.com/BGT-M/spartan2/tree/master/spartan/model/CubeFlow) | Anomaly Detection | [[11]](#ref11) CubeFlow: Money Laundering Detection with Coupled Tensors [[pdf]](https://arxiv.org/pdf/2103.12411.pdf) | 2021 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/CubeFlow.ipynb) |
| [MonLAD](https://github.com/BGT-M/spartan2/tree/master/spartan/model/MonLAD) | Anomaly Detection | [[13]](#ref13) MonLAD: Money Laundering Agents Detection in Transaction Streams [[pdf]](https://shenghua-liu.github.io/papers/wsdm2022-monlad.pdf) | 2022 | — |
| [SpecGreedy](https://github.com/BGT-M/spartan2/tree/master/spartan/model/SpecGreedy) | Anomaly Detection | [[12]](#ref12) SpecGreedy: Unified Dense Subgraph Detection [[pdf]](https://shenghua-liu.github.io/papers/pkdd2020_specgreedy.pdf) | 2020 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/SpecGreedy.ipynb) |
| [DPGS](https://github.com/BGT-M/spartan2/tree/master/spartan/model/DPGS) | Summarization | [[6]](#ref6) DPGS: Degree-Preserving Graph Summarization [[pdf]](https://shenghua-liu.github.io/papers/sdm2021-dpgs.pdf) | 2021 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/DPGS.ipynb) |
| [kGrass](https://github.com/BGT-M/spartan2/tree/master/spartan/model/kGS) | Summarization | [[9]](#ref9) GraSS: Graph Structure Summarization [[pdf]](http://cs-people.bu.edu/evimaria/papers/Social-net.pdf) | 2010 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/kGrass.ipynb) |
| [IAT](https://github.com/BGT-M/spartan2/tree/master/spartan/model/iat) | Summarization | [[10]](#ref10) RSC: Mining and Modeling Temporal Activity in Social Media [[pdf]](https://www.researchgate.net/publication/277311838) | 2015 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/iat_demo.ipynb) |

### Time Series

| Algorithm | Task | Paper | Year | Tutorial |
| :-------- | :--- | :---- | :--- | :------- |
| [BeatLex](https://github.com/BGT-M/spartan2/tree/master/spartan/model/beatlex) | Summarization & Forecast | [[14]](#ref14) BEATLEX: Summarizing and Forecasting Time Series with Patterns [[pdf]](https://shenghua-liu.github.io/papers/pkdd2017-beatlex.pdf) | 2017 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/Beatlex.ipynb) |
| [BeatGAN](https://github.com/BGT-M/spartan2/tree/master/spartan/model/beatgan) | Anomaly Detection | [[15]](#ref15) BeatGAN: Anomalous Rhythm Detection using Adversarially Generated Time Series [[pdf]](https://www.ijcai.org/Proceedings/2019/0616.pdf) | 2019 | [notebook](https://github.com/BGT-M/spartan2-tutorials/blob/master/BeatGAN.ipynb) — requires `torch` and `tqdm`; uses scipy Pan-Tompkins (no biosppy) |

---

## References

1. <span id="ref1"></span> Shenghua Liu, Bryan Hooi, and Christos Faloutsos. "HoloScope: Topology-and-Spike Aware Fraud Detection." *CIKM 2017*.
2. <span id="ref2"></span> Shenghua Liu, Bryan Hooi, Christos Faloutsos. "A Contrast Metric for Fraud Detection in Rich Graphs." *IEEE TKDE*, Vol 31, Issue 12, 2019.
3. <span id="ref3"></span> B. Aditya Prakash et al. "Eigenspokes: Surprising Patterns and Scalable Community Chipping in Large Graphs." *PAKDD 2010*.
4. <span id="ref4"></span> Wenjie Feng, Shenghua Liu, et al. "EagleMine: Vision-guided Micro-clusters Recognition and Collective Anomaly Detection." *Future Generation Computer Systems*, 2021. Also: "Beyond Outliers and On to Micro-Clusters." *PAKDD 2019*.
5. <span id="ref5"></span> Bryan Hooi, Hyun Ah Song, et al. "Fraudar: Bounding Graph Fraud in the Face of Camouflage." *KDD 2016*.
6. <span id="ref6"></span> Houquan Zhou, Shenghua Liu, et al. "DPGS: Degree-Preserving Graph Summarization." *SDM 2021*.
7. <span id="ref7"></span> Jiabao Zhang, Shenghua Liu, et al. "EigenPulse: Detecting Surges in Large Streaming Graphs with Row Augmentation." *PAKDD 2019*.
8. <span id="ref8"></span> Xiangfeng Li, Shenghua Liu, et al. "FlowScope: Spotting Money Laundering Based on Graphs." *AAAI 2020*.
9. <span id="ref9"></span> Kristen LeFevre and Evimaria Terzi. "GraSS: Graph Structure Summarization." *SDM 2010*.
10. <span id="ref10"></span> Alceu Ferraz Costa et al. "RSC: Mining and Modeling Temporal Activity in Social Media." *KDD 2015*.
11. <span id="ref11"></span> Xiaobing Sun, Jiabao Zhang, et al. "CubeFlow: Money Laundering Detection with Coupled Tensors." *PAKDD 2021*.
12. <span id="ref12"></span> Wenjie Feng, Shenghua Liu, et al. "SpecGreedy: Unified Dense Subgraph Detection." *ECML-PKDD 2020*.
13. <span id="ref13"></span> Xiaobing Sun, Wenjie Feng, Shenghua Liu, et al. "MonLAD: Money Laundering Agents Detection in Transaction Streams." *WSDM 2022*.
14. <span id="ref14"></span> Bryan Hooi, Shenghua Liu, et al. "BEATLEX: Summarizing and Forecasting Time Series with Patterns." *ECML-PKDD 2017*.
15. <span id="ref15"></span> Bin Zhou, Shenghua Liu, et al. "BeatGAN: Anomalous Rhythm Detection using Adversarially Generated Time Series." *IJCAI 2019*.
16. <span id="ref16"></span> Shenghua Liu, Bin Zhou, et al. "Time Series Anomaly Detection with Adversarial Reconstruction Networks." *IEEE TKDE 2022*.
