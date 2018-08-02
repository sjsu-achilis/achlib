from setuptools import setup, find_packages

#dependency_links = ['git+https://github.com/trusty/python-xmp-toolkit.git#egg=dutaxmptoolkit']
dependencies = [
    psycopg2==2.7.5
]

setup(
    name="achlib",
    version="0.1",
    packages=find_packages(),
    install_requires=dependencies,
    package_data={"": ["*.ini"]},
)
