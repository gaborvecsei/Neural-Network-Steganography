# Hiding Secrets and Malware in Neural Networks - NN Steganography

Hide some secret data in a Neural Network - text, malicious software or watermark your NN.
(As long as you can convert it to bytes, you can hide it.)

A neural network usually contains many parameters which are represented as floating point numbers
(generally 32bit floats). We can modify the bits of the parameters to hide data in the neural network with no or just
a small degradation of the metric (e.g.: accuracy) used to evaluate the NN.

*Unofficial implementation, with understandability in mind (verbose implementation)*

# Citations

```bibtex
@article{DBLP:journals/corr/abs-2107-08590,
  author    = {Zhi Wang and Chaoge Liu and Xiang Cui},
  title     = {EvilModel: Hiding Malware Inside of Neural Network Models},
  journal   = {CoRR},
  volume    = {abs/2107.08590},
  year      = {2021},
  url       = {https://arxiv.org/abs/2107.08590},
  eprinttype = {arXiv},
  eprint    = {2107.08590},
  timestamp = {Thu, 22 Jul 2021 11:14:11 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2107-08590.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

```bibtex
@article{DBLP:journals/corr/abs-2109-04344,
  author    = {Zhi Wang and Chaoge Liu and Xiang Cui and Jie Yin},
  title     = {EvilModel 2.0: Hiding Malware Inside of Neural Network Models},
  journal   = {CoRR},
  volume    = {abs/2109.04344},
  year      = {2021},
  url       = {https://arxiv.org/abs/2109.04344},
  eprinttype = {arXiv},
  eprint    = {2109.04344},
  timestamp = {Tue, 21 Sep 2021 17:46:04 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2109-04344.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

```bibtex
@inproceedings{10.1145/3427228.3427268,
  author = {Liu, Tao and Liu, Zihao and Liu, Qi and Wen, Wujie and Xu, Wenyao and Li, Ming},
  title = {StegoNet: Turn Deep Neural Network into a Stegomalware},
  year = {2020},
  isbn = {9781450388580},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3427228.3427268},
  doi = {10.1145/3427228.3427268},
  booktitle = {Annual Computer Security Applications Conference},
  pages = {928–938},
  numpages = {11},
  location = {Austin, USA},
  series = {ACSAC '20}
}
```

