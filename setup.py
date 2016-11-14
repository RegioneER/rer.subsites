# -*- coding: utf-8 -*-
"""
This module contains the tool of rer.subsites
"""
import os
from setuptools import setup, find_packages

version = '1.3.1.dev0'

tests_require = ['zope.testing']

setup(name='rer.subsites',
      version=version,
      description="Subsites for ER portals",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='https://rersvn.ente.regione.emr.it/svn/plone/prodotti/rer.subsites/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rer', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'archetypes.schemaextender',
                        'plone.app.imaging',
                        'plone.api',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='rer.subsites.tests.test_docs.test_suite',
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
