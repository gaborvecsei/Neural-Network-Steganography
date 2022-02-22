FROM tensorflow/tensorflow:2.7.1-gpu

WORKDIR /

# Jupyter Lab&Notebook install
RUN pip install jupyterlab

# Installing the required packages
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# This folder is required for Jupyter Lab/Notebook
RUN mkdir -p /.local && chmod a+rw /.local

# Start the notebook server
ENTRYPOINT jupyter lab --ip 0.0.0.0 --port 8888

