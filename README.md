## van-tools
Bits of code that run in my converted camper van. Likely to involve security, tracking, and solar charging. In time as I get more sure of what I'm doing this will get more useful.

##### Van has:
- Raspberry pi, some flavour of linux
- 3g dongle on three to connect back to home over openvpn
- modified USB hub to split power and data to get 5Amps from a buck converter, for wifi and 3g etc

##### Van will have:
- some kind of connectivity from pi to the bluetooth charge controller to get solar & use metrics
- some kind of current sensor coming from the battery, currently only the (max) 10A from the charge controller can be monitored
- tilt sensors
- temperature and humidity sensors
- PIC controlled lighting
- PIC voltage monitoring, PIC as A/D converter, then over i2c into pi, both house and starter batteries
- Containerised tools and package, in case I want to change linux flavour etc
- Many controllable relays for ventilation / heating, ideally based on charged'ness
- Different modes for the controller, 'maintain' or 'in use', so pi will be more likely to use power for ventilation to stop damp if the van isn't in use. 'in use' should stop that and allow me to manage it manually
- USB ports everywhere, maybe relay controllable so I can see what goes on and where through some kjind of thing (cacti matybe?)
- Something to monitor the openvpn connection and remediate if down (if possible with network limitations)