from setuptools import find_packages, setup

def get_requirements():
    pass

setup(
    name='sensor', #find out sensor folder
    version='0.0.1',
    author='pranay',
    author_email='pmohadikar.94@gmail.com',
    packages=find_packages(), #packages in sensor folder .py
    install_requirements = get_requirements() #libraries required for project function,

    
)