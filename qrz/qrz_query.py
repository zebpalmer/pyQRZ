#!/usr/bin/env python
#coding:utf-8

import os
import requests
import re
import time
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
            self._session_key = regex.search(r.content.decode("utf-8").group(1)
            if self._session_key is not None:
                return True
        raise Exception("Could not get QRZ session")


    def callsign(self, callsign):
        raw_xml = ''
        if 'cache' in self._cfg.__dict__:
            xml_cache = self._cfg.cache['cache-path']
            if xml_cache != '':
                xml_filename = os.path.join(xml_cache, callsign + '.xml')
                if os.path.isfile(xml_filename):
                    # Cache expires time is file's modification datetime + time allowed for file cache
                    #                                                      secs*mins*hours*days
                    cache_expiry_time = os.path.getmtime(xml_filename) + (60*60*24*int(self._cfg.cache['cache-expires']))
                    if cache_expiry_time > time.time():
                        with open(xml_filename) as xml_file:
                            raw_xml = "".join(xml_file.readlines())
                    else:
                        os.remove(xml_filename)                
        if raw_xml == '':
            if self._session_key is None:
                self._get_session()
            url = """http://xmldata.qrz.com/xml/current/?s={0}&callsign={1}""".format(self._session_key, callsign)
            r = self._session.get(url)
            if r.status_code != 200:
                raise Exception("Error Querying")
            if xml_cache != '':
                if not os.path.isdir(xml_cache):
                    os.mkdir(xml_cache)
                if r.content.decode("utf-8").find('<Callsign>') > -1:
                    with open(xml_filename, 'w') as xml_file:
                        xml_file.writelines(r.content.decode("utf-8")
            raw_xml = r.content.decode("utf-8")
                
        raw_dict = xmltodict.parse(raw_xml)
        calldict = {}
        if raw_dict['QRZDatabase'].has_key('Callsign'):
            for key in raw_dict['QRZDatabase']['Callsign'].keys():
                calldict[key] = raw_dict['QRZDatabase']['Callsign'][key]
        return calldict
