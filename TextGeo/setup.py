import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textgeo", # Replace with your own username
    version="0.0.2",
    author="Sathappan Muthiah",
    author_email="sathap1@vt.edu",
    description="Geocode text content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sathappanspm/geocoding",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'wheel',
        'elasticsearch-dsl>=7.0.0,<8.0.0',
        'gevent',
        'nltk',
        'numpy',
        'unicodecsv',
        'Unidecode',
    ],
    package_data={
        'textgeo': [
            'geoutils/Admin2Info.json',
            'geoutils/adminInfo.json',
            'geoutils/countryInfo.json',
            'geoutils/stopwords.txt',
        ]
    }
)
