'''
To define the configuration of the project, its metadata, dependencies and more. 
It is essential for packaging and distributing the project.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)


    except FileNotFoundError:
        print("requirements.txt file not found")

    
    return requirement_lst

setup(
    name="ETL_MLOPS",
    version="0.0.1",
    author="Shivanshi Agarwal",
    author_email="shivanshi.agarwal@okstate.edu",
    packages=find_packages(),
    install_requires= get_requirements()
)