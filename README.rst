==================
pyQRZ
==================

A python module to query QRZ.com's ham radio license database. Supports both python 2.7 and 3.x


NOTE: this is VERY alpha, though working great for call sign lookup, which was what I needed quickly for another project
I'm working on.


Install / Use
-----------------

This package can be installed via pip: "pip install -U pyQRZ"


Once installed, you'll need to create a settings file (see below) and use the path to said file

.. code-block:: python

    # pyQRZ settings
    [qrz]
    username=blah
    password=blahblah



Basic use example:

.. code-block:: python

    qrz = QRZ('./settings.cfg')
    result = qrz.callsign("w7atc")
    print result['fname'], result['name']
    print result['addr2'], result['state']
    print result['country']


ALSO NOTE:
To use QRZ.com's XML API, a subscription is required. But, in my opinion it's the fastest and most complete (world wide)
ham radio license database. If you don't have a QRZ.com subscription or aren't building an application
(logging software) for those that do, this won't be of any use to you.


My project will also incorperate the FCC database (free but USA only) I'll
add that at some point.


