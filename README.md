## van-tools
Bits of code that run in my converted camper van. Likely to involve security, tracking, and solar charging. In time as I get more sure of what I'm doing this will get more useful.

#### Hardware
- [X] Raspberry pi, powered (from buck converter) and mounted on removable board
- [X] DHT22 (temperature and humidity) inside battery compartment
- [ ] Tilt sensor, currently powered but not coded to log any data
- [ ] Three voltage sensors (resistive dropper) although this need a DAC (pic?) put in place
- [X] 3G dongle with data plan in place
- [X] Modified USB hub to split power and data. Powered by 5A buck converter
- [ ] PIC for lights (in case pi falls over I still want to be able to use lights)
- [ ] PIC for DAC -> I2C in place for voltage sensors
- [ ] ?? Shunt? (to measure draw from the battery without having to use MPPT controller)
- [ ] Another DHT22 somewhere in the van (roof & floor?)
- [ ] Ventilation system for boxed in areas

#### Software
- [X] Web page (cycling.bear.army/van.php) showing a live(ish) climate view
- [ ] 3G Monitoring and remediation where required
- [ ] Some kind of link to Solar MPPT controller
- [ ] Tilt sensor, some code to support this and give me useful data
- [ ] A full inventory / backup of software, currently very 'pet' based build
- [ ] Different modes for the controller, 'maintain' or 'in use', so pi will be more likely to use power for ventilation to stop damp if the van isn't in use. 'in use' should stop that and allow me to manage it manually
