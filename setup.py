from setuptools import (
    find_packages,
    setup,
)

with open("README.md", "r") as fh:
    long_description = fh.read()
    setup(
        name='web3fsnpy',  
        version='0.9.5',
        scripts=['fsnpyscript'] ,
        author="Marcel Cure",
        author_email="marcel.cure@gmail.com",
        description="A Fusion extension to the web3.py package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/FUSIONFoundation/web3fsnpy",
        packages=find_packages(),
        install_requires=[
            "attrdict>=2.0.1",
            "attrs>=19.1.0",
            "base58>=1.0.3",
            "certifi>=2019.9.11",
            "chardet>=3.0.4",
            "cytoolz>=0.10.0",
            "eth-abi>=2.0.0",
            "eth-hash>=0.2.0",
            "eth-keyfile>=0.5.1",
            "eth-rlp>=0.1.2",
            "eth-typing>=2.1.0",
            "eth-utils>=1.7.0",
            "hexbytes>=0.2.0",
            "idna>=2.8",
            "ipfshttpclient>=0.4.12",
            "jsonschema>=3.0.2",
            "lru-dict>=1.1.6",
            "multiaddr>=0.0.8",
            "netaddr>=0.7.19",
            "parsimonious>=0.8.1",
            "protobuf>=3.9.2",
            "pycryptodome>=3.9.0",
            "pyrsistent>=0.15.4",
            "python-dateutil>=2.8.0",
            "requests>=2.22.0",
            "rlp>=1.1.0",
            "six>=1.12.0",
            "toolz>=0.10.0",
            "urllib3>=1.25.6",
            "varint>=1.0.2",
            "web3>=5.1.0",
        ],
        setup_requires=['setuptools-markdown'],
        classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         'Programming Language :: Python :: 3.7',
         'Natural Language :: English',
        ],
        keywords=[
            'Fusion Protocol','blockchain','Decentralized finance',
        ],
        python_requires='>=3.6',
    )