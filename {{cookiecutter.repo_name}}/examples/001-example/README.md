# 001-example

This is a minimal example of using the content in this repository.

````bash

git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git

cd examples/001-example
terraform init
terraform plan -out tfplan
terraform apply tfplan

````

<!-- BEGIN_TF_DOCS -->

<!-- END_TF_DOCS -->