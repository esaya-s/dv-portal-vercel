#!/usr/bin/env python3
"""
Setup file for DV Portal Ethiopia Django Application
This is Python's equivalent of package.json
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="dv-portal-ethiopia",
    version="1.0.0",
    author="DV Portal Ethiopia",
    author_email="support@dvportal-ethiopia.com",
    description="Django application for DV-2027 program assistance in Ethiopia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://polocash.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "django-debug-toolbar>=4.2.0",
            "django-extensions>=3.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dv-migrate=migrate_database:main",
            "dv-collectstatic=collect_static:main",
            "dv-createsuperuser=create_admin:main",
            "dv-startbot=start_bot:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)