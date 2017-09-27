# MRaDS-2017-Demo-Study

This is the demo study project at MRaDS Conference 2017.

# Setup

To be able to follow you will have to do the following steps.

## Make sure you have a python 3.5 environment

If not, install [Anaconda](https://www.anaconda.com/download/#macos) or [VirtualEnv](https://virtualenv.pypa.io/en/stable/installation/) and create one.

## Make sure you have a CoRR account.

If not, register and wait for the admin approval.
The admin will approve.
Make sure you can login.
Go to your Dashboard.
Go to your available Tools.
Download the Sumatra Tool Credentials.
It will a file named: Sumatra-config.json
I contains your tool and user credentials to talk to this CoRR instance.

## The study Code

Go to the github page of the [demo](https://github.com/usnistgov/MRaDS-2017-Demo-Study)

Download or git clone the study.
Now you have the study.
Open it as a folder to see what is in there.
Move the Sumatra-config.json file here.
Rename Sumatra-config.json to config.json.

## Sumatra Integrated CoRR

Go to the github page of [corr-sumatra](https://github.com/usnistgov/corr-sumatra)

Install gitpython: 

	$ pip install gitpython.

Install ConfigParser:

	$ pip install ConfigParser

Install Jinja 2.8.1

	$ pip install jinja2==2.8.1

Go to a place outside of the study.
Download or git clone it.
Go inside the folder.
Install the module:

	$ python setup.py install.

## Study Required Libraries

Install [tesseract](https://github.com/tesseract-ocr/tesseract/wiki)
For Mac:

	$ brew install tesseract

For Ubuntu:

	$ sudo apt-get install tesseract-ocr

For all add:

	$ pip install pytesseract
	
For Linux:
	$ sudo apt-get install 

Install graphviz needed by [Dask](https://dask.pydata.org/en/latest/)

	$ pip install graphviz

## Setup Sumatra for the Study

Make sure you have everything in version control with git.
	
	$ git init
	$ git add --all
	$ git commit -m "Setup commit"

Now initialize Sumatra.

	$ smt init -s config.json SEM-Images-Sumatra

## How would you typically run this
	
	$ python setup.py combined.py

## Make sure you go back to the study folder

Run (In your terminal): jupyter notebook
Follow the the Sumatra Notebook
