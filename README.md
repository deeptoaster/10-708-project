# BCI-GGN

## Usage

This is a repository for the project "A Probabilistic Graphical Model for Motor
Imagery Brain Computer Interfaces." This file provides instructions for running
each of the experiments in the project, and the _preprocessing_ directory
contains scripts for preprocessing BCI data as described in the paper. All of
the experiments were done by modifying code from
[GGN](https://github.com/ICLab4DL/GGN) and do not include separate scripts.

## Instructions

### Setup

### Preprocessing

We were able to obtain 28 subjects out of the 37 subjects available in the online BCI dataset [3].
Each subject underwent 3 sessions of 120 trials. For each of the 10800 trails, the EEG data was
normalized to 1000 timesteps (1 second) and 62 channels for shape consistency, and a single lable of
0 or 1 was made for left-target trial and right-target trial, respectively

### Experiments
