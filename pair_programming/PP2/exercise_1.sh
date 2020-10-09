#!/bin/bash

read -r -p "Specify file for git: "

file = $1

git add file
git status

read -r -p "Would you like to continue?"

foo = $1
if [ “$foo" = "N"]; then 
	exit 1
fi

read -r -p "Specify a commit message: "

commit_name = $1
git commit -m commit_name

git status

read -r -p "Would you like to continue?"

foo = $1
if [ “$foo" = "N"]; then 
	exit 1
fi

git push