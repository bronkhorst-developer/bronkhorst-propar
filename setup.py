import setuptools

setuptools.setup(
    name="bronkhorst_propar",
    version="0.5.5",
    url='https://github.com/bronkhorst-developer/bronkhorst-propar',
    author="Bronkhorst",
    author_email="support@bronkhorst.com",
    description="Communicate to Bronkhorst Instruments using the propar protocol over RS232 or RS485.",
    long_description="""
The bronkhorst-propar module provides communication with Bronkhorst (Mass) Flow Meters and Controllers using the default RS232/RS485 interface.

Documentation: https://bronkhorst-propar.readthedocs.io/en/latest/introduction.html

Download Page: https://pypi.org/project/bronkhorst-propar
""",
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