"""
Program: videostoreGUI_JR.py
Chapter 8
1/26/2024

**NOTE: the module breezypythonygui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based app that prompts for the number of video rentals in pricing categories. Calculates and displays the grand total.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header (class name will change project to project)
class VideoStore(EasyFrame):

	# Definition of our classes constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Five Star Retro Video", background = "purple4", width = 480, height = 360)

		# Variable to store a font design for multiple labels
		labelFont = Font(family = "Terminal", size = 16)

		# Label and entry field
		self.label = self.addLabel(text = "Five Star Retro Video", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "purple4", foreground = "MediumPurple1", font = Font(family = "Terminal", size = 22))
		self.addLabel(text = "Number of New Rentals ordered", row = 1, column = 0, background = "purple4", foreground = "MediumPurple1", font = labelFont)
		self.newrentalField = self.addIntegerField(value = 0, row = 1, column = 1, width = 10)
		self.addLabel(text = "Number of Old Rentals ordered", row = 2, column = 0, background = "purple4", foreground = "MediumPurple1", font = labelFont)
		self.oldrentalField = self.addIntegerField(value = 0, row = 2, column = 1, width = 10)
		self.newrentalField["background"] = "MediumPurple1"
		self.oldrentalField["background"] = "MediumPurple1"

		# Bind the oldrentalField to the press of the enter key event
		self.oldrentalField.bind("<Return>", lambda event: self.order())

		# Add button
		self.button = self.addButton(text = "Show Total!", row = 3, column = 0, columnspan = 2, command = self.order)
		self.button["background"] = "MediumPurple1"
		self.button["width"] = 15
		self.button["height"] = 2


		# Label for total cost and output field
		self.outputLabel = self.addLabel(text = "", row = 4, column = 0, sticky = "NSEW", columnspan = 2, background = "purple4", foreground = "MediumPurple1", font = labelFont)

	# Definition of the order() function which is the event handler
	def order(self):
		newRentals = self.newrentalField.getNumber()
		oldRentals = self.oldrentalField.getNumber()
		totalCost = (newRentals * 3.50) + (oldRentals * 2)
		self.outputLabel["text"] = "THE TOTAL COST FOR THIS ORDER IS: $%0.2f" % totalCost

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	VideoStore().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()