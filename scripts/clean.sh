#!/usr/bin/env bash

echo clean up
killall -9 viewer.py
rm viewer/__viewer_cache__/cmp_exp
