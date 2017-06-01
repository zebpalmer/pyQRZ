=====
pyQRZ
=====

.. image:: https://travis-ci.org/zebpalmer/pyQRZ.svg?branch=master
    :target: https://travis-ci.org/zebpalmer/pyQRZ

A python module to query QRZ.com's ham radio license database. Tested on python 2.7, 3.4, 3.5, 3.6


Breaking Changes
----------------
When using pyQRZ in a project, please pin pyQRZ to a version that is working with your code. There may be breaking
changes in a soon to be released version.


Install / Use
-------------

This package can be installed via pip: "pip install -U pyQRZ"


Once installed, you'll need to create a settings file (see below) and provide the file path when using QRZ. Alternately,
you may set environment variables "QRZ_USER" and "QRZ_PASSWORD" with appropriate contents.

.. code-block:: python

    # pyQRZ settings
    [qrz]
    username=blah
    password=blahblah



Basic use example:

.. code-block:: python

    qrz = QRZ(cfg='./settings.cfg')
    result = qrz.callsign("w7atc")
    print result['fname'], result['name']
    print result['addr2'], result['state']
    print result['country']


NOTES:
To use QRZ.com's XML API for detailed data, a subscription is required. However, it appears you can get basic
information with a standard QRZ user account. I wouldn't count on that though.

I am thinking about providing a free (and opensourced) callsign lookup service, probably start off as USA only. If
this is of interest to you, feel free to contact me. Knowing it would be useful would make it a higher priority.




