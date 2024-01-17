# Copyright 2015 Ocado Innovation Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup file for django-closuretree."""
import os
import re

from setuptools import setup, find_packages


def get_version(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding="utf-8") as handle:
        content = handle.read()
    return re.search(r'__version__ = "([^"]+)"', content).group(1)


setup(
    name='django-closuretree',
    version=get_version('closuretree/__init__.py'),
    packages=find_packages(),
    author='Mike Bryant',
    author_email='mike.bryant@ocado.com',
    description='Efficient tree-based datastructure for Django',
    long_description=open('README.rst').read(),
    url='https://github.com/vndly-oss/django-closuretree',
    install_requires=[
        'django >= 2.0, < 5.0',
        'six >= 1.13, < 2.0'
    ],
    tests_require=['django-setuptest >= 0.2.1'],
    test_suite='setuptest.setuptest.SetupTestSuite',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
