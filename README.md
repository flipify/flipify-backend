# flipify-backend

## Description

An easily accessible platform that switch deployment infastructure from one to another.

### Project Stack

Python (Django)
Python (Django Rest Framework)

## Contribution Guidelines

The following are the  guidelines for contributing to this project:

- Fork this repository to get a personal copy on your github account
- To clone the forked repository to your local machine, open command prompt and run:

```bash
git clone https://github.com/flipify/flipify-backend/
```

- Change to the project directory you just cloned

```bash
cd flipify-backend
```

- Set Upstream Remote so that changes can be pulled from upstream to your repository

```bash
git remote add upstream https://github.com/flipify/flipify-backend/
```

- Checkout Your Feature Branch

Feature Branching Workflow means you create a new branch for every feature or issue you are working on.
It is goood practice for the branch name to reflect the issue being issolved.
So if an issue title is **Update ReadMe.md** then our branch name would be **update-readme**.
create and checkout feature branch by running:

```bash
git checkout -b issue-name
```

- Setup Development Environment

To setup the development environment to run project run:

```bash
pip install pipenv
pipenv shell
python manage.py migrate

```

- Set Environment Variables by creating a file called '.env' in the project directory and use the env.sample to create a template for your .env file.

- Run ```python manage.py test``` before and after creating fixing an issue or adding a feature.

- Write test code for any additional code.

- After fixing the issue and passing the tests, commit the changes and push them to the feature branch of your remote origin.

```bash
git add *
git commit -m "feat: descriptive commit message"
git push origin feature-branch-name
```

- Login to your github account and go to the your forked repository and make a pull request.