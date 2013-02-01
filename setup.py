import sys
from setuptools import setup, find_packages

readme = open('README.rst', 'rt').read()

versionstr = '0.0.1a'

setup(
	name='pyQRZ',
    version=versionstr,
    author='Zeb Palmer',
    author_email='zeb@zebpalmer.com',
    packages=['qrz'],
    package_dir={ 'qrz': 'qrz'},
    url='http://github.com/zebpalmer/pyQRZ',
    license='LGPLv3',
    description='Query QRZ.com Ham Radio License API',
    long_description=readme,
    install_requires=['requests', 'xmltodict'],
    use_2to3=True,
    classifiers=[
              'Development Status :: 3 - Alpha',
              'Environment :: Console',
              'Environment :: Plugins',
              'Intended Audience :: Developers',
              'Intended Audience :: Telecommunications Industry',
              'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
              'Natural Language :: English',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.2',
              'Topic :: Software Development :: Libraries :: Python Modules',
              'Topic :: Utilities'
              ],
)


