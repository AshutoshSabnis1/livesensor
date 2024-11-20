from setuptools import find_packages,setup

def get_requirements()->list[str]:
    requirement_list=list[str]=[]
    return requirement_list

#from typing import list
setup(
    name="sensor",
    version="0.1",
    author="Ashutosh_Sabnis",
    author_email="ashutoshsabnis.24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() #["pymongo"]
)