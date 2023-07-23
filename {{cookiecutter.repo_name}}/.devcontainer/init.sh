#!/bin/bash
# shellcheck disable=SC1083,SC1056,SC1072

owner=$(stat -c '%U' "$HOME/.pre-commit")

if [[ "$owner" == "root" ]]
then
  sudo chown vscode:vscode "$HOME/.pre-commit"
  pre-commit install
  pre-commit install-hooks
{% if cookiecutter.use_terrascan == "y" %}  terrascan init{% endif %}
fi
