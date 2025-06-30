![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
<a href="https://arxiv.org/pdf/2406.15627" target="_blank"><img src=https://img.shields.io/badge/arXiv-b5212f.svg></a>
## 🔗 Project Origin

This repository is based on [IINemo/lm-polygraph](https://github.com/IINemo/lm-polygraph).  
Special thanks to the original authors for their excellent work.

## ✨ What's Modified

- Adapted part of the uncertainty estimation pipeline for new datasets on analogical reasoning


# LM-Polygraph: Uncertainty estimation for LLMs

[Installation](#installation) | [Basic usage](#basic_usage) | [Overview](#overview_of_methods) | [Benchmark](#benchmark) | [Demo application](#demo_web_application) | [Documentation](https://lm-polygraph.readthedocs.io/)

LM-Polygraph provides a battery of state-of-the-art of uncertainty estimation (UE) methods for LMs in text generation tasks. High uncertainty can indicate the presence of hallucinations and knowing a score that estimates uncertainty can help to make applications of LLMs safer.

The framework also introduces an extendable benchmark for consistent evaluation of UE techniques by researchers and a demo web application that enriches the standard chat dialog with confidence scores, empowering end-users to discern unreliable responses.

## Installation

### From GitHub
To install latest from main brach, clone the repo and conduct installation using pip, it is recommended to use virtual environment. Code example is presented below:

```shell
git clone https://github.com/IINemo/lm-polygraph.git
python3 -m venv env # Substitute this with your virtual environment creation command
source env/bin/activate
cd lm-polygraph
pip install .
```

Installation from GitHub is recommended if you want to explore notebooks with examples or use default benchmarking configurations, as they are included in the repository but not in the PyPI package. However code from the main branch may be unstable, so it is recommended to checkout to the latest stable release before installation:

```shell
git clone https://github.com/IINemo/lm-polygraph.git
git checkout tags/v0.3.0
python3 -m venv env # Substitute this with your virtual environment creation command
source env/bin/activate
cd lm-polygraph
pip install .
```

### From PyPI
To install the latest stable version from PyPI, run:

```shell
python3 -m venv env # Substitute this with your virtual environment creation command
source env/bin/activate
pip install lm-polygraph
```

To install a specific version, run:

```shell
python3 -m venv env # Substitute this with your virtual environment creation command
source env/bin/activate
pip install lm-polygraph==0.3.0
```

## <a name="basic_usage"></a>Basic usage
```python
python main.py
```


## <a name="Part of the methods"></a>Methods adapted in this paper

<!-- | Uncertainty Estimation Method                                       | Type        | Category            | Compute | Memory | Need Training Data? |
| ------------------------------------------------------------------- | ----------- | ------------------- | ------- | ------ | ------------------- |
| Number of semantic sets (NumSets) (Kuhn et al., 2023)               | Black-box   | Meaning Diversity   | High    | Low    |         No          |
| Sum of eigenvalues of the graph Laplacian (EigV) (Lin et al., 2023) | Black-box   | Meaning Diversity   | High    | Low    |         No          |
| Degree matrix (Deg) (Lin et al., 2023)                              | Black-box   | Meaning Diversity   | High    | Low    |         No          |
| Eccentricity (Ecc) (Lin et al., 2023)                               | Black-box   | Meaning Diversity   | High    | Low    |         No          |
| Lexical similarity (LexSim) (Fomicheva et al., 2020a)               | Black-box   | Meaning Diversity   | High    | Low    |         No          | -->


