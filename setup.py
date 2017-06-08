from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='acolytegm',
    version='0.1dev',
    packages=['acolytegm',],
    license='Apache 2.0',
    long_description=readme()
)
