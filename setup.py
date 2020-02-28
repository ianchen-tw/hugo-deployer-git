from setuptools import setup, find_packages

setup(
    name="hugo-deployer-git",
    version="0.87",
    license='MIT',
    url='https://github.com/ianre657/hugo-deployer-git',
    packages=find_packages( exclude="test-site"),
    author="Ian Chen",
    author_email="ianre657@gmail.com",
    description="Deploy your hugo site with github pages using one command",
    keywords= ["hugo", "github pages", "deploy", "git", "blogger", "utility", "static site"],
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Development Status :: 2 - Pre-Alpha",
      "Topic :: Utilities",
    ],
    entry_points={
      'console_scripts':[
        'hugo-deployer-git=hugo_deployer_git.cli.__main__:main'
      ]
    },
)