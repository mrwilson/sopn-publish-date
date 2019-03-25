from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sopn-publish-date",
    url="https://github.com/mrwilson/sopn-publish-date",
    version="0.1.0",
    description="Derive publish dates of Statements of Persons Nominated for UK elections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alex Wilson",
    author_email="alex+github@probablyfine.co.uk",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=("pandas"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Topic :: Software Development :: Documentation",
    ],
)
