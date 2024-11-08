#!/bin/bash

if [[ -d build ]]; then
    rm -fr build
fi


#if [[ -e mouseMove.spec ]]; then
#    rm -f  mouseMove.spec
#fi

python setup.py build

./dist/mouseMove.exe  &
