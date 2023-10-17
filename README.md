# Security-System-With-RaspberryPi
This is a Home Security Project. Designed as a low-budget option but also upgradable with ease. Made over the duration of 1-2 months (due to lack of parts). Made for testing personal abilities and developing knowledge on the interaction between hardware and software. Used Python 3.9.5 for this project but planning in the future to possibly change to an alternate language for more speed and be able to add more functionality. The total cost of the entire build was kept under $100. A suggestion I would add for one doing a similar project is to use a more recent Raspberry Pi as booting takes a long time and its capabilites are limited. Initially planned to add FaceID (Code Complete) but I felt that would be too much for the Raspberry Pi to deal with. Currently thinking for options for FaceID. And this project should only be used for recreation if you have a good level of knowledge in python and I couple of libraries like tkinter and time which are important for the functionality of the program.


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


# How the code works?

**I have a video in-depth as the code is very long and typing would make this boring and a discouraging project. I will keep the video as short as possible but well explained. I'll also try and add comments to the code for further guidance.**

# Functions/Modules

<h3>create_widgets(self)</h3>
Simply creates the keypad and all the buttons. There is however an empty button as I used a loop to create the buttons so 3 column buttons for each row. They way I made it looks complicated, but if you have a good understanding of 2D lists and how the 'enumerate' method works you should have minimal difficulty understanding it. The empty button has no features, it won't be registered by the program when pressed. A delete button was also added by me incase for a miss click and one wanted to delete the incorrect number clicked. With this I added a entry label which was actual only to show the person the passcode they are typing and also to let them know if their passcode is wrong and how long the cooldown would last.
<br></br>


<h3>on_keypress(self, value)</h3>
This function is very simple, all it does is whenever a button is pressed on the keypad, this function is run which appends the number pressed by the user to a string keeping track of each press. And clicking the back arrow button will result in the most recent number saved to be deleted. And once the keys pressed which were saved are over 8, a new function would be executed called 'update_entry()', however this is ran regardless, I added that for my own understanding. And the parameter value is the button pressed by the user which of course, resets.
<br></br>

<h3>disable_keypad_button(self)</h3>
This function locked all the buttons and makes them unclickable. This only occurs when there is a cooldown or if the passcode entered by the user was correct. This feature was added as there was an issue with the program replicating random buttons over the screen when pressed upon during cooldown or when the keypad is in a unlocked state.
<br></br>


<h3>enable_keypad_button(self)</h3>
This function does the exact opposite of the 'disable_keypad_button()'. It makes all the keypad buttons normal and allows them to be clickable and change values to the user_input string which records what the user is typing.
<br></br


<h3>update_entry(self)</h3>
This function when is ran intially changes the entry label to the passcode typed by the user which changes in real-time. After which the function checks if the passcode typed by the user is the length of 8. If so then the computer would check against the alternating password (24 hours) if it is correct and if so, the function 'show_success_button()' will run. However if not, then the function will check the attempts made and if they are less than 2, an incorrect message would be displayed on the entry label, the attempt will be recorded to a variable and the passcode string would reset back to being empty. But if also the attempts are above 2 then the try will still be recorded to a variable but this time a thread will be ran alongside it which on the thread would run function called 'lock_keypad'.
<br></br>


<h3>show_success_button(self)</h3>
This function changes the entry label to "access granted" notifying the user that the password is correct. And then a GPIO pin is turned off to allow the solenoid to take power from its own source activating it and lifting it up so the door is no longer locked. After which all the keypads are disabled using the 'disable_keypad_button()' function previously made. And finally a new button is created to engage the lock back which is set to when pressed it would run the function 'reset_input()'.
<br></br>


<h3>reset_input(self)</h3>
This function sets the entry label to nothing as a reset way. It also sets the string for the user clicked passcode to nothing and sets the entry state to normal so it's interchangeable. It also resets the keypad back to its normal state. And also checks if there is a tkinter button called success button and it it exists simply delete it.
<br></br>


