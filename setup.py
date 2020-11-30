# This file was auto-generated by Shut. DO NOT EDIT
# For more information about Shut, check out https://pypi.org/project/shut/

from __future__ import print_function
import io
import os
import setuptools
import sys

readme_file = 'README.md'
if os.path.isfile(readme_file):
  with io.open(readme_file, encoding='utf8') as fp:
    long_description = fp.read()
else:
  print("warning: file \"{}\" does not exist.".format(readme_file), file=sys.stderr)
  long_description = None

requirements = [
  'click',
  'pyserial',
]

setuptools.setup(
  name = 'digital-multimeter',
  version = '0.0.1',
  author = 'Nicholas de Jong',
  author_email = 'contact@nicholasdejong.com',
  description = 'Digital Multimeter provides both a CLI interface and a Python3 library interface to receive data from a variety of digital multimeters.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://pypi.python.org/pypi/digital-multimeter/',
  license = 'MIT',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'tests', 'tests.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = {},
  tests_require = [],
  python_requires = '>=3.5.0,<4.0.0',
  data_files = [],
  entry_points = {},
  cmdclass = {},
  keywords = [],
  classifiers = [],
  zip_safe = True,
)
