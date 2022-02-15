#!/bin/bash

IMAGE=tou7and/phonemizer:3.0.1
CONTAINER=phonemizer_x

docker stop $CONTAINER
docker rm $CONTAINER

# docker run --name phonemizer_x -d -it -v "$(pwd)"/tmp:/phonemizer/data tou7and/phonemizer:3.0.1 /bin/bash
docker run --name $CONTAINER -d -it -p 5566:5000 $IMAGE

