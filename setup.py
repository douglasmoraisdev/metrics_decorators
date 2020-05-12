import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metrics_decorators",
    version="0.0.1",
    author="Douglas Morais",
    author_email="msantos.douglas@gmail.com",
    description="Decorators to help log metrics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/douglasmoraisdev/metrics_decorators",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	dependency_links=[
        'git+https://github.com/douglasmoraisdev/json_log@master#egg=json_log-0.0.1'
    ]    
)