#!/bin/bash
#coder: Tale Lokvenec
#sharer: Eleonora Shantsila
#listener: Xin Zeng

#Hayoun - we want to take the slower approach an iterate through each of the files in the directory in turn
#Tale - ls l on every file to list the pattern at the beggining and match the experession to see if we can execute
#Eleonora - create an if loop using -x file command



for file in $(find . -type f); do
    if [ -x $file ]; then
        echo "$file"
    fi
done

#Xin - error when running the scrips. Re-running fixes the issue
#Tested with dummy.txt and output was correct