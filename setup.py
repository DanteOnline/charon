import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dante-charon',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='GNU General Public License v3.0', 
    description='Prepare interface to monitor and increase power and set normal managed mode',
    long_description=README,
    url='https://github.com/DanteOnline/charon',
    author='DanteOnline',
    author_email='iamdanteonline@gmail.com',
    keywords = ['iw', 'dev', 'trxpower', 'monitor', 'managed', 'interface', 'wi-fi'],
    classifiers = [],
    entry_points={
        'console_scripts': [
            'charon = charon.main:main',
        ]
    },
)