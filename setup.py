#project management script

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requriments = f.read().splitlines()

setup(
    name="mlops-hotel-project",
    version="0.1",
    author= "Rakibul Islam",
    packages= find_packages(),
    install_requires = requriments,
)