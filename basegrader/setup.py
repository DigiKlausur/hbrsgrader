# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='grader',
    version='0.0.1',
    description='Grader',
    author='Tim Metzler',
    author_email='tim.metzler@h-brs.de',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data = True,
    data_files = [
        ("share/grader", [
            "config/README.md"
        ]),
        ("etc/jupyter/jupyter_notebook_config.d", [
            "jupyter-config/jupyter_notebook_config.d/grader.json"
        ])
    ],
    zip_safe=False
)
