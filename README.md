# BCI-GGN

## Usage

This is a repository for the project "A Probabilistic Graphical Model for Motor
Imagery Brain Computer Interfaces." This file provides instructions for running
each of the experiments in the project, and _DataProcessing.py_ is a script for
preprocessing BCI data as described in the paper. All of the experiments were
done by modifying code from [GGN](https://github.com/ICLab4DL/GGN) and do not
include separate scripts.

## Instructions

### Setup

1.  Clone [GGN](https://github.com/ICLab4DL/GGN) and set up its environment as
    provided.
2.  Download the Exp1 and Exp2 datasets from [Meng and
    He](https://figshare.com/articles/online_resource/Shared_data_for_exploring_training_effect_in_42_human_subjects_using_a_noninvasive_sensorimotor_rhythm-based_online_BCI/7959572).
3.  Copy _adjs/raw_bci_adj.npy_ to the same location in the GGN repository.

### Preprocessing

### Experiments

The instructions for each experiment below assume that the state of the GGN
repository has been reset between each experiment.

#### Transposed

1.  Change all instances of `20` (the electrode or channel count) to `58` in
    _eeg_main.py_.
2.  Change all instances of `7` (the class count) to `2` in _eeg_main.py_.
3.  Change all instances of `34` (the first feature dimension, in this case
    frequency count) to `51` in ggn.py.
4.  Run _training.sh_ with the following parameters:
