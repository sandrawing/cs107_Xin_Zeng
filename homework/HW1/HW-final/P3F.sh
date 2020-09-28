#!/bin/bash
for i in $(find -maxdepth 1 -type f); do echo "${i##*/}" "$(wc -l<"$i")"; done