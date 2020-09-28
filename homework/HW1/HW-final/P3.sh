#!/bin/bash
grep '[0-9]' apollo13.txt | wc -l > apollo_out.txt
grep --help | grep -e "--count"
ls . | grep ".py$" | wc -l
find . -type f ! -perm -006 | wc -l
find . -type f ! -perm -006 -o -type d ! -perm -006 -maxdepth 1 | wc -l

