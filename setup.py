from setuptools import setup, find_packages

dependencies = [
    "psycopg2==2.7.5"
]

setup(
    name="achlib",
    version="0.1",
    packages=find_packages(),
    install_requires=dependencies,
    package_data={"": ["*.ini"]},
)
