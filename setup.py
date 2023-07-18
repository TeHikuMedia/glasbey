"""Python setup.py for project_name package"""
import io
import os
from setuptools import find_packages, setup

setup(
    name="glasbey",
    version="0.0.1",
    description="Generate maximally distinct sets of colors ",
    url="https://github.com/TeHikuMedia/glasbey",
    author="taketwo",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=["numpy", "colorspacious", "progressbar"],
    py_modules = ['glasbey', 'view_palette']
)
