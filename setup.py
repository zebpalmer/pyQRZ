from setuptools import setup, find_packages

readme = open('README.rst', 'rt').read()

versionstr = '0.1.0'

setup(
    name='pyQRZ',
    version=versionstr,
    author='Zeb Palmer',
    author_email='zeb@zebpalmer.com',
    package_dir={'qrz': 'qrz'},
    url='http://github.com/zebpalmer/pyQRZ',
    license='MIT',
    description='Query QRZ.com Ham Radio License API',
    long_description=readme,
    install_requires=['requests', 'xmltodict', 'six'],
    use_2to3=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Ham Radio',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
