# Security-System-With-RaspberryPi
This is a Home Security Project. Designed as a low-budget option but also upgradable with ease. Made over the duration of 1-2 months (due to lack of parts). Made for testing personal abilities and developing knowledge on the interaction between hardware and software. Used Python 3.9.5 for this project but planning in the future to possibly change to an alternate language for more speed and be able to add more functionality. The total cost of the entire build was kept under $100. A suggestion I would add for one doing a similar project is to use a more recent Raspberry Pi as booting takes a long time and its capabilites are limited. Initially planned to add FaceID (Code Complete) but I felt that would be too much for the Raspberry Pi to deal with. Currently thinking for options for FaceID.


# Components/Hardware
**Listed Version**

1. Raspberry Pi Model B+ (521MB)
2. Two 5V Rely Switch (only needed/used one)
3. 3.5 inch LCD Screen
4. DC 12V Power Supply (Solenoid)
5. Female Connector (Used for CCTV cameras, etc.)
6. Fielect DV 12V Pull Type Solenoid Electromagnet (open-framed)
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
This project used a 3.5 inch LCD Screen for the keypad. The 3.5 inch LCD screen was a great size and the digital buttons were able to be spaced properly and large enough to prevent misclicking. A good startchoice and the connection with the pins were strong and rigid.

**Fielect DV 12V Pull Type Solenoid Electromagnet**


# How it works (Written Version)




