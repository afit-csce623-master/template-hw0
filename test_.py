import pytest
import hashlib
import json
from testbook import testbook

assert False, "Update test file and remove sample code"

@pytest.fixture(scope='module')
def tb():
  with testbook('hw.ipynb', execute=True) as tb:
    yield tb

# Sample test code
# Read more at https://github.com/nteract/testbook

# verify notebook exists
def find_notebook(tb):
  assert True

# sample verify var
def test_var(tb):
  var = tb.ref('var')
  assert var == 'foo', 'msg'

# sample verify function
def test_func(tb):
  func = tb.ref('func')
  assert func(1,2) == 3, 'msg'

# sample verify numpy array var value without displaying target value
def test_numpy_var_obscure(tb):
  array_var = tb.ref('var')
  assert hashlib.md5(str(array_var).encode('utf-8')).hexdigest() == '## some hash value ##'

# sample verify string var value without displaying target value
def test_string_var_obscure(tb):
  string_var = tb.ref('var')
  assert hashlib.md5((string_var).encode('utf-8')).hexdigest() == '## some hash value ##'

# sample verify arbitrary var value without displaying target value
def test_json_var_obscure(tb):
  var = tb.ref('var')
  assert hashlib.md5(json.dumps(var).encode('utf-8')).hexdigest() == '## some hash value ##'

