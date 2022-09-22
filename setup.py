from setuptools import setup
from setuptools import setup, find_packages

REQUIREMENT_FILE_NAME = "requirements.txt"
REMOVE_PACKAGE = "-e ."


def get_requirement_list(requirement_file_name=REQUIREMENT_FILE_NAME) -> list:
    try:
        requirement_list = None
        with open(requirement_file_name) as requirement_file:
            requirement_list = [requirement.replace("\n", "") for requirement in requirement_file]
            requirement_list.remove(REMOVE_PACKAGE)
        return requirement_list
    except Exception as e:
        raise e


setup(
    name='dt2_sk2co',
    version='1.1',
    packages=['detector_function'],
    url='',
    license='',
    author='mayuresh',
    author_email='mayuresh.gawai4799@gmail.com',
    description=''
)
