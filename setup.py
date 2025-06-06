from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)-> List[str]:
    '''
    this function return list of requirement
    '''
    requirement =[]
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement= [req.replace("\n", "") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    return requirement





setup(
    name = "mlproject",
    version = "0.0.1",
    author = "aditya",
    author_email= "adityapandey8349@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirement.txt")



)
