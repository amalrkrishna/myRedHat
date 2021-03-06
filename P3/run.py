#!/usr/bin/env python

"""  $ python run.py runserver 0:8080  """

"""
Programming test: Basic Web Container

Write a python program to cater basic web container needs. Your program should be a mini web framework which should be able for:

1) URL mapping to controller
2) template rendering
3) http request handling

Scenario: Suppose we have three python scripts say urls.py, controller.py, run.py and one html index.html where urls.py shall contain urls to controller and template mapping, controller.py should return template context and run.py to handle server functions. So, this python script should be able to render this html with its context on browser and hence should contain a simple http server inbuilt. Kindly keep this implementation limited to simple and basic web page rendering.

Note: The Project has used default deployment files from Django project. I needed to work mainly only with the templates and run.py, controller.py and urls.py.  

"""

__author__		= "Amal Krishna R"
__date__		= "06/07/2016"

from django.core.management import execute_from_command_line
import os
import sys

if __name__ == "__main__":
	#set the Django environment and parse the command line arguments.
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "source.settings")
	execute_from_command_line(sys.argv)
