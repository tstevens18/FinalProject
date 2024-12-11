'''
Author: Trevor Stevens
Date: 12/11/24
Prrogram:  StevensTrevorHealthyHabits.py
Version: 1.0
The program is designed to help users monitor and improve their overall health by tracking daily water intake, exercise routines, calorie consumption, and sleep patterns.
'''
import tkinter as tk  # Importing the tkinter library for GUI creation
from tkinter import ttk, messagebox  # Importing themed widgets and messagebox for user interaction
from PIL import Image, ImageTk  # Importing PIL for image handling

# Global variables to track daily progress for various activities
water_intake = 0           # Water intake (glasses)
exercise_time = 0          # Exercise time (minutes)
calories_consumed = 0      # Calories consumed (kcal)
sleep_hours = 0            # Sleep hours (hours)

def update_progress():
    """
    Update progress bars and labels based on the logged activity values.
    The progress is calculated as a percentage of daily goals.
    """
    # Update progress bar values
    water_progress['value'] = (water_intake / 8) * 100
    exercise_progress['value'] = (exercise_time / 60) * 100
    calories_progress['value'] = (calories_consumed / 2000) * 100
    sleep_progress['value'] = (sleep_hours / 8) * 100

    # Dynamically update progress labels with current values
    water_label_var.set(f"Water Intake: {water_intake}/8 glasses")
    exercise_label_var.set(f"Exercise: {exercise_time}/60 minutes")
    calories_label_var.set(f"Calories: {calories_consumed}/2000 kcal")
    sleep_label_var.set(f"Sleep: {sleep_hours}/8 hours")

def log_activity():
    """
    Open a new window for the user to log an activity.
    The user selects an activity type and enters a numeric value.
    """
    def submit():
        """
        Handles the submission of activity data.
        Validates input and updates the corresponding activity value.
        """
        global water_intake, exercise_time, calories_consumed, sleep_hours
        try:
            # Get activity type and value from user input
            activity = activity_dropdown.get()  # Dropdown selection
            value = int(entry_field.get())      # Convert entry to integer

            # Ensure the entered value is non-negative
            if value < 0:
                raise ValueError("Value cannot be negative.")

            # Update the corresponding global variable based on activity
            if activity == "Water":
                water_intake += value
            elif activity == "Exercise":
                exercise_time += value
            elif activity == "Meal":
                calories_consumed += value
            elif activity == "Sleep":
                sleep_hours += value
            else:
                # Show error if activity type is invalid
                messagebox.showerror("Error", "Invalid activity type")
                return

            # Update progress bars and close the log window
            update_progress()
            log_window.destroy()
        except ValueError:
            # Handle invalid inputs (non-numeric or negative values)
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    # Create a new window for logging activity
    log_window = tk.Toplevel(root)
    log_window.title("Log Activity")  # Window title
    log_window.geometry("400x400")    # Set window size

    # Display image 
    try:
        img2 = Image.open("image2.jpg").resize((150, 150))  # Resize the image
        photo2 = ImageTk.PhotoImage(img2)
        tk.Label(log_window, image=photo2).pack(pady=10)  # Add image to window
        log_window.photo2 = photo2  # Keep reference to avoid garbage collection
    except:
        tk.Label(log_window, text="image2.jpg not found").pack()  # Handle missing image

    # Dropdown menu for selecting activity type
    tk.Label(log_window, text="Select Activity").pack(pady=5)
    activity_dropdown = ttk.Combobox(log_window, values=["Water", "Exercise", "Meal", "Sleep"])
    activity_dropdown.pack(pady=5)
    activity_dropdown.current(0)  # Default selection: "Water"

    # Entry field for entering the activity value
    tk.Label(log_window, text="Enter Value").pack(pady=5)
    entry_field = tk.Entry(log_window)
    entry_field.pack(pady=5)

    # Submit button to log the activity
    submit_button = tk.Button(log_window, text="Submit", command=submit)
    submit_button.pack(pady=10)

def exit_app():
    """ Exit the application. """
    root.destroy()

# Main Application Window
root = tk.Tk()
root.title("Tracking Healthy Habits")  # Set window title
root.geometry("500x500")             # Set window size
root.configure(bg="#f0f4f7")        # Set background color

# Title Label for the main window
tk.Label(root, text="Tracking Healthy Habits", font=("Arial", 16, "bold"), bg="#f0f4f7").pack(pady=10)

# Display an image in the main window
try:
    img = Image.open("image1.jpg").resize((100, 100))  # Resize the image
    photo = ImageTk.PhotoImage(img)
    tk.Label(root, image=photo, bg="#f0f4f7").pack()
    root.photo = photo  # Keep reference to avoid garbage collection
except:
    tk.Label(root, text="image1.jpg not found", bg="#f0f4f7").pack()  # Handle missing image

# Progress Labels and Bars (using StringVars for dynamic updates)
water_label_var = tk.StringVar(value="Water Intake: 0/8 glasses")
exercise_label_var = tk.StringVar(value="Exercise: 0/60 minutes")
calories_label_var = tk.StringVar(value="Calories: 0/2000 kcal")
sleep_label_var = tk.StringVar(value="Sleep: 0/8 hours")

def create_progress_section(label_var, max_width=300):
 
# Helper function to create a progress section with a label and progress bar.
 
    frame = tk.Frame(root, bg="#f0f4f7")  # Frame for grouping label and progress bar
    tk.Label(frame, textvariable=label_var, bg="#f0f4f7").pack(anchor="w")  # Label displaying progress
    progress = ttk.Progressbar(frame, length=max_width, mode='determinate')  # Progress bar
    progress.pack(pady=5)  # Add padding
    frame.pack(fill="x", padx=20, pady=5)  # Pack frame into the main window
    return progress

# Create progress sections for each activity
water_progress = create_progress_section(water_label_var)
exercise_progress = create_progress_section(exercise_label_var)
calories_progress = create_progress_section(calories_label_var)
sleep_progress = create_progress_section(sleep_label_var)

# Buttons for user actions
# Button to open the log activity window
tk.Button(root, text="Log Activity", command=log_activity, bg="#4CAF50", fg="white").pack(pady=10)

# Button to exit the application
tk.Button(root, text="Exit", command=exit_app, bg="#f44336", fg="white").pack(pady=5)

# Footer with motivational message
tk.Label(root, text="Stay hydrated! You're on your way to a healthier you!", 
         bg="#f0f4f7", fg="#555").pack(side="bottom", pady=10)

# Start the main GUI event loop
root.mainloop()

