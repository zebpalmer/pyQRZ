#!/usr/bin/env python
#coding:utf-8

import os
import requests
import re
import time
import xmltodict
from ConfigParser import SafeConfigParser
from os.path import expanduser

class QRZerror(Exception):
    pass

class CallsignNotFound(Exception):
    pass

class QRZ(object):
    def __init__(self, cfgfile):
        self._cfg = SafeConfigParser()
        self._cfg.read(cfgfile)
        self._session = None
        self._session_key = None

    def _get_session(self):
        username = self._cfg.get('qrz', 'username')
        password = self._cfg.get('qrz', 'password')
        if not username or not password:
            raise Exception("No Username/Password found")

        url = '''https://xmldata.qrz.com/xml/current/?username={0}&password={1}'''.format(username, password)
        self._session = requests.Session()
        self._session.verify = False
        r = self._session.get(url)
        if r.status_code == 200:
            raw_session = xmltodict.parse(r.content)
            self._session_key = raw_session['QRZDatabase']['Session']['Key']
            if self._session_key is not None:
                return True
        raise Exception("Could not get QRZ session")


    def callsign(self, callsign):
        if self._session_key is None:
            self._get_session()
        url = """http://xmldata.qrz.com/xml/current/?s={0}&callsign={1}""".format(self._session_key, callsign)
        r = self._session.get(url)
        if r.status_code != 200:
            raise Exception("Error Querying")
        raw_dict = xmltodict.parse(r.content)
        return raw_dict['QRZDatabase']['Callsign']
