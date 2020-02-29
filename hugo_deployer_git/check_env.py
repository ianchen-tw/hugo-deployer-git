import toml
import sys
from colorama import init as colorama_init
from colorama import Fore, Back, Style

colorama_init()
LINK = Fore.BLUE
ERROR = Fore.RED
CLEAR = Style.RESET_ALL

cfg_filename ='config.toml'
required_fields = [
  'repo',
  'branch',
]

usage = f'''
You have to configure the deployment settings in cconfig.toml first!
Example:

[hugo-deployer-git]
    repo = "<your github page url>"
    branch =  "master"
    name= "<your username>"
    email= "test@testtest.com"
    message = ""
    build-config= "--minify"

For more help, you can check the docs: {LINK}https://github.com/ianre657/hugo-deployer-git{CLEAR}
'''

def shout_and_exit(msg):
  print(msg,file=sys.stderr)
  print(usage,file=sys.stderr)
  sys.exit(1)

def check_env():
  try:
    with open(cfg_filename, "r") as cfg_toml:
      config = toml.loads(cfg_toml.read())
  except FileNotFoundError as fne:
    shout_and_exit(f"File not found: {cfg_filename}, are you inside hugo website folder?")
  except Exception as e:
    shout_and_exit(e)

  if config.get('hugo-deployer-git',None) is None:
    shout_and_exit(f"There're no [hugo-deployer-git] section inside your {cfg_filename}")

  config= config['hugo-deployer-git']
  lack = [s for s in required_fields if config.get(s,None) is None]
  if len(lack) > 0:
    s = 's' if len(lack)>1 else ''
    lack_str = str(lack) if len(lack)>1 else f'"{lack[0]}"'
    shout_and_exit(f'Error in {ERROR}{cfg_filename}{CLEAR}: missing field{s} <{lack_str}> inside your [hugo-deployer-git] block')