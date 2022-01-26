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

