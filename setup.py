from setuptools import setup, find_packages

CLASSIFIERS = [
    # Beta status until 1.0 is released
    "Development Status :: 4 - Beta",

    # Who and what the project is for
    "Intended Audience :: Developers",
    "Topic :: Communications",
    "Topic :: Internet",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Software Development :: Libraries",
    "Topic :: Text Processing :: Markup :: XML",

    # License classifiers
    "License :: OSI Approved :: MIT License",
    "License :: DFSG approved",
    "License :: OSI Approved",

    # Generally, we support the following.
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Framework :: Django",

    # Specifically, we support the following releases.
    "Programming Language :: Python :: 2.7",
    "Framework :: Django :: 1.9",
]

setup(
    name='django-ddp-chat',
    version='0.2.0',
    description='Django DDP Chat',
    long_description=open('README.rst').read(),
    author='Tyson Clugg',
    author_email='tyson@clugg.net',
    url='https://github.com/tysonclugg/django-ddp-chat',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='ddc.tests',
    install_requires=[
        'django-ddp',
        'django',
    ],
    scripts=[
        'dddp_chat/manage.py',
    ],
    tests_require=['requests'],
    classifiers=CLASSIFIERS,
)
