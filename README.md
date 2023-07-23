# cookiecutter-terraform

1. [Overview](#overview)
2. [Usage](#usage)

## Overview

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) Terraform template for Azure modules or projects.


## Usage

Install [cookiecutter](https://github.com/cookiecutter/cookiecutter) to do all the work.

First, get Cookiecutter. Here is an example using a Python virtual environment in Linux:

````bash

mkdir ~/venvs
python3 -m venv ~/venvs/cookiecutter
source ~/venvs/cookiecutter/bin/activate
pip install cookiecutter

````

Then run it against this repo:

````bash

cookiecutter https://github.com/tonyskidmore/cookiecutter-terraform

````

You'll be prompted for some values. Provide them, then a Terraform project will be created for you.


Answer the prompts with your own options. For example:

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [My Awesome Project]: Reddit Clone
    project_slug [reddit_clone]: reddit
    description [Behold My Awesome Project!]: A reddit clone.
    author_name [Daniel Roy Greenfeld]: Daniel Greenfeld
    domain_name [example.com]: myreddit.com
    email [daniel-greenfeld@example.com]: pydanny@gmail.com
    version [0.1.0]: 0.0.1
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    Select username_type:
    1 - username
    2 - email
    Choose from 1, 2 [1]: 1
    timezone [UTC]: America/Los_Angeles
    windows [n]: n
    Select an editor to use. The choices are:
    1 - None
    2 - PyCharm
    3 - VS Code
    Choose from 1, 2, 3 [1]: 1
    use_docker [n]: n
    Select postgresql_version:
    1 - 15
    2 - 14
    3 - 13
    4 - 12
    5 - 11
    6 - 10
    Choose from 1, 2, 3, 4, 5 [1]: 1
    Select cloud_provider:
    1 - AWS
    2 - GCP
    3 - None
    Choose from 1, 2, 3 [1]: 1
    Select mail_service:
    1 - Mailgun
    2 - Amazon SES
    3 - Mailjet
    4 - Mandrill
    5 - Postmark
    6 - Sendgrid
    7 - SendinBlue
    8 - SparkPost
    9 - Other SMTP
    Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9 [1]: 1
    use_async [n]: n
    use_drf [n]: y
    Select frontend_pipeline:
    1 - None
    2 - Django Compressor
    3 - Gulp
    4 - Webpack
    Choose from 1, 2, 3, 4 [1]: 1
    use_celery [n]: y
    use_mailhog [n]: n
    use_sentry [n]: y
    use_whitenoise [n]: n
    use_heroku [n]: y
    Select ci_tool:
    1 - None
    2 - Travis
    3 - Gitlab
    4 - Github
    Choose from 1, 2, 3, 4 [1]: 4
    keep_local_envs_in_vcs [y]: y
    debug [n]: n

Enter the project and take a look around:

````bash

cd terraform-azurerm-machine-learning/
ls

````

Create a git repo and push it there:

````bash

git init
git add .
git commit -m "first commit"
git remote add origin git@github.com:tonyskidmore/terraform-azurerm-machine-learning.git
git push -u origin master

````
