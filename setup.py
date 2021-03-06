from setuptools import setup
import os
import sys

if (sys.version_info.major == 2 and sys.version_info.minor == 7) or\
    (sys.version_info.major == 3 and sys.version_info.minor == 5) or\
    (sys.version_info.major == 3 and sys.version_info.minor == 6) or\
    (sys.version_info.major == 3 and sys.version_info.minor == 7):
    print('[SETUP] bayeso supports Python {}.{} version in this system.'.format(sys.version_info.major, sys.version_info.minor))
else:
    sys.exit('[ERROR] bayeso does not support Python {}.{} version in this system.'.format(sys.version_info.major, sys.version_info.minor))

path_requirements = 'requirements.txt'
list_packages = ['bayeso', 'bayeso.utils']

with open(path_requirements) as f:
    required = f.read().splitlines()

setup(
    name='bayeso',
    version='0.4.1',
    author='Jungtaek Kim',
    author_email='jtkim@postech.ac.kr',
    url='http://bayeso.org',
    license='MIT',
    description='Simple, but essential Bayesian optimization package',
    packages=list_packages,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, != 3.3.*, !=3.4.*, <4',
    install_requires=required,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
