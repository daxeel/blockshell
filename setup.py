from setuptools import setup

setup(
    name="blockshell",
    version='0.1',
    author = "Daxeel Soni",
    author_email = "daxeelsoni44@gmail.com",
    url = "https://daxeel.github.io",
    description = ("A command line utility for learning Blockchain concepts."),
    py_modules=['bscli'],
    install_requires=[
        'Click',
        'colorama',
        'flask'
    ],
    entry_points='''
        [console_scripts]
        blockshell=bscli:cli
    ''',
)
