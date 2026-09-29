from setuptools import setup, find_packages

setup(
    name='ImpararePackage',
    version='0.1.0',
    author='João Paulo Carneiro',
    author_email='joaopaulo@portalqualis.com.br',
    description="Pacote com utilitários para os pipelines",
    packages=find_packages(include=["ImpararePackage", "ImpararePackage.*"]),
    install_requires=[
        'pandas>=2.0.3'
    ],
)