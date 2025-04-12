
from setuptools import setup, find_packages

setup(
    name='ptw_integration',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'openpyxl'
    ],
    author='Nick B',
    description='PTW data integration for FPDS and GSA CALC sources',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ]
)
