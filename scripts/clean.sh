#!/usr/bin/env bash

echo clean up
echo killing PID: $1
kill -9 $1
rm viewer/__viewer_cache__/cmp_exp
rm -f  viewer/__viewer_cache__/out.txt
rm -f viewer/__viewer_cache__/a.out
