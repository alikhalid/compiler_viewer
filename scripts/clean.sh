#!/usr/bin/env bash

echo clean up
killall -9 viewer.py
rm viewer/__viewer_cache__/cmp_exp
rm -f  viewer/__viewer_cache__/out.txt
rm -f viewer/__viewer_cache__/a.out
