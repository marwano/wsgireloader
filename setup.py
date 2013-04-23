
from setuptools import setup
import re

readme = open('README.rst').read()
changes = open('CHANGES.txt').read()
version = re.findall("__version__ = '(.*)'", open('wsgireloader.py').read())[0]
try:
    version = __import__('utile').git_version(version)
except ImportError:
    pass

setup(
    name='wsgireloader',
    version=version,
    description="Automatically reload wsgi applications",
    long_description=readme + '\n\n' + changes,
    keywords='wsgireloader',
    author='Marwan Alsabbagh',
    author_email='marwan.alsabbagh@gmail.com',
    url='https://github.com/marwano/wsgireloader',
    license='BSD',
    py_modules=['wsgireloader'],
    namespace_packages=[],
    include_package_data=True,
    install_requires=[
        'filewatcher>=0.1',
        'utile>=0.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
