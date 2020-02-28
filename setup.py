from setuptools import setup, find_packages

setup(
    name="hugo-deployer-git",
    version="0.87",
    packages=find_packages(),
    author="Ian Chen",
    author_email="ianre657@gmail.com",
    description="Deploy your hugo site with git using one command",

    entry_points={
      'console_scripts':[
        'hugo-deployer-git=hugo_deployer_git.cli.__main__:main'
      ]
    },
)