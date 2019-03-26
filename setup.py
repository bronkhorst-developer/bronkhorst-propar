import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bronkhorst_propar",
    version="0.2.3",
    author="Bronkhorst",
    author_email="support@bronkhorst.com",
    description="Communicate to Bronkhorst Instruments using the Propar protocol over RS232 or RS485.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=[
        'pyserial',
    ],
)