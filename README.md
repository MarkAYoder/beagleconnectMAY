# BeagleConnect Freedom

Currently the BeagleConnect can be configured in one of three ways:
1. A gateway
2. A sensor test
3. A greybus/mikrobus connector


## Reading sensors
The easest way to read the sensors is to flash one BCF as the gateway and another
as the sensor test.  Follow the instrutions 
[here](https://github.com/beagleboard/beagleconnect#flash-beagleconnect-freedom-gateway-device)
to flash the gateway.

## Flashing the sensor test
This is much the same at flashing the gateway.  

Do this from the BeagleBone® Green Gateway board that was previously used to program the BeagleConnect™ Freedom gateway device:

1. Disconnect the BeagleConnect™ Freedom **gateway** device
2. Connect a new BeagleConnect™ Freedom board via USB
3. Run on the bone: `cc2538-bsl.py /usr/share/beagleconnect/cc1352/gsensortest_beagleconnect.bin /dev/ttyACM0`
4. After it finishes programming successfully, disconnect the BeagleConnect Freedom node device
5. Power the newly programmed BeagleConnect Freedom node device from an alternate USB power source
6. Reconnect the BeagleConnect Freedom **gateway** device to the BeagleBone Green Gateway
7. Run: `./sensorPlay.py`  After a minute or so you will see:

```python
('fe80::1510:7a22:4b:1200', 59451, 0, 7)  b'1l:477.92;'
477.92
('fe80::1510:7a22:4b:1200', 59451, 0, 7)  b'3h:26.84;3t:0.70;'
26.84
0.7
```
The `477.92` is the brightness, the `26.84` is the humidity and `0.7` is the temperature in C (It's a cold morning here). 

If you wait longer more reading will appear.  If you don't want to wait so long, press the button the the sensor board that is nearest to the LEDs.
This will cause it to take a reading.

## Plotting data
You can send the sensor data to a Google Sheet using `sensorPlot.py`.  Do this by:
1. Run `./install.sh`   This will take several minutes while your bone installs the needed Python libraries.
2. Open (https://docs.google.com/spreadsheets) and start a new spreadsheet.
3. Copy the sheet ID from the URL of the sheet.  https://docs.google.com/spreadsheets/d/**194-6E4KGiKREfnmcSQmCroe3n_E5PvAD2LBzfRVB64I**/edit#gid=0  The sheet ID is the stuff between the **'s.
4. Edit `sensorPlot.py` and replace the SAMPLE_SPREADSHEET_ID on line 31 with your ID.
5. Run: `./sensorPlot.py`  After a few seconds it will print something like:

```
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=834314057708-q7dsgi6i0eeef4ap6gh3d6k2qu64g5k5.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fspreadsheets&state=r2JjhaxsmbsfB0D08svWfguL5tLMSz&prompt=consent&access_type=offline&code_challenge=5t1z76h66pGC9lSjWYrr_VwU1q6y_sBmcsOGRVECDOc&code_challenge_method=S256
Enter the authorization code:
```
6. Paste the text into the browser on your host computer and follow the instructions.  
7. After a few seconds your data should be plotting on the sheet.

