""" Installer
"""
from setuptools import setup, find_packages
import os
from os.path import join

NAME = 'edw.highcharts'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description="Highcharts JS lib",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Framework :: Plone",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Programming Language :: Zope",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
      ],
      keywords='eea daviz highcharts plone zope',
      author='Alin Voinea',
      author_email='alin@eaudeweb.ro',
      url='http://github.com/eaudeweb/edw.highcharts',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['edw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
