from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksDBMS',
    version='0.1.4',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks DB Management System.',
    install_requires=[
        'flask',
        'flask-cors',
        'pymongo',
        'psycopg2',
        'simplejson'
    ],
    url='http://pypi.python.org/pypi/GeobricksDBMS/'
)
