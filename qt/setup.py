from setuptools import setup, find_packages
from cx_Freeze import setup, Executable

# Lista de dependências
install_requires = [
    "pyside6",
    "httpx",
    "dynaconf",
    "pydantic",
    "bcrypt",
    "unidecode",
    "pandas",
    "pandas-stubs"
]


executables = [Executable("app.py", base=None, icon="icon.png")]

setup(
    name="Chiquitos",
    version="0.1.0",
    description="Descrição do seu programa",
    author="Antonio Fernando",
    packages=find_packages(),
    install_requires=install_requires,
    executables=executables
)