<h3>toggle_fullscreen(self)</h3>
This is very self-explanatory, this is for being able to toggle between full-screen mode to access the code which is attached to a keybind.
<br></br>


<h3>end_fullscreen(self)</h3>
This is also quite self-explanatory, this simply kills full-screen entirely and prevents it from being engaged.
<br></br>


<h3>change_passcode(self)</h3>
This is a function that will run infinitely till the program is killed. It would start by making a randomly generated passcode with the length of 8. After which it opens a thread where it attachs the email_send function with parameters which are simply the title of the email and the password in the body of the email. After a 24 hour sleep timer begins where this function will remain inactive but only on its thread since it was activated on a separated thread. After the timer has ran out, the reset_input() function will run and the entry label would be reset.
<br></br>


<h3>lock_keypad(self)</h3>
So this function is quite crucial. This function sets the entry label to disabled, changes the entry label to display 'cooldown' and disables the keypad. After which it runs a loop where every sec it displays the time left from 30 counting down. This displays it on the screen in real-time as it runs on its own thread and not on the main thread. After which it runs the function 'reset_input()'.
<br></br>


<h3>email_send(self, subject, body)</h3>
This is a very important piece of code as this is the only way the user can know the passcode. In this part, it makes a connection to SMTP servers and sends an email using a specific account. And in the subject and body it would have the description of what it is and the actual passcode for the lock itself. Comments will help you better understand it.
<br></br>


# Further important Information (if you plan on replicating or want to understand why I did certain things)

<h3>Why are there extra pieces of code?</h3>
You may have noticed extra pieces of code being run in a function but I have added a line which repeats what the function does. This is because sometimes the code would randomly bug out for no reason and disrupt the program's ability to work. This would happen on random occasions so there was no specific reason I could come up with it. Instead I created these solutions to rerun things that could cause issues and it seemed to clear up all the issues. Just to also mention, I have made changes to the at the end which would most likely prevent the issue even after deleting the extra code but since this runs on an actual door in my house I will leave it in. Just incase.
<br></br>

<h3>Why threads? Why not just run them on the main thread?</h3>
This is a very important question which I suspect many who haven't used tkinter well or maybe new to it may ask. If I didn't use threads for somethings this would result in the screen freezing up as it was running on the main thread and no background tasks could run that could change the screen itself. So I implemented threads for this. This allowed me to make changes to the main thread while on another thread and another added benefit was that I could run certain tasks in the background like creating the passcode and setting a 24 hour timer or sending an email without freezing the screen up. It also allowed me to show the cool-down in real-time as the numbers go down. Without the thread, the program would freeze until the timer was up and nothing would show up till it was over.
<br>

<h3>What GPIO pins should I use?</h3>
Use many GPIO pin you want! There is no instructions on which one to use, its all up to you. Of course when I say use whatever pin you want I mean for the number pins like GPIO 1 or GPIO 23. For the voltage and GND pins you would have to correspond them with the correct labeled pin.
<br></br>

<h3>Could you use a database with this?</h3>
Of course! My intital plan was to use a database with this project as I was really excited about it but I changed my focus towards something more lighter and won't require too much management. As this project was meant to be low budget but more importantly not too techy and complicated. However if you are planning to add a database to your's some of my ideas for which you could use a database for would be like recording entries, successful entries, incorrect entries, date of entry, cooldown activation, keeping record of email address instead of directly on code and more. These are just my suggestions and if you need my help do hesitate to ask me, I would love to help! And just as a small detail, I use this in my house but for my room door as I always wanted to have some cool spy tech things and this furfills my long-lived wishes 😂.





I hope you guys liked this project and this code. I really spent a lot of time on it and it does make me shed a few tears over this project as I had a blast making it. Even though on some occasions I wanted to either quit or smash my head through my computer. I'll now probably find another project to work on or upgrade it with more tech for people who want a more powerful verson. Till then, see you all!

