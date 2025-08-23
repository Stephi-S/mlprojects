from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
      this function return the list of requirements
    '''
    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name ='mlprojects',
    version='0.0.1',
    author='Stephi',
    author_email='stephisajeev1997@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)