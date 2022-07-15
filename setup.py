#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'requests', 'tqdm']

test_requirements = ['pytest>=3', ]

setup(
    author="Core.Today",
    author_email='engine@core.today',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Core.Today Dataset Management Library",
    entry_points={
        'console_scripts': [
            'coredotdata=coredotdata.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='coredotdata',
    name='coredotdata',
    packages=find_packages(include=['coredotdata', 'coredotdata.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/CoreDotToday/coredotdata',
    version='0.3.0',
    zip_safe=False,
)
