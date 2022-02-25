# Hiding Secrets and Malware in Neural Networks - NN Steganography

Hide some secret data in a Neural Network - text, malicious software or watermark your NN.
(As long as you can convert it to bytes, you can hide it.)

A neural network usually contains many parameters which are represented as floating point numbers
(generally 32bit floats). We can modify the bits of the parameters to hide data in the neural network with no or just
a small degradation of the metric (e.g.: accuracy) used to evaluate the NN.

*Unofficial implementation, with understandability in mind (verbose implementation)*

# Method

I could write about it, but with some pseudo code you'll understand better

```python
# Init an already trained model and a dataset containing images
model = load_model("resnet50", weights="imagenet")
dataset = create_dataset()

# Test the model without any modifications
original_predictions = model.predict(dataset)

# Hide the secret in the model weights - this modifies the float values in the model
secret = read_secret()
hide_secret_in_model(model, secret, bit_to_use=8)

# With the modified weights make predictions for the same dataset
modified_predictions = model.predict(dataset)

# From here we can check what predictiosn changed in the model and adjust the hiding of the secret if necessary
nb_predictions_changed = calculate_changes(original_predictions, modified_predictions)
```

# Run

Build the docker image

```shell
docker build -t stego_nn .
```

Run the image - this will create a jupyter notebook instance

*(<DATA> is a folder where you have the images used for testing)*

```shell
docker run -d --rm --name stegonn -p 8888:8888 -v $(pwd):/code -v <DATA>:/data --gpus '"device=0"' -u $(id -u):$(id -g) stego_nn

docker exec stegonn jupyter lab list

# Now you can open http://<IP>:8888 for the jupyter notebook server
```

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

> This repo does not encourage anyone to use such techniques to commit anything illegal. Its only intention it to
> experiment with hiding secrets in neural networks

