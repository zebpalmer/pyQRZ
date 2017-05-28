#!/usr/bin/env python
# coding:utf-8

import os
import requests
import xmltodict
from ConfigParser import SafeConfigParser


class QRZerror(Exception):
    pass


class CallsignNotFound(Exception):
    pass


class QRZ(object):
    def __init__(self, cfg=None):
        if cfg:
            self._cfg = SafeConfigParser()
            self._cfg.read(cfg)
        else:
            self._cfg = None
        self._session = None
        self._session_key = None

    def _get_session(self):
        if self._cfg and self._cfg.has_section('qrz'):
            username = self._cfg.get('qrz', 'username')
            password = self._cfg.get('qrz', 'password')
        else:
            username = os.environ.get('QRZ_USER')
            password = os.environ.get('QRZ_PASSWORD')
        if not username or not password:
            raise Exception("No Username/Password found")

        url = '''https://xmldata.qrz.com/xml/current/?username={0}&password={1}'''.format(username, password)
        self._session = requests.Session()
        self._session.verify = False
        r = self._session.get(url)
        if r.status_code == 200:
            raw_session = xmltodict.parse(r.content)
            self._session_key = raw_session['QRZDatabase']['Session']['Key']
            if self._session_key:
                return True
        raise Exception("Could not get QRZ session")

    def callsign(self, callsign, retry=True):
        if self._session_key is None:
            self._get_session()
        url = """http://xmldata.qrz.com/xml/current/?s={0}&callsign={1}""".format(self._session_key, callsign)
        r = self._session.get(url)
        if r.status_code != 200:
            raise Exception("Error Querying: Response code {}".format(r.status_code))
        raw = xmltodict.parse(r.content).get('QRZDatabase')
        if not raw:
            raise QRZerror('Unexpected API Result')
        if raw['Session'].get('Error'):
            errormsg = raw['Session'].get('Error')
            if 'Session Timeout' in errormsg or 'Invalid session key' in errormsg:
                if retry:
                    self._session_key = None
                    self._session = None
                    return self.callsign(callsign, retry=False)
            elif "not found" in errormsg.lower():
                raise CallsignNotFound(errormsg)
            raise QRZerror(raw['Session'].get('Error'))
        else:
            ham = raw.get('Callsign')
            if ham:
                return ham
        raise Exception("Unhandled Error during Query")
