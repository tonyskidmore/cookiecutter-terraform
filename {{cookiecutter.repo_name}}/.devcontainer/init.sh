#!/bin/bash

owner=$(stat -c '%U' "$HOME/.pre-commit")

if [[ "$owner" == "root" ]]
then
  sudo chown vscode:vscode "$HOME/.pre-commit"
  pre-commit install
  pre-commit install-hooks
  {% if cookiecutter.year_from == cookiecutter.year_to %}
  terrascan init
  {% endif %}
fi