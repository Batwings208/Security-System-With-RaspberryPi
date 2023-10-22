# Security-System-With-RaspberryPi
This is a Home Security Project designed as a low-budget option but also upgradeable with ease. It was made over the duration of 1-2 months (due to a lack of parts). The project was created for testing personal abilities and developing knowledge on the interaction between hardware and software. Python 3.9.5 was used for this project, but there is a plan in the future to possibly change to an alternate language for more speed and the ability to add more functionality. The total cost of the entire build was kept under $100. A suggestion I would add for someone doing a similar project is to use a more recent Raspberry Pi, as booting takes a long time, and its capabilities are limited. Initially, I planned to add FaceID (Code Complete), but I felt that would be too much for the Raspberry Pi to handle. I'm currently thinking of options for FaceID. This project should only be used for recreation if you have a good level of knowledge in Python and a couple of libraries like tkinter and time, which are important for the functionality of the program.


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

This project is powered by a Raspberry Pi Model B+ (512MB). Due to a lack of CPU power, the project was redesigned for efficiency and effective power usage in order to avoid overheating. The system's average temperature was approximately 40-42°C while being overclocked at a high level by Raspberry Pi's native overclock tool. While running, the CPU load was kept to a bare minimum of less than 5%. The system should still be considered weak for such a project because increasing functionality would be extremely difficult due to the increased power burden. The Raspberry Pi did not appear to be overheating when touched.

**Two 5V Rely Switch**

The project only needed one relay switch; however, a separate one couldn't be found. It runs on 5V, and only one of the relay switches was used. The temperature of the relay was relatively low and never reached high temperatures. When the relay switch received power, it would make a sound of the LED light turning off, indicating that power is no longer being provided to the relay switch. The relay switch proved to be effective and useful in reaching the goal of minimizing heat and power consumption.

**3.5 inch LCD Screen**

This project used a 3.5-inch LCD screen for the keypad. The 3.5-inch LCD screen was a great size, and the digital buttons were properly spaced and large enough to prevent misclicking. A good starting choice, and the connection with the pins was strong and rigid.

**Fielect DC 12V Pull Type Solenoid Electromagnet**

This is a 5-volt exposed solenoid. The mechanism works in a pull-type form and uses electromagnets. However, this can only pull in the solenoid. When deactivated, there is a spring on top that pushes it out as the solenoid is no longer receiving power and can no longer activate the electromagnets. It's wise to mention that the use of electromagnets makes the process seem almost instant. However, there is the sound of metal hitting against itself when the solenoid deactivates, and the solenoid has a tendency to jump out after deactivation due to the sudden loss of pull. This could be prevented by adding a wood block to prevent the metal piece from falling out but be in reach for the solenoid's electromagnets to pull it up. Overall, the solenoid is pretty solid, a good choice, but I would highly recommend upgrading if this is for locking main doors. If you are planning such and need guidance, I'm here to help.



# How the hardware work and wire configurations?

So focusing first on the raspberry pi, I have a GPIO expansion board as I needed extra pins since I am also connection a 3.5 inch screen. I have 3 wires which are connected to the rb Pi (I suggest using different colors but its up to you). 

A **white wire** connected to the **3.3V DC power pin** which is **pin #1**. 

A **black wire** connected to the **Ground pin(GND)** which is **pin #6**. 

And a **red wire** connected to **P18 or GPIO 18** which is **pin #12**. **Remember**, you may choose different GPIO pins as long as they are the same except for the white wire as its an output pin so you can chose another like P21 or even P8, its up to you. 

From these wires, they are connected to the rely switch. I have two switches, which I do not recommend, so my configurations may differ. 

The **white wire** is connected to the **VCC port**. 

The **black wire** is connected to the **Ground(GND) port**. 

And the **red wire** is connected to the **IN2 port**. On your rely if it is one rely, it would most likely have just be **IN or IN1**. I highly again advise against buying a rely switch with two rely's together.



# Documentation

<h3>create_widgets(self)</h3>
Simply creates the keypad and all the buttons. There is, however, an empty button as I used a loop to create the buttons, so there are three column buttons for each row. The way I made it looks complicated, but if you have a good understanding of 2D lists and how the 'enumerate' method works, you should have minimal difficulty understanding it. The empty button has no features, and it won't be registered by the program when pressed. A delete button was also added by me in case of a misclick, and if one wanted to delete the incorrect number clicked. With this, I added an entry label, which was actually only to show the person the passcode they are typing and also to let them know if their passcode is wrong and how long the cooldown would last.
<br></br>


<h3>on_keypress(self, value)</h3>
This function is very simple; all it does is, whenever a button is pressed on the keypad, this function runs, appending the number pressed by the user to a string, keeping track of each press. Clicking the back arrow button results in the most recent number saved being deleted. Once the keys pressed, which were saved, are over 8, a new function called 'update_entry()' is executed. However, this is run regardless; I added that for my own understanding. The parameter value is the button pressed by the user, which, of course, resets.
<br></br>

<h3>disable_keypad_button(self)</h3>
This function locks all the buttons and makes them unclickable. This only occurs when there is a cooldown or if the passcode entered by the user was correct. This feature was added because there was an issue with the program replicating random buttons over the screen when pressed during cooldown or when the keypad is in an unlocked state.
<br></br>


<h3>enable_keypad_button(self)</h3>
This function does the exact opposite of 'disable_keypad_button()'. It makes all the keypad buttons normal and allows them to be clickable, changing values in the user_input string, which records what the user is typing.
<br></br


