#Generate Dockerfile.

#!/bin/sh

 set -e

generate_docker() {
  docker run --rm kaczmarj/neurodocker:0.7.0 generate docker \
             --base neurodebian:stretch-non-free \
             --pkg-manager apt \
             --arg DEBIAN_FRONTEND=noninteractive \
             --miniconda \
               version=latest \
               conda_install="python=3.8" \
               pip_install="nilearn pandas seedir" \
               create_env='bids_atlas' \
               activate=true \
            --run-bash "source activate bids_atlas && conda install -c mrtrix3 mrtrix3" \
            --copy . /home/bids_atlas \
            --run-bash "source activate bids_atlas && cd /home/bids_atlas && pip install -e ." \
            --env IS_DOCKER=1 \
            --workdir '/tmp/' \
            --entrypoint "/neurodocker/startup.sh  bids_atlas"
}

# generate files
generate_docker > Dockerfile

# check if images should be build locally or not
if [ $1 = local ]; then
    echo "docker image will be build locally"
    # build image using the saved files
    docker build -t bids_atlas:local .
else
  echo "Image(s) won't be build locally."
fi            


