import tkinter as tk
import tkinter.font
from random import randint
from threading import Thread
import time
import smtplib
from email.message import EmailMessage
import RPi.GPIO as GPIO # only will work on a Raspberry Pi System


class DoorLockSystem(tk.Tk):
	def __init__(self):
		self.tk = tk.Tk()
		self.tk.title("Security Door Lock")
		self.tk.attributes('-fullscreen', True)
		self.state = True
		self.tk.bind("<F1>", self.toggle_fullscreen)
		self.tk.bind("<Escape>", self.end_fullscreen)
		self.password = ""
		self.input_digits = ""
		self.attempts = 1
		self.tk.config(cursor="none")

		thread = Thread(target=self.change_passcode)
		thread.start()
		
		#sets up the GPIO pin
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18, GPIO.OUT) # 18 is the pin I used
		
		self.create_widgets()

	def create_widgets(self):
		self.entry_label = tk.Label(self, text="Enter Passcode")
		FontType = tkinter.font.Font(family = "Helvetica")
		self.entry_label.configure(font = FontType)
		self.entry_label.pack(pady=10)

		self.entry_var = tk.StringVar()
		self.entry = tk.Entry(self, textvariable=self.entry_var, font=("Arial", 20), justify="center", state="readonly")
		FontType = tkinter.font.Font(family = "Helvetica")
		self.entry.configure(font = FontType)
		self.entry.pack(pady=10)

		self.keypad_frame = tk.Frame(self)
		self.keypad_frame.pack()

		keypad_buttons = [
			('1', '2', '3'),
			('4', '5', '6'),
			('7', '8', '9'),
			('', '0', '←')
		]

		for i, row in enumerate(keypad_buttons):
			for j, text in enumerate(row):
				btn = tk.Button(self.keypad_frame, text=text, width=5, height=2, command=lambda t=text: self.on_keypress(t))
				FontType = tkinter.font.Font(family = "Helvetica")
				btn.configure(font = FontType)
				btn.grid(row=i, column=j, padx=5, pady=5)

	def on_keypress(self, value):
		if value == "←":
			self.input_digits = self.input_digits[:-1]
		elif len(self.input_digits) < 8:
			self.input_digits += value

		self.update_entry()
	
	def disable_keypad_buttons(self):
		for btn in self.keypad_frame.winfo_children():
			btn["state"] = "disabled"

	def enable_keypad_buttons(self):
		for btn in self.keypad_frame.winfo_children():
			btn["state"] = "normal"

	def update_entry(self):
		self.entry_var.set(self.input_digits)

		if len(self.input_digits) == 8:
			if self.input_digits == self.password:
				self.show_success_button()

			else:
				if self.attempts <= 2:
					self.attempts += 1
					self.reset_input()
					self.entry_var.set('Incorrect')
				else:
					self.attempts += 1
					self.reset_input()
					thread2 = Thread(target=self.lock_keypad)
					thread2.start()

	def show_success_button(self):
		self.entry_var.set("Access Granted")
		self.entry.config(state="disabled")
		GPIO.output(18,0) # activates solenoid
		self.disable_keypad_buttons()
		self.success_button = tk.Button(self, text="Engage Lock", command=self.reset_input, width=13, height=2)
		self.success_button.pack(pady=20)
		FontType = tkinter.font.Font(family = "Helvetica")
		self.success_button.configure(font = FontType)
		

	def reset_input(self):
		self.entry_var.set("")
		self.input_digits = ""
		self.entry.config(state="normal")
		GPIO.output(18,1) # turns solenoid off (the magnet no longer pulls the solenoid out of the door's way)
		self.enable_keypad_buttons()

		if hasattr(self, 'success_button'):
			self.success_button.pack_forget()
			del self.success_button

	def toggle_fullscreen(self):
		self.state = not self.state  # Just toggling boolean
		self.tk.attributes("-fullscreen", self.state)
		return "break"

	def end_fullscreen(self):
		self.state = False
		self.tk.attributes("-fullscreen", False)
		return "break"
	
	def change_passcode(self): 
		while True:
			for x in range(0,8):
				self.password += str(randint(0,9))
			thread2 = Thread(target=self.email_send("Security System Lock", f"Passcode Valid for 24 hours: {self.password}"))
			thread2.start()
			time.sleep(86400) # 24 hr = 86,400 seconds
			self.password = ""
			self.attempts = 0
			
	def lock_keypad(self):
		self.entry.config(state="disabled")
		self.entry_var.set('Cooldown')
		self.disable_keypad_buttons()
		time.sleep(0.5)

		sec = 30
		for i in range(30):
			self.entry_var.set(f'{sec} seconds left')
			time.sleep(1)
			sec -= 1
		self.reset_input()
		self.entry_var.set('')

	def email_send(self, subject, body):

		EMAIL_ADDRESS = 'abcdefgh@gmail.com' #  Email Address which will be sending the password
		APP_CODE = 'abcd efgh ijkl' # App Password (the formatting should look similar to this but different letters. Don't share it with anyone)

		msg = EmailMessage()
		msg['Subject'] = subject
		msg['From'] = EMAIL_ADDRESS
		msg['To'] = ['kobe@gmail.com', 'michael@gmail.com', 'james@gmail.com'] # email addresses for who will be receiving the email with the lock's passcode
		msg.set_content(body)


		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(EMAIL_ADDRESS, APP_CODE)
			smtp.send_message(msg)



if __name__ == '__main__':
	app = DoorLockSystem()
	app.mainloop()