<h3>update_entry(self)</h3>
This function, when initially run, changes the entry label to the passcode typed by the user, which changes in real-time. Afterward, the function checks if the passcode typed by the user has a length of 8. If it does, the computer would check against the alternating password (24 hours), and if it's correct, the function 'show_success_button()' will run. However, if it's not correct, the function will check the number of attempts made, and if they are less than 2, an incorrect message will be displayed on the entry label, the attempt will be recorded in a variable, and the passcode string will reset to being empty. If the attempts are above 2, the try will still be recorded in a variable, but this time a thread will run alongside it, and on the thread, a function called 'lock_keypad' will be executed.
<br></br>


<h3>show_success_button(self)</h3>
This function changes the entry label to "access granted," notifying the user that the password is correct. Then, a GPIO pin is turned off to allow the solenoid to take power from its own source, activating it and lifting it up so the door is no longer locked. After this, all the keypads are disabled using the 'disable_keypad_button()' function previously created. Finally, a new button is created to engage the lock back, which, when pressed, will run the 'reset_input()' function.
<br></br>


<h3>reset_input(self)</h3>
This function resets the entry label to empty. It also sets the string for the user-clicked passcode to empty and sets the entry state to normal, making it interchangeable. It also resets the keypad back to its normal state. Additionally, it checks if there is a tkinter button called success button, and if it exists, it simply deletes it.
<br></br>


<h3>toggle_fullscreen(self)</h3>
This is very self-explanatory. It allows toggling between full-screen mode to access the code, which is attached to a keybind.
<br></br>


<h3>end_fullscreen(self)</h3>
This is also quite self-explanatory. It simply exits full-screen mode and prevents it from being engaged.
<br></br>


<h3>change_passcode(self)</h3>
This is a function that runs infinitely until the program is terminated. It starts by generating a random passcode with a length of 8. After that, it opens a thread where it attaches the 'email_send' function with parameters that include the email title and the password in the email body. Then, a 24-hour sleep timer begins, during which this function remains inactive, but only on its thread, as it was activated on a separate thread. After the timer runs out, the 'reset_input()' function will run, and the entry label will be reset.
<br></br>


<h3>lock_keypad(self)</h3>
This function is quite crucial. It sets the entry label to disabled, changes the entry label to display 'cooldown,' and disables the keypad. After that, it runs a loop where every second it displays the time remaining from 30, counting down. This is displayed on the screen in real-time as it runs on its own thread and not on the main thread. Afterward, it runs the 'reset_input()' function.
<br></br>


<h3>email_send(self, subject, body)</h3>
This is a very important piece of code because it's the only way the user can know the passcode. In this part, it establishes a connection to SMTP servers and sends an email using a specific account. In the subject and body of the email, it includes a description of what it is and the actual passcode for the lock. Comments within the code provide further explanation for better understanding.
<br></br>


# Further important Information (if you plan on replicating or want to understand why I did certain things)

<h3>Why are there extra pieces of code?</h3>
You may have noticed extra pieces of code being run in a function, but I added a line that repeats what the function does. This is because sometimes the code would randomly encounter bugs without any apparent reason, disrupting the program's functionality. These issues occurred sporadically, making it difficult to identify a specific cause. Consequently, I created these solutions to rerun actions that could potentially cause problems, and this appeared to resolve all the issues. It's worth mentioning that I have made additional changes at the end that should likely prevent the issue even after removing the extra code. However, since this system is implemented on an actual door in my house, I've chosen to leave it in, just in case.
<br></br>

<h3>Why threads? Why not just run them on the main thread?</h3>
This is a very important question which I suspect many who haven't used tkinter well or maybe new to it may ask. If I didn't use threads for somethings this would result in the screen freezing up as it was running on the main thread and no background tasks could run that could change the screen itself. So I implemented threads for this. This allowed me to make changes to the main thread while on another thread and another added benefit was that I could run certain tasks in the background like creating the passcode and setting a 24 hour timer or sending an email without freezing the screen up. It also allowed me to show the cool-down in real-time as the numbers go down. Without the thread, the program would freeze until the timer was up and nothing would show up till it was over.
<br>

<h3>What GPIO pins should I use?</h3>
Use many GPIO pin you want! There is no instructions on which one to use, it's all up to you. Of course when I say use whatever pin you want I mean for the number pins like GPIO 1 or GPIO 23. For the voltage and GND pins you would have to correspond them with the correct labeled pin.
<br></br>

<h3>Could you use a database with this?</h3>
Of course! My intital plan was to use a database with this project as I was really excited about it but I changed my focus towards something more lighter and won't require too much management. As this project was meant to be low budget but more importantly not too techy and complicated. However if you are planning to add a database to your's some of my ideas for which you could use a database for would be like recording entries, successful entries, incorrect entries, date of entry, cooldown activation, keeping record of email address instead of directly on code and more. These are just my suggestions and if you need my help do hesitate to ask me, I would love to help! And just as a small detail, I use this in my house but for my room door as I always wanted to have some cool spy tech things and this furfills my long-lived wishes 😂.


<br></br>
I hope you guys liked this project and this code. I really spent a lot of time on it and it does make me shed a few tears over this project as I had a blast making it. Even though on some occasions I wanted to either quit or smash my head through my computer. I'll now probably find another project to work on or upgrade it with more tech for people who want a more powerful verson. Till then, see you all!

