# hugo-deployer-git

Deploy your hugo site with git using one command

Inspired by [hexo-deployer-git](https://github.com/hexojs/hexo-deployer-git).

## Installation

`pip3 install hugo-deployer-git`

## Setup

In your `config.toml`, put in this section

```toml
[hugo-deployer-git]
    # required
    repo = "your github page repo"
    branch =  "master"

    # optoinal
    name= "haha"
    email= "test@testtest.com"
    message = ""
    build-config= "--minify"
```

## How to use

In your hugo website folder, use `hugo-deployer-git`.