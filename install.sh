#!/bin/bash

installation_command="pip install -r requirements.txt"
echo "$installation_command"
$installation_command

DIR=".git/"
if [ -d "$DIR" ]; then
  precommit_command="pre-commit install"
  echo "$precommit_command"
  $precommit_command
fi
