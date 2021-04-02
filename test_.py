import pytest
import hashlib
import json
from testbook import testbook

@pytest.fixture(scope='module')
def tb():
  with testbook('hw0.ipynb', execute=True) as tb:
    yield tb

# sample verify arbitrary var value without displaying target value
def test_df(tb):
  df = tb.ref('df')
  assert hashlib.md5(df.to_records().tobytes()).hexdigest() == '2f231a52e0554ed5b7f5c407ac7262c1'
