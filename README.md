# Security-System-With-RaspberryPi
This is a Home Security Project. Designed as a low-budget option but also upgradable with ease. Made over the duration of 1-2 months (due to lack of parts). Made for testing personal abilities and developing knowledge on the interaction between hardware and software. Used Python 3.9.5 for this project but planning in the future to possibly change to an alternate language for more speed and be able to add more functionality. The total cost of the entire build was kept under $100. A suggestion I would add for one doing a similar project is to use a more recent Raspberry Pi as booting takes a long time and its capabilites are limited. Initially planned to add FaceID (Code Complete) but I felt that would be too much for the Raspberry Pi to deal with. Currently thinking for options for FaceID.


# Components/Hardware
**Listed Version**

1. Raspberry Pi Model B+ (521MB)
2. Two 5V Rely Switch (only needed/used one)
3. 3.5 inch LCD Screen
4. DC 12V Power Supply (Solenoid)
5. Female Connector (Used for CCTV cameras, etc.)
6. Fielect DC 12V Pull Type Solenoid Electromagnet (open-framed)
7. Tenda W311m 150 Mbps Mini Wireless USB Adapter
8. GPIO Expansion Board
9. DC 5V Power Supply (Raspberry Pi Model B+)
10. Dupont Cables **MM-MM and FF-FF** (1 MM-MM and 3 FF-FF Used)

<br></br>

**More In-depth Explanation (Only Key Components)**

**Raspberry Pi Model B+ (512MB)**

The project runs on a **Raspberry Pi Model B+ (512MB)**. Due to the lack of power, the project was adjusted for effiency and effective power usage to prevent overheating. The average temperature of the system sat around **40-42 Cº** being overclocked at **high** by RaspberryPi's own overclock tool. The load on the CPU while running stayed at a bare minimum below **5%**. The system should still be deemed weak for such a project as adding functionality would be really difficult as it would add aggressive power load. To touch, the Raspberry Pi didn't feel like it was overheating.

**Two 5V Rely Switch**

The project only needed one rely switch however couldn't find a separate one. Runs on 5V and only one of the rely switch was used. The temperature of the rely was relatively low and never reached high temperatures. And when the rely switch would be recieving power it would make a sound of the LED light turning off indicating power is no longer being provided to the rely switch. The rely switched proved to be effective and useful while reaching the goal of minimizing heat and power drawn.

**3.5 inch LCD Screen**

This project used a 3.5 inch LCD Screen for the keypad. The 3.5 inch LCD screen was a great size and the digital buttons were able to be spaced properly and large enough to prevent misclicking. A good start choice and the connection with the pins were strong and rigid.

**Fielect DC 12V Pull Type Solenoid Electromagnet**

This is a 5 volt exposed solenoid. The mechanism words in a pull type form. And uses electromagnets. However this can only pull in the solenoid. When deactivated there is spring on top which would push it out as the solenoid is no longer receiving power and can not longer activate the electromagnets. Its wise to mention that the use of electromagnets make the process seem almost instant. There is though the sound of metal hitting against itself when the solenoid deactivates. And the solenoid has a tendency to jump out after deactivation due to the sudden loss of pull. This could be prevented by adding a wood block to prevent the metal piece from falling out but be in reach for the solenoid's electromagnets to pull it up. Overall, the solenoid is pretty solid, a good choice but would highly recommend upgrading if this is for locking main doors. If you are planning such and need guidance, I'm here to help. 



# How the hardware work and wire configurations?

So focusing first on the raspberry pi, I have a GPIO expansion board as I needed extra pins since I am also connection a 3.5 inch screen. I have 3 wires which are connected to the rb Pi (I suggest using different colors but its up to you). 

A **white wire** connected to the **3.3V DC power pin** which is **pin #1**. 

A **black wire** connected to the **Ground pin(GND)** which is **pin #6**. 

And a **red wire** connected to **P18 or GPIO 18** which is **pin #12**. **Remember**, you may choose different GPIO pins as long as they are the same except for the white wire as its an output pin so you can chose another like P21 or even P8, its up to you. 

From these wires, they are connected to the rely switch. I have two switches, which I do not recommend, so my configurations may differ. 

The **white wire** is connected to the **VCC port**. 

The **black wire** is connected to the **Ground(GND) port**. 

And the **red wire** is connected to the **IN2 port**. On your rely if it is one rely, it would most likely have just be **IN or IN1**. I highly again advise against buying a rely switch with two rely's together.


# How the code works? (Written Version)

**I have a video in-depth as the code is very long and typing would make this boring and a discouraging project. I will keep the video as short as possible but well explained. I'll also try and add comments to the code for further guidance.**




