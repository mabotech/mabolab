import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'simplejson',
    'SQLAlchemy',    
    'zope.interface',
    'flask',    
    'pyro',
    ]

setup(name='mabolab',
      version='0.0.1',
      description='mabolab',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: ",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='MaboTech',
      license='MIT',
      author_email='mabotech@163.com',
      url='http://www.mabotech.com',
      keywords='mabotech lab lib web',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='mabolab',
      install_requires = requires,     
      #data_files=[]

  )

