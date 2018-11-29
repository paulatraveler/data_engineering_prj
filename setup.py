from setuptools import setup, find_packages

__version__ = '0.1'


def read_requirements():
    with open('requirements.txt') as f:
        return [line for line in f.readlines()]


setup(
    name='datascience_interview',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=read_requirements()
)