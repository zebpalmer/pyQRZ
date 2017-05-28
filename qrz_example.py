from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from qrz import QRZ


def print_keys(key_names, query_result):
    """
    Prints results and does not throw exception on queries
    like W1AW where fname key does not exist
    """
    info = ""
    for key_name in key_names:
        if key_name in query_result:
            info += query_result[key_name] + " "
    print(info)


if __name__ == '__main__':
    qrz = QRZ('./settings.cfg')
    result = qrz.callsign("w7atc")
    print_keys(['fname', 'name'], result)
    print_keys(['addr2', 'state'], result)
    print_keys(['country'], result)
    # Show all the data available from QRZ.com
    print('-' * 50)
    for dict_key, dict_value in sorted(result.items()):
        print(u'{0}: {1}'.format(dict_key, dict_value))
