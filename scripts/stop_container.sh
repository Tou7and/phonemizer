#!/bin/bash

CONTAINER=phonemizer_x

docker stop $CONTAINER
docker rm $CONTAINER

