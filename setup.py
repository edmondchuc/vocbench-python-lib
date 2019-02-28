import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open_local(['requirements.txt']) as req:
    install_requires = req.read().split("\n")

setuptools.setup(
    name="vocbench",
    version="0.0.1",
    author="Edmond Chuc",
    author_email="edmond.chuc@outlook.com",
    description="A Python library to make requests to an instance of VocBench.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edmondchuc/vocbench-python-lib",
    packages=setuptools.find_packages(),
    license='LICENSE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
)
