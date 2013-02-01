==================
pyQRZ
==================

A python module to query QRZ.com's ham radio license database.



I'll be packaging this and posting to pypi in the near future. If you want to use it now though,
clone/download this repo, create a settings.cfg file with qrz user/pass (see settings_example.cfg)
then see qrz_example.py for a use example. You'll also need to install 'xmldict' and 'requests' via pip
if you don't already have them.

At the moment, this is python 2.x only, onced packaged and on pypi, it'll support 3.x as well.

To use QRZ.com's XML API, a subscription is required. But, in my opinion it's the fastest and most complete (world wide)
ham radio license database. I will be releasing another ham radio callsign module (USA only) which will data from the FCC
in the near future.



