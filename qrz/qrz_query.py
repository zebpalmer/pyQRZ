#!/usr/bin/env python
#coding:utf-8

import sys
import requests
import re
import xmltodict
from ConfigParser import SafeConfigParser

class Settings(object):
    def __init__(self, filename):
        try:
            settings = SafeConfigParser()
            settings.read(filename)
        except Exception, e:
            raise Exception(e)

        try:
            for section in settings.sections():
                temp = {}
                for item in settings.items(section):
                    lines = [x.strip() for x in item[1].split(',')]
                    if len(lines) > 1:
                        temp[item[0]] = lines
                    else:
                        temp[item[0]] = item[1]

                self.__dict__[section] = temp
        except Exception:
            raise Exception('Error in config file')

    def __getattr__(self, name):
        print 'Config Section Not Found'
        return {}


class QRZ(object):
    def __init__(self, cfgfile):
        self._cfg = Settings(cfgfile)
        self._session = None
        self._session_key = None

    def _get_session(self):
        regex = re.compile("<Key>(.*)</Key>")
        url = '''https://xmldata.qrz.com/xml/current/?username={0}&password={1}'''.format(self._cfg.qrz['username'],
                                                                                          self._cfg.qrz['password'])
        self._session = requests.Session()
        self._session.verify = False
        r = self._session.get(url)
        if r.status_code == 200:
            self._session_key = regex.search(r.content).group(1)
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
        raw = xmltodict.parse(r.content)
        calldict = {}
        for key in raw['QRZDatabase']['Callsign'].keys():
            calldict[key] = raw['QRZDatabase']['Callsign'][key]
        return calldict


