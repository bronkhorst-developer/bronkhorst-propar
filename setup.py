import setuptools

try:
    with open('readme.md', 'r') as f:
        long_description = f.read()
except:
    long_description = ""

setuptools.setup(
    name="bronkhorst_propar",
    version="1.2.0",
    url='https://github.com/bronkhorst-developer/bronkhorst-propar',
    author="Bronkhorst",
    author_email="support@bronkhorst.com",
    description="Communicate to Bronkhorst Instruments using the propar protocol over USB, RS232, or RS485.",
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