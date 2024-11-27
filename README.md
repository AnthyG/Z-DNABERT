# DNABERT-Z

## Modifications by Garratt

### Installation

#### Prerequisites

Native system or Virtual Machine with at least around 30 GB free.

The systems is required to provide the following commands:

- `mkdir`
- `cp`

#### Dependencies

##### NixOS

On NixOS, all dependencies are already included in the file `shell.nix`, no manual installation of dependencies is required.

###### Nvidia CUDA

Nvidia CUDA allows for faster execution of the Notebook at hand by utilizing the GPU instead of the CPU. From a select few tests, it seems to increase the iterations per second about tenfold when using a AMD Ryzen 9 5900HX CPU and a NVIDIA GeForce RTX 3070 Laptop (Mobile) GPU.

To run the Jupyter Notebook with CUDA support enabled, some manual adjusting needs to be done.

The file `shell.nix` has to be edited, specifically `#` in the line containing `#    cudaPackages.cudatoolkit` has to be removed.

If you want the exact python pip package versions, remove all `#` from the file `requirements.txt`.

Furthermore, it seems to be necessary to include the following lines in `/etc/nixos/configuration.nix`.
If you have any advice on how to solve this via a `shell.nix`-File, please let me know! The documentation on how to use CUDA on NixOS seems to be outdated or at least didn't work out of the box for me.

```nix
systemd.services.nvidia-control-devices = {
  wantedBy = [ "multi-user.target" ];
  serviceConfig.ExecStart = "${pkgs.linuxPackages.nvidia_x11.bin}/bin/nvidia-smi";
};
```

##### Debian / Ubuntu

For Debian / Ubuntu, the following two commands should suffice:

```sh
sudo apt install gcc curl python3.11 python3-pip
python3.11 -m pip install --user virtualenv
```

##### Other

On other systems, dependencies may need to be installed manually if the previous sections are not applicable. Please refer to the previous install commands for Debian / Ubuntu and the `shell.nix` file for NixOS to derive the required setup for your system.

### Usage

#### Starting JupyterLab

On the first run, starting up might take a while, because the python dependencies required to run the Notebook will be installed.

##### NixOS

To start JupyterLab on NixOS, the following command needs to be executed:

```sh
nix-shell
```

##### Debian / Ubuntu / Other

To start JupyterLab on Debian / Ubuntu and potentially other systems, the following command needs to be executed:

```sh
bash ./run.sh
```

#### Using the Notebook

Once JupyterLab has opened, open the notebook `ZDNA-prediction.local.ipynb` in JupyterLab.

The big blue link at the very top with the title "Jump to Run Section" can be used to jump to the "Run"-Section, if you feel like it takes too long to scroll down.

The "Run"-Section contains further information on how to use the notebook.

## Original README

This repository contains code and data for the article ["Z-Flipon Variants reveal the many roles of Z-DNA and Z-RNA in health and disease"](https://www.biorxiv.org/content/10.1101/2023.01.12.523822v1.abstract)

The full genome predictions for human and mouse genomes can be downloaded [here](https://github.com/mitiau/Z-DNABERT/tree/main/beds)

To predict Z-DNA flipons on new data please use [this colab notebook](https://colab.research.google.com/github/mitiau/Z-DNABERT/blob/main/ZDNA-prediction.ipynb)

The finetuned DNABERT weights can be downloaded from google drive:
- [MM Kouzine data](https://drive.google.com/drive/folders/1JXJc9G6BQUIpvjATthv9Xyyp2uVRPz-h?usp=share_link)
- [MM Shin data](https://drive.google.com/drive/folders/1fvTX1MHq7Gn80SYa7ibqQEHMbvsT5cHl?usp=share_link)
- [HG Kouzine data](https://drive.google.com/drive/folders/1FbM8fDTWQ5hYLQVWv7F9okNE9DlXY7kY?usp=share_link)
- [HG Shin data](https://drive.google.com/drive/folders/1-3Ntyyjp-JfJ_V2ZXORedCDihAgckRQV?usp=share_link)

## Files in this repository

1_HG_chipseq.ipynb - Generate data splits for HG data with Chipseq labels. Train the models. Generate full genome predictions.

1_HG_kousine.ipynb - Generate data splits for HG data with Kouzine labels. Train the models. Generate full genome predictions.

1_MM_curax.ipynb - Generate data splits for MM data with Curax labels. Train the models.

1_MM_kousine.ipynb - Generate data splits for MM data with Kouzine labels. Train the models.

2_Generate_stats_hg_chipseq.ipynb - Calculate most frequently attended k-mers for HG data with Chipseq labels.

2_Generate_stats_hg_kouzine.ipynb - Calculate most frequently attended k-mers for HG data with Kouzine labels.

2_Generate_stats_mm_curax.ipynb - Generate full genome predictions for MM data with Curax labels. Calculate most frequently attended k-mers.

2_Generate_stats_mm_kouzine.ipynb - Generate full genome predictions for MM data with Kouzine labels. Calculate most frequently attended k-mers.

README.md - This file

ZDNA-prediction.ipynb - Standalone notebook for prediction of Z-DNA. Intended to be run in colab enviroment via: https://colab.research.google.com/github/mitiau/Z-DNABERT/blob/main/ZDNA-prediction.ipynb
