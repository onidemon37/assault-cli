# assault-cli
Tutorial into buildind a cli tool, using click and python

## requirements
- [pre-commit](https://pre-commit.com/)
- (setup.py)

## setup.py (for humans)
This repo exists to provide an example setup.py file, that can be used to bootstrap your next Python project. It includes some advanced patterns and best practices for setup.py, as well as some commented–out nice–to–haves.

For example, this setup.py provides a $ python setup.py upload command, which creates a universal wheel (and sdist) and uploads your package to PyPi using Twine, without the need for an annoying setup.cfg file. It also creates/uploads a new git tag, automatically.

In short, setup.py files can be daunting to approach, when first starting out — even Guido has been heard saying, "everyone cargo cults thems". It's true — so, I want this repo to be the best place to copy–paste from :)

Check out the example!

* Installation
cd your_project

```
## Download the setup.py file:
## download with wget
wget https://raw.githubusercontent.com/navdeep-G/setup.py/master/setup.py -O setup.py
```

```
## download with curl
curl -O https://raw.githubusercontent.com/navdeep-G/setup.py/master/setup.py
```

* To Do
Tests via `$ setup.py` test (if it's concise).
Pull requests are encouraged!

### More Resources
What is setup.py? on Stack Overflow
Official Python Packaging User Guide
The Hitchhiker's Guide to Packaging
Cookiecutter template for a Python package
