#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


# Borrowed from here: https://blog.ionelmc.ro/2014/05/25/python-packaging/


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


setup(
    name="arlo-e2e",
    version="0.1.0",
    license="AGPLv3",
    description="arlo-e2e: e2e verified risk-limiting audits",
    # long_description='%s\n%s' % (
    #     re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
    #     re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    # ),
    author="Dan S. Wallach",
    author_email="dwallach@voting.works",
    url="https://github.com/votingworks/arlo-e2e",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        # "Programming Language :: Python :: Implementation :: PyPy",
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        "Topic :: Utilities",
    ],
    project_urls={
        "Changelog": "https://github.com/votingworks/arlo-e2e/blob/master/CHANGELOG.rst",
        "Issue Tracker": "https://github.com/votingworks/arlo-e2e/issues",
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=">=3.8",
    tests_require=["hypothesis==5.9.0"],
    install_requires=[
        "gmpy2==2.1.0b4",
        "numpy==1.18.2",
        "pandas==1.0.4",
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=["pytest-runner",],
    entry_points={
        #         'console_scripts': [
        #             'nameless = nameless.cli:main',
        #        ]
    },
)
