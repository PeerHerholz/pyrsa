#!/bin/sh

set -e

# Generate Dockerfile or Singularity recipe.
generate() {
  docker run --rm repronim/neurodocker:0.7.0 generate "$1" \
    --base=ubuntu:bionic-20201119 \
    --pkg-manager=apt \
    --install "gcc g++ tree git" \
    --user=pyrsa \
    --miniconda \
      conda_install="python=3.7" \
      pip_install='rsa3' \
      create_env="pyrsa" \
      activate=true \
    --workdir='/home/pyrsa' 
  }


generate docker > Dockerfile
generate singularity > Singularity