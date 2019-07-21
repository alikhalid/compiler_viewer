#!/usr/bin/env bash

echo clean up
kill $(ps aux | grep 'viewer.py' | awk '{print $2}')
rm viewer/__viewer_cache__/cmp_exp
rm -f  viewer/__viewer_cache__/out.txt
rm -f viewer/__viewer_cache__/a.out
