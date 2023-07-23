#!/bin/bash
# shellcheck disable=all

owner=$(stat -c '%U' "$HOME/.pre-commit")

if [[ "$owner" == "root" ]]
then
  sudo chown vscode:vscode "$HOME/.pre-commit"
  pre-commit install
  pre-commit install-hooks
{% if cookiecutter.use_terrascan == "y" %}  terrascan init{% endif %}
fi
