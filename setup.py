from setuptools import setup, find_packages

setup(
    name='python_test_version',  # Replace 'YourProjectName' with the name of your project
    version='1.3.6',  # The initial release version
    author='Benjamin Chenebault',  # Your name or your organization's name
    author_email='your.email@example.com',  # Your contact email
    description='A short description of your project',  # A brief description of your project
    long_description=open('README.md').read(),  # This will include your README.md as the long description
    long_description_content_type='text/markdown',  # This is important for markdown files
    url='https://github.com/yourusername/yourprojectname',  # The URL to your project's repository
    packages=find_packages(),  # This will automatically find any packages in your project
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',  # Assuming your project is MIT licensed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',  # This specifies that your project is compatible with Python 3.6 up to but not including 3.8
    install_requires=[
        # List your project's dependencies here.
        # For example: 'requests>=2.19.1',
    ],
    extras_require={
        # Optional dependencies that are not required for the main functionality of your project
        # For example: 'dev': ['check-manifest'],
        #               'test': ['coverage'],
    },
    entry_points={
        # If your project includes executable scripts or apps, you can specify them here
        # For example: 'console_scripts': ['yourscript=yourmodule:main_function'],
        'console_scripts': [
            'mycommand=main:main',  # Replace 'yourpackage.main:main' accordingly
        ],
    },
)