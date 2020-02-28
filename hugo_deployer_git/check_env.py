import toml
import sys

cfg_filename ='config.toml'
required_fields = [
  'repo',
  'branch',
]

def shout_and_exit(msg):
  print(msg,file=sys.stderr)
  sys.exit(1)

def check_env():
  try:
    with open(cfg_filename, "r") as cfg_toml:
      config = toml.loads(cfg_toml.read())
  except FileNotFoundError as fne:
    shout_and_exit(f"File not found: {cfg_filename}, are you inside hugo website folder?")
  except Exception as e:
    shout_and_exit(e)

  if config.get('deploy',None) is None:
    shout_and_exit(f"There're no [deploy] section inside your {cfg_filename}")

  config= config['deploy']
  lack = [s for s in required_fields if config.get(s,None) is None]
  if len(lack) > 0:
    s = 's' if len(lack)>1 else ''
    lack_str = str(lack) if len(lack)>1 else f'"{lack[0]}"'
    shout_and_exit(f'Error in {cfg_filename}: missing field{s} <{lack_str}> inside your [deploy] block')