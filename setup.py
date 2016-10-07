#!/usr/bin/env python


from setuptools import setup, find_packages


setup(name='redcap-data-parser',
      version='1.0',
      description='redhat parser',
      author='Guillaume de Chambrier',
      author_email='chambrierg@gmail.com',
      url='https://github.com/gpldecha/',
      packages=find_packages(),
      install_requires=[
	'python-docx',
	'openpyxl'
      ],
      scripts=['bin/rcparse.py']	
)
