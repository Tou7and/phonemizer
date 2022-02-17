#!/bin/bash

# IMAGE_NAME=tou7and/phonemizer:3.0.1
# - based on https://github.com/bootphon/phonemizer
# - add app.py for supportting restful api

IMAGE_NAME=tou7and/phonemizer:3.0.1-mk2
# - add separator for phone separation
# - add a work-around error handling mechanics

docker build . -t $IMAGE_NAME

