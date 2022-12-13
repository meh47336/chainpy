#!/bin/bash

chainpy() {
  heterodimers=$1
  cd $heterodimers
  python3 ../../chainpy.py
  cd ../..
}
export -f chainpy
ls -d */heterodimer_* | parallel -j 30 chainpy
