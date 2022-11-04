from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="packageDIO",
    version="0.0.1",
    author="alisson_lima",
    author_email="infoalisson21@gmail.com",
    description="Pacote para testes da DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlissonLima19/packageDIO"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
