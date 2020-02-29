import pytest

import tempfile
import os
import shutil

from pathlib import Path

from hugo_deployer_git.fsutil import is_dir
from hugo_deployer_git.fsutil import is_file

@pytest.fixture
def cleandir():
    old_cwd = os.getcwd()
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    yield
    os.chdir(old_cwd)
    shutil.rmtree(newpath)

@pytest.mark.usefixtures("cleandir")
def test_isdir(cleandir):
  # normal folder
  print(f'cwd: {os.getcwd()}')
  b = Path('b')
  b.mkdir()
  assert( is_dir(b) == True )

@pytest.mark.usefixtures("cleandir")
def test_isdir_under_hidden_folder(cleandir):
  # under hidden folder
  root = Path('.git_deploy')

  f = root/Path('testdir')
  f.mkdir(parents=True)
  print(f'f:{f.absolute()}')
  assert( is_dir(f) == True)

  hidden = root/Path('.hidden')
  hidden.mkdir(parents=True)
  assert( is_dir(hidden) == True)

@pytest.mark.usefixtures("cleandir")
def test_isfile_under_hidden_folder(cleandir):
  # under hidden folder
  root = Path('.git_deploy')
  root.mkdir(parents=True)

  Path(root/'.a').touch()
  assert( is_file(root/'.a') == True)

  # strange, why is this True inside testcase?
  # assert( os.path.isfile(root/'.a') == True)