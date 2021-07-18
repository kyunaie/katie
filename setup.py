from setuptools import setup
setup(
    name = 'katie',
    version = '0.1.0',
    packages = ['katie'],
    entry_points = {
        'console_scripts': [
            'katie = katie.__main__:main'
        ]
    })