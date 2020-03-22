## C Implementation of the project

### Hardware connection

Pin-layout (component side up)

[                           RC522                                        ]
[_______________________________________]
   |         |          |           |          |         |         |         |
SDA  SCK  MOSI  MISO  IRQ  GND  RST  3.3V


Connect to Raspberry pin

	pin	GPIO
sda 	24	8		// chip select
sck 	23	11		// clock
mosi 	19	IO		// master out, slave in
miso 	21 	9		// master in, slave out
IRQ	--
gnd 	20
rst 	15	22		// hard reset
3.3V	1


### Software setup on the Raspberry Pi.

Make sure you are on latest versions

1. ```bash 
	sudo apt-get update & sudo apt-get upgrade & raspi-update
   ```

2. Make sure you have SPI  in raspi-config (advanced section)
3. Make sure that Device tree is enabled in raspi config (advanced)

```bash
	cd  /home/pi # (assuming this is your home directory)
```


#### BCM2835 library

Install latest from BCM2835 from :[BCM2835](http://www.airspayce.com/mikem/bcm2835/)

1. ```bash
	wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.50.tar.gz
   ```

2. ```bash
	tar -zxf bcm2835-1.50.tar.gz
   ```

3. ```bash
	cd bcm2835-1.50
   ```

4. ```bash
	./configure
   ```

5. ```bash
	sudo make check
   ```

6. ```bash
	sudo make install
   ```

7. ```bash
	cd  ..
   ```


#### RC522 utility

1. ```bash
	cd rfid-rc522
   ```

2. ```bash
	tar -zxvf rc522-1-6-0.tar.gz
   ```

3. ```bash
	cd rc522
   ```

4. ```bash
	./mc			# compile executable
   ```

5. ```bash
	sudo cp RC522.conf   /etc
   ```

6. ```bash
	sudo chmod 666 /etc/RC522.conf
   ```

7. edit   /etc/RC522.conf 		// if necessary


```bash
	reboot 
```

```bash
	cd rc522
```


Run command as root :  ```bash
				./rc522  -h
                       ```


Note: The software was tested on Jessie Debian version with a Pi2 and Pi3. The GPIO section has not changed with the BCM2836, only the processor.
