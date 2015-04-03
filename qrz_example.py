from qrz import QRZ

if __name__=='__main__':
    qrz = QRZ('./settings.cfg')
    result = qrz.callsign("w7atc")
    print result['fname'], result['name']
    print result['addr2'], result['state']
    print result['country']
    # Show all the data available from QRZ.com
    print '-' * 50
    for dict_key, dict_value in sorted(result.items()):
        print u'{0}: {1}'.format(dict_key, dict_value)
