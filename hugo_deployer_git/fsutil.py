import shutil
import os
from pathlib import Path
from typing import List
import stat

def empty_tree(path:str, ignore_list:List[str]=['.git']):
  '''remove all files under a folder'''
  assert( ignore_list is not None)

  target = Path(path)
  rmlist = ( target/f for f in os.listdir(target) if f not in ignore_list)
  for f in rmlist:
    if f.is_file():
      f.unlink()
    elif f.is_dir():
      shutil.rmtree(f)

def copy_cover_tree_unignore(src:str, dst:str):
  copy_cover_tree(src, dst, ignore_list=None)

def is_dir(f:str):
  fpath = Path(f)
  if not fpath.exists():
    raise FileNotFoundError(fpath)

  # its required to use stat because os.is_dir only return True
  # if it is a regular file, but all of our file are place inside
  # an hidden folder, which result in a false negative
  return stat.S_ISDIR(os.stat(fpath).st_mode)

def is_file(f:str):
  fpath = Path(f)
  if not fpath.exists():
    raise FileNotFoundError(fpath)
  # see is_dir for exmplanation
  return stat.S_ISREG(os.stat(fpath).st_mode)


def copy_cover_tree( src:str, dst:str, ignore_list:List[str]=['.git','.deploy_git']):
  '''Copy files under src foler into dst folder'''
  src,dst = Path(src), Path(dst)
  dst.mkdir(exist_ok=True)
  if ignore_list is None:
    ignore_list = []
  ignore_list += src.name

  cover_list = [f for f in os.listdir(src) if f not in ignore_list]
  for f in cover_list:
    source = src/f
    target = dst/f
    # print(f'file :{source.name}: startswith .? {source.name.startswith(".")}')
    if source.name.startswith("."):
      continue
    if is_dir(source):
      # print(f'copy from :{source} to {target}')
      copy_cover_tree_unignore(source, target)
    elif is_file(source):
      shutil.copy(source, target)