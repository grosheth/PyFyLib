from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

install_reqs = [
    'spotipy==2.23.0'
    'python-dotenv==1.0.1'
]

setup(
    name='pyfylib',
    version='0.0.1',
    description='Work In Progress! Small project that uses Spotipy features',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="@salledelavage",
    author_email="",
    url='',
    project_urls={
        'Source': 'https://github.com/grosheth/PyFyLib',
    },
    python_requires='>3.11',
    install_requires=install_reqs,
    license='MIT',
    packages=['pyfylib'])
