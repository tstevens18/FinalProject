# FinalProject
User Manual for "Tracking Healthy Habits" Application
________________________________________
1. Introduction
Welcome to the "Tracking Healthy Habits" application! This tool is designed to help you monitor your daily water intake, exercise time, calories consumed, and sleep hours. Track your progress easily with visual progress bars and motivational messages.
________________________________________
2. System Requirements
•	Python Version: Python 3.x
•	Dependencies:
o	tkinter (built-in with Python 3)
o	Pillow for image handling (pip install pillow)
•	Images: Ensure you have the following images in the same folder as the script:
o	image1.jpg for the main window
o	image2.jpg for the log activity window
________________________________________
3. How to Use the Application
3.1 Launching the Application
1.	Save the code to a file (e.g., healthy_tracker.py).
2.	Run the program:
python healthy_tracker.py
3.	The main window will open, displaying the title and four progress bars for:
o	Water Intake
o	Exercise Time
o	Calories Consumed
o	Sleep Hours
________________________________________
3.2 Main Window Features
The main window consists of the following sections:
Progress Bars
Each progress bar tracks an activity:
•	Water Intake: Progress out of 8 glasses
•	Exercise Time: Progress out of 60 minutes
•	Calories Consumed: Progress out of 2000 kcal
•	Sleep Hours: Progress out of 8 hours
The labels above each progress bar update dynamically based on your activity logs.
Buttons
•	Log Activity: Opens a new window to log your activities.
•	Exit: Closes the application.
Motivational Footer
A motivational message is displayed at the bottom to keep you inspired.
________________________________________
3.3 Logging an Activity
1.	Click Log Activity on the main window.
2.	A new window opens with the following options:
o	Activity Selection: Choose from:
	Water (glasses)
	Exercise (minutes)
	Meal (calories)
	Sleep (hours)
o	Value Input: Enter a positive integer for the chosen activity.
3.	Click Submit to log the activity. The progress bars in the main window will update accordingly.
4.	If invalid input (non-numeric or negative value) is entered, an error message will display.
________________________________________
4. Visual Aids
Main Window
•	Displays the progress of all activities.
•	Example layout:
[Progress Bar for Water Intake]
Water Intake: 2/8 glasses
Log Activity Window
•	Allows you to input values for specific activities:
Select Activity:  [Dropdown Menu]
Enter Value:      [Text Box]
[Submit Button]
________________________________________
5. Troubleshooting
Issue	Cause	Solution
"image1.jpg not found"	Image file missing.	Place image1.jpg in the folder.
"Value cannot be negative"	Entered a negative value.	Input only positive numbers.
"Invalid Input" error	Non-numeric input.	Ensure you enter a valid number.
Progress not updating	Activity not submitted.	Confirm submission via "Submit".
________________________________________
6. Exiting the Application
To exit the program:
•	Click the Exit button on the main window.
•	Alternatively, close the window directly.
________________________________________
7. Notes
•	Default daily goals are:
o	8 glasses of water
o	60 minutes of exercise
o	2000 kcal (calories)
o	8 hours of sleep
•	Progress is reset every time the program restarts.
________________________________________
Enjoy tracking your progress and improving your healthy habits!
