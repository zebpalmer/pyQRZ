import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

from qrz import QRZ


VALID_SESSION = """
<?xml version="1.0" ?> 
<QRZDatabase version="1.33">
  <Session>
    <Key>2331uf894c4bd29f3923f3bacf02c532d7bd9</Key> 
    <Count>123</Count> 
    <SubExp>Wed Jan 1 12:34:03 2013</SubExp> 
    <GMTime>Sun Aug 16 03:51:47 2012</GMTime> 
  </Session>
</QRZDatabase>
"""

class test_QRZ(unittest.TestCase):
    # def test_qrz_session(self):
    #     self.assertEqual('2331uf894c4bd29f3923f3bacf02c532d7bd9', session)

    def test_all(self):
        qrz = QRZ('/home/zeb/.qrz.cfg')
        result = qrz.callsign("w7atc")
        self.assertEqual(result['fname'], 'ZEB M')
        self.assertEqual(result['name'], 'PALMER')
        self.assertEqual(result['addr2'], 'Nampa')
        self.assertEqual(result['state'], 'ID')
        self.assertEqual(result['country'], 'United States')
