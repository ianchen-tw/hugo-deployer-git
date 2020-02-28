# hugo-deployer-git

Deploy your hugo site with git using one command

Inspired by [hexo-deployer-git](https://github.com/hexojs/hexo-deployer-git).

## Installation

~`pip install hugo-deployer-git`~ (WIP)

## Setup

In your `config.toml`, put in this section

```toml
[deploy]
    # required field
    repo = "<your github page repo>"
    branch =  "master"

    # optional_commit message, default to build time
    message = ""

    name= "testuser"
    email= "test@testtest.com"
    build-config= "--minify"
```

## How to use

In your hugo website folder, use `hugo-deployer-git`.