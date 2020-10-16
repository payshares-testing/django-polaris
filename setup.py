from setuptools import setup, find_packages


with open("README.rst") as f:
    long_description = f.read()

setup(
    name="django-polaris",
    version="1.1.2",
    description="An extendable Django server for Stellar Ecosystem Proposals",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://django-polaris.readthedocs.io/en/stable",
    author="Jake Urban",
    author_email="jake@stellar.org",
    license="Apache license 2.0",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=[
        "stellar",
        "sdf",
        "anchor",
        "server",
        "polaris",
        "sep-24",
        "sep24",
        "sep-31",
        "sep31",
    ],
    include_package_data=True,
    package_dir={"": "polaris"},
    packages=find_packages("polaris"),
    install_requires=[
        "aiohttp==3.6.3",
        "aiohttp-sse-client==0.1.7",
        "async-timeout==3.0.1",
        "attrs==20.2.0",
        "certifi==2020.6.20",
        "cffi==1.14.3",
        "chardet==3.0.4",
        "crc16==0.1.1",
        "cryptography==3.1.1",
        "django==2.2.16",
        "django-cors-headers==3.5.0",
        "django-environ==0.4.5",
        "django-model-utils==4.0.0",
        "djangorestframework==3.12.1",
        "idna==2.10",
        "mnemonic==0.19",
        "multidict==4.7.6",
        "psycopg2-binary==2.8.6",
        "pycparser==2.20",
        "pyjwt==1.7.1",
        "pynacl==1.3.0",
        "pytz==2020.1",
        "requests==2.24.0",
        "six==1.15.0",
        "sqlparse==0.4.1",
        "stellar-base-sseclient==0.0.21",
        "stellar-sdk==2.8.1",
        "toml==0.10.1",
        "typing-extensions==3.7.4.3; python_version < '3.8'",
        "urllib3==1.25.10",
        "whitenoise==5.2.0",
        "yarl==1.5.1",
    ],
    python_requires=">=3.7",
)
