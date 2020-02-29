from typing import Dict, List
from pathlib import Path
from datetime import datetime
import shutil
import subprocess as sp

from .fsutil import empty_tree
from .fsutil import copy_cover_tree

def passed(fun):
  def wrapper(fun):
    '''Do nothing'''
    return None
  return wrapper

class Deployer:
  def __init__(self, config:Dict=None, src_dir:str=""):
    self.src_dir = Path(src_dir)
    self.deploy_dir = self.src_dir/Path(".deploy_git")
    self.config = config

  def deploy(self):
    self.init_state()
    self.gen_website()
    self.makesure_deploy_dir_exists()
    self.fetch_deploy_dir()
    self.copy_website()
    self.force_push()
    self.init_state()

  @passed
  def init_state(self):
    print('='*20, " cleanup ", '='*20)
    if self.deploy_dir.exists():
      print(f'remove: {self.deploy_dir}')
      shutil.rmtree(self.deploy_dir)


  # @passed
  def gen_website(self):
    build_cfg = self.config.get('build-config', "")
    build_cmd = f'hugo {build_cfg}'.split()
    sp.run(build_cmd, cwd=self.src_dir)

  # @passed
  def makesure_deploy_dir_exists(self):
    if not self.deploy_dir.exists():
      self.deploy_dir.mkdir(exist_ok=True)
      self.setup()

  # @passed
  def setup(self):
    '''Setup git repository'''
    username = self.config.get("name", "unknown")
    email = self.config.get("email", "unknown@haha.com")
    def split(s:str)->List[str]:
      return s.split()

    placeholder = (self.deploy_dir / "placeholder")
    placeholder.touch()
    cmd_flow = [
      split('git init'),
      split('git config user.name')+ [username],
      split('git config user.email')+[email],
      split('git add -A'),
      split('git commit -m')+['first commit']
    ]
    for cmd in cmd_flow:
      sp.run( cmd, cwd=self.deploy_dir)

  @passed
  def fetch_deploy_dir(self):
    pass

  # @passed
  def copy_website(self):
    '''copy with ignore pattern'''
    # clear depoly_folder
    empty_tree(self.deploy_dir)

    # copy the entire website into deploy folder
    copy_cover_tree(self.src_dir/'public', self.deploy_dir)
    pass

  # @passed
  def force_push(self):
    '''force update target repo'''
    repo_url = self.config.get('repo','default')
    branch = self.config.get('branch','default')
    msg = self.config.get('message','')

    print(f'url:{repo_url}, b:{branch}, msg:{msg}')
    def split(s:str)->List[str]:
      return s.split()

    now = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    optional_str = f'{msg} @' if len(msg) > 0 else ''
    commit_msg = f":robot: {optional_str} {now}"

    cmd_flow = [
      # add
      split("git add -A"),
      split("git commit -m ") + [commit_msg],
      # force update
      split(f"git push -u {repo_url} HEAD:{branch} --force")
    ]
    for cmd in cmd_flow:
      sp.run(cmd, cwd=self.deploy_dir)
