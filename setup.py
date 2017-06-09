from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    author='Steven E. Lamberson, Jr.',
    author_email='steven.lamberson@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Topic :: Games/Entertainment :: Role-Playing'
    ],
    description='A tool to help tabletop RPG game masters plan and run their games.',
    install_requires=['pip-tools'],
    license='Apache Software License v2.0',
    long_description=readme(),
    name='acolytegm',
    packages=['acolytegm',],
    url='https://github.com/lamberss/acolytegm',
    version='0.1.0.dev2'
)
