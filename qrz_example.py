from qrz import QRZ

if __name__=='__main__':
    qrz = QRZ('./settings.cfg')
    result = qrz.callsign("w7atc")
    print result['fname'], result['name']
    print result['addr2'], result['state']
    print result['country']