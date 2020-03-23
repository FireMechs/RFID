## C++ Implementation of the project

### Getting started 

The sub directory 'RPi-RFID' contains the header files Mofare  RC522  RFID reader. This library uses another library 'bcm' found in the following link [bcm](http://www.airspayce.com/mikem/bcm2835/bcm2835-1.50.tar.gz) . Download the library and install using the following list of commands
```bash
	tar zxvf bcm2835-1.xx.tar.gz

	cd bcm2835-1.xx

	./configure

	make

	sudo make check

	sudo make install
``` 

Any program using thise program is compiled using the following  flag '-lbcm2835' as follows

```bash
	g++ <filename>.cpp -lbcm2835 -std=c++11  -o <outputName> 
```
