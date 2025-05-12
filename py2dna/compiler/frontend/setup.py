
from setuptools import setup, find_packages

setup(
    name='py2dna',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'py2dna=py2dna.main:main',  # ajuste se houver função main
        ]
    },
    author='Luis Claudio DeVita',
    description='Compilador de lógica para DNA',
    license='MIT',
)
