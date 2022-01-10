from setuptools import setup, find_packages
import os
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent
README = (CURRENT_DIR / "readme.md").read_text()

env = os.environ.get('dev')


def get_dependencies():
    dependency = [
        'Flask',
        'Flask-SQLAlchemy'
    ]

    if env and env == "dev":
        return dependency

    return dependency + ["PF-PY-Common"]


setup(
    name='PF-Flask-DB',
    version='1.0.0',
    url='https://github.com/problemfighter/pf-flask-db',
    license='Apache 2.0',
    author='Problem Fighter',
    author_email='problemfighter.com@gmail.com',
    description='Flask Database Manager by Problem Fighter Library',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=get_dependencies(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ]
)
