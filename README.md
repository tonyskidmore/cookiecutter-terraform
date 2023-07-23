[![GitHub Super-Linter](https://github.com/tonyskidmore/cookiecutter-terraform/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

# cookiecutter-terraform

1. [Overview](#overview)
2. [Usage](#usage)

## Overview

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) Terraform template for Azure modules or projects.


## Usage

Install [cookiecutter](https://github.com/cookiecutter/cookiecutter) to do all the work.

First, get Cookiecutter and install other required libraries. Here is an example using a Python virtual environment in Linux:

````bash

mkdir ~/venvs
python3 -m venv ~/venvs/cookiecutter
source ~/venvs/cookiecutter/bin/activate
pip install pip setuptools --upgrade
pip install cookiecutter
pip install pyyaml

````

Then run it against this repo:

````bash

cookiecutter https://github.com/tonyskidmore/cookiecutter-terraform

````

You'll be prompted for some values. Provide them, then a Terraform project will be created for you.


Answer the prompts with your own options. For example, creating a Terraform Azure module for Machine Learning:

````bash

project_name [project_name]: terraform-azurerm-machine-learning
repo_name [repo_name]: terraform-azurerm-machine-learning
full_name [Your Name]: Tony Skidmore
email [Your email]: 16082810+tonyskidmore@users.noreply.github.com
project_short_description [A short description of the project.]: Terraform module for Azure Machine Learning
Select license:
1 - BSD 2-Clause License
2 - BSD 3-Clause License
3 - MIT license
4 - ISC license
5 - Apache Software License 2.0
6 - GNU Lesser General Public License v3 or later (LGPLv3+)
7 - GNU Lesser General Public License v3 (LGPLv3)
8 - GNU Lesser General Public License v2.1 or later (LGPLv2+)
9 - GNU Lesser General Public License v2.1 (LGPLv2)
10 - no
Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 [1]: 3
version [0.0.1]:
use_checkov [y]:
use_terrascan [y]: n
year_from [2023]:
year_to [2023]:

````

Enter the project and take a look around:

````bash

cd terraform-azurerm-machine-learning/
ls

````

Create a git repo in GitHub and then push to it:

````bash

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:tonyskidmore/terraform-azurerm-machine-learning.git
git push -u origin main

````
