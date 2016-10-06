#!/usr/bin/env python

from distutils.core import setup

setup(name='hbp-parser',
      version='1.0',
      description='redhat parser',
      author='Guillaume de Chambrier',
      author_email='chambrierg@gmail.com',
      url='https://github.com/gpldecha/hbp-parser'
      packages=find_packages(),
      install_requires=[
	'python-docx',
	'openpyxl'
      ]

)
