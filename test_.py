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
    complete = tb.ref('STEP_1_COMPLETE')
  except:
    
    try: 
      df = tb.ref('df')
    except:
      assert False, 'STEP 1: df does not exist. Confirm that you have named your variable correctly in Step 1'
      
    assert hashlib.md5(df.to_records().tobytes()).hexdigest() == '2f231a52e0554ed5b7f5c407ac7262c1', \
      'STEP 1: The dataframe df does not match the housing.csv data. Be sure you are importing the correct file from the correct site.'
    
  if complete:
    assert complete.resolve(), 'STEP 1: not complete.'
    
def test_step_2(tb):
  try:
    complete = None
    complete = tb.ref('STEP_2_COMPLETE')
  except:
    pass
  
  if complete:
    assert complete.resolve(), 'STEP 2: not complete.'

def test_step_3(tb):
  try:
    complete = None
    complete = tb.ref('STEP_3_COMPLETE')
  except:
    pass
  
  if complete:
    assert complete.resolve(), 'STEP 3: not complete.'
