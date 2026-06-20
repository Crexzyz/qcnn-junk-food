# QCNN for Junk Food classification

This repository shares the models and quantum circuits used in the paper `Quantum Machine Learning for Food Classification in Advertisements`, to be published at [CLEI 2026](https://conferencia2026.clei.org/), in the [TLISC track](https://www.ripaisc.net/tlisc-2026/). Paper DOI: `TBD`

Please note that the original datasets are not included in this repository.

# Folder structure

1. `src`: contains a set of subfolders with code for building the models
    1. `headless`: contains the files that built and trained the models with the original configuration as reported in the paper.
    1. `datasets`: contains a PyTorch-derived custom dataset used to train the models.
    1. `qml`: contains the encoders, ansatz, measurements, and hybrid PyTorch layer used to build the Quantum Convolution block.
    1. `training`: contains utility training logic that also collected metrics for benchmarking across epochs.
1. `results`: contains the training logs, and the PyTorch model that got the best performance during training.
