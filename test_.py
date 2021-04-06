import pytest
import hashlib
import json
from testbook import testbook


@pytest.fixture(scope='module')
def tb():
  with testbook('hw0.ipynb', execute=True) as tb:
    yield tb

    
def test_step_1(tb):
  
  try:
    complete = None
    complete = tb.ref('STEP_1_COMPLETE').resolve()
  except:
    # STEP_1_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 1: not complete.'
    
  try:
    df = str(tb.ref('df')).encode('utf-8')
  except:
    assert False, 'STEP 1: df does not exist. Confirm that you have named your variable correctly.'

  assert hashlib.md5(df).hexdigest() == '530e2e766ef6397f107ccddcf423c58e', \
  'STEP 1: The dataframe df does not match the housing.csv data. Be sure you are importing the correct file from the correct site.'
    
    
def test_step_2(tb):
  try:
    complete = None
    complete = tb.ref('STEP_2_COMPLETE').resolve()
  except:
    # STEP_2_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 2: not complete.'
    
    
def test_step_3(tb):
  try:
    complete = None
    complete = tb.ref('STEP_3_COMPLETE').resolve()
  except:
    # STEP_3_COMPLETE constant has been removed, set to true
    complete = True
  finally:
    assert complete, 'STEP 3: not complete.'
