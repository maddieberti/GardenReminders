#GardenReminders zone 7a. This application sends desktop notifications
#for commonly cultivated plants in hardiness zone 7a.
#reminders include when to sow, start, transplant, harvest, prune, and
#fertilize, based on the earliest likely date one should perform those
#tasks in zone 7a.

import tkinter as tk
from tkinter import ttk
from datetime import date, datetime
from plyer import notification
import pickle
import os
from playsound3 import playsound
import PyInstaller

root =  tk.Tk()
#Set the title displayed on the window
root.title("Zone 7a Garden Reminders")
#Set the default size of the window, as well as the layout
root.geometry("1200x600")
root.configure(bg="#4A5D23")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

#get home directory (application kept creating new folders when I changed my working directory)
home_dir = os.path.expanduser("~")

#define folder for app data
app_data_folder = os.path.join(home_dir, ".garden_reminders")
#if folder doesn't already exist
if not os.path.exists(app_data_folder):
    #make a folder for the application data
    os.makedirs(app_data_folder)
#define path to the app save data file
DATA_FILE = os.path.join(app_data_folder, 'garden_data.pkl')

#Did not get a sound with the regular plyer notification, so added playsound3 to make it more noticeable
#when a notification comes up in the user desktop.
#find where Python script is running(avoid lookig for the sound in the wrong place)
script_folder = os.path.dirname(os.path.abspath(__file__))
#define path to the sound files (notification and startup, respectively)
notification_sound_path = os.path.join(script_folder, 'sounds', 'leaves_notification_sound.mp3')
startup_sound_path = os.path.join(script_folder, 'sounds', 'startup_bubble_sound.mp3')

#play startup sound
playsound(startup_sound_path)

#List of plants
plants = ["Test", "Potatoes", "Garlic", "Tomatoes", "Peppers", "Cilantro", "Carrots", "Cucumber", "Broccoli", "Blackberries"]
#Frame/container for selecting plants
plant_frame = tk.LabelFrame(root, text="Select Plants to Grow", padx=10, pady=10)
plant_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# responsiveness feature for frame
plant_frame.grid_rowconfigure(0, weight=1)
plant_frame.grid_columnconfigure(0, weight=1)

#Dictionary that holds bool state of check boxes/selection status of plants
plant_vars = {}

#loop to make checkboxes for every plant
for i, plant in enumerate(plants):
    var = tk.BooleanVar() #track the state of each checkbox
    checkbox = tk.Checkbutton(plant_frame, text=plant, variable=var)
    #position checkboxes
    checkbox.grid(row=i, column=0, sticky='w', padx=5, pady=5)
    #set weight for checkboxes so that they separate equally when the window is resized.
    plant_frame.grid_rowconfigure(i, weight=1)
    #store name/status of plant in the dictionary
    plant_vars[plant] = var

#Container for more plant info such as timelines, harvest dates etc. 9/11 added sticky param and

timeline_frame = tk.LabelFrame(root, text="Planting Timelines", padx=5, pady=5)
timeline_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
# make timeline frame fit to varied window sizes
timeline_frame.grid_rowconfigure(0, weight=1)
timeline_frame.grid_columnconfigure(0, weight=1)

# add a treeview widget and define the headings for each process
timeline_tree = ttk.Treeview(timeline_frame, columns=("Plant", "Start", "Sow", "Transplant", "Harvest", "Fertilize", "Prune"), show="headings")
timeline_tree.grid(row=0, column=0, sticky="nsew")

#headings
timeline_tree.heading("Plant", text="Plant Name")
timeline_tree.heading("Start", text="Start Indoors")
timeline_tree.heading("Sow", text="Sow")
timeline_tree.heading("Transplant", text="Transplant")
timeline_tree.heading("Harvest", text="Harvest")
timeline_tree.heading("Fertilize", text="Fertilize")
timeline_tree.heading("Prune", text="Prune")

#define plant data for each plant
# month, day format for dates
# order: plant name, start indoors, sow, transplant, harvest, fertilize, prune
plant_data = [
    ("Test", "January 24", "September 18", "September 19", "September 20", "September 21", "September 22"),
    ("Tomatoes", "February 15", "April 1", "April 15", "July 1", None, None),
    ("Potatoes", None, "January 20", None, "June 15", None, None),
    ("Garlic", None, "September 1", None, "July 15", None, None),
    ("Broccoli", "February 10", "March 15", "April 1", "May 20", None, None),
    ("Peppers", "February 20", "April 5", "May 1", "July 30", None, None),
    ("Cilantro", None, "April 1", None, "June 10", None, None),
    ("Carrots", None, "March 10", None, "June 30", None, None),
    ("Cucumber", "March 5", "April 10", "May 15", "August 1", None, None),
    ("Blackberries", None, "February 20", None, "June 25", "February 15", "February 15")
]
#function to format the dates in the treeview
def parse_date(date_str):
    """Parse a date string in 'Month Day' format into a datetime object."""
    if isinstance(date_str, str):
        try:
            return datetime.strptime(date_str, "%B %d").date()
        except ValueError:
            return None
    return None

#helper to format a single date
def format_date(date_obj):
    """Format a datetime object as 'Month Day'."""
    if date_obj:
        return date_obj.strftime("%B %d")
    return ""

#format the dates so they appear correctly in the treeview
def format_dates(data):
    """Format date strings in the plant data while preserving non-date values."""
    #declare a list for all of the reformatted plant data
    formatted_data = []
    #loop through all plants in data (plant_data will be passed)
    for plant, *dates in data:
        #declare a list for the formatted dates for each plant
        formatted_dates = []
        #loop through all of the dates in data
        for d in dates:
            # if the date is a string, call parse_date to format it.
            if isinstance(d, str):
                parsed_date = parse_date(d)
                #add parsed, formatted date to formatted_dates, preserve the original string if it doesn't translate to a date.
                formatted_dates.append(format_date(parsed_date) if parsed_date else d)
            else:
                formatted_dates.append(d)
        #combine formatted dates for each plant by appending to formatted_data
        formatted_data.append((plant, *formatted_dates))
    return formatted_data


#populate plant data into treeview widget
# updated statements to show formatted dates
formatted_plant_data = format_dates(plant_data)
for item in formatted_plant_data:
    timeline_tree.insert("", "end", values=item)
# for each column, stretch it to fit the window
for col in timeline_tree["columns"]:
    timeline_tree.column(col, width=100, anchor="center", stretch=True)

#task list frame
task_frame = tk.LabelFrame(root, text="Gardening To-Do List", padx=10, pady=10)
task_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
#set the task list to expand
task_frame.grid_rowconfigure(1, weight=1)
task_frame.grid_columnconfigure(0, weight=1)

#listbox widget for the Task frame. extended param so that multiple can be selected
task_listbox = tk.Listbox(task_frame, selectmode="extended", height=10)
task_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

#function to save data using pickle
def save_data():
    """Saves the state of the selected plants and to-do list tasks to a file."""
    data = {
        "selected_plants": {plant: var.get() for plant, var in plant_vars.items()},
        "tasks": task_listbox.get(0, tk.END)
    }
    with open(DATA_FILE, 'wb') as file:
        pickle.dump(data, file)

#function to load data
def load_data():
    """Loads the state of the selected plants and to-do list tasks from a file."""
    #if path with save data exists:
    if os.path.exists(DATA_FILE):
        #open and load the data with pickle
        with open(DATA_FILE, 'rb') as file:
            data = pickle.load(file)
            # Restore plant selections
            for plant, selected in data["selected_plants"].items():
                if plant in plant_vars:
                    plant_vars[plant].set(selected)
            #clear tasks before loading(otherwise duplicates appear)
            task_listbox.delete(0, tk.END)
            # Restore tasks in the to-do list
            for task in data["tasks"]:
                task_listbox.insert(tk.END, task)




# function to check for tasks due today
def check_tasks():
    """Checks which tasks are currently due. For all plants selected by the user,
    check_tasks will compare today's date with the dates of the action items contained within the plant
    data, then add any tasks that are due today to the task list if those tasks aren't already on it."""
    today = date.today()
    today_formatted = (today.month, today.day)
    #create a set of tasks currently in the listbox
    tasks_due = set(task_listbox.get(0, tk.END))
    # for each date and each plant in plant_data
    for plant, *dates in plant_data:
        #if checkbutton for plant is selected
        if plant_vars[plant].get():
            #check every task name and task date(if there is one) to see if any of the dates match today
            for task_name, task_date in zip(("Start Indoors", "Sow", "Transplant", "Harvest", "Fertilize", "Prune"), dates):
                # convert task_date from string to tuple if it's a string
                if isinstance(task_date, str):
                    try:
                        task_date_obj = parse_date(task_date)
                        if task_date_obj and (task_date_obj.month, task_date_obj.day) == today_formatted:
                            task_str = f"{plant} - {task_name}"
                            #if the task isn't already in task list
                            if task_str not in tasks_due:
                                #add the task to the task list
                                task_listbox.insert(tk.END, task_str)
                                tasks_due.add(task_str)
                                #notify the user that a task has been added
                                notify_user(task_str)
                                #save the task list
                                save_data()
                    except ValueError:
                        continue

#function to notify the user
def notify_user(task_str):
    notification.notify(
        title='Garden Reminder',
        message=f'Time to do: {task_str}',
        app_name='Garden Reminders',
        timeout=1  # Notification duration
    )
    playsound(notification_sound_path)

# Function to remove selected tasks from the listbox
def remove_completed_tasks():
    """Removes selected tasks from the task listbox. Select the task you would like to remove,
    then click Remove Completed Tasks button"""
    #get index of selected task
    selected_tasks = task_listbox.curselection()
    #remove tasks from end first (avoids index shifting)
    for index in reversed(selected_tasks):
        task_listbox.delete(index)
    #save the updated task list
    save_data()

#add teh Remove Completed Tasks button (calls remove_completed_tasks when clicked)
remove_button = tk.Button(task_frame, text="Remove Completed Tasks", command=remove_completed_tasks)
remove_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# function to check tasks. run check_tasks every hour and when new plant is selected
def schedule_task_check():
    """Schedule check_tasks to run every hour, and when plants are
    selected or deselected by the user."""
    check_tasks()
    #add a trace for every checkbutton in plant_vars using anonymous func ignore trace_add arguments, that way it can call check_tasks when changes occur
    for plant, var in plant_vars.items():
        var.trace_add("write", lambda *args: check_tasks())
    #recurring timer set to call schedule_task_check every hour using tkinter after method
    root.after(1000 * 60 * 60, schedule_task_check)

#call schedule_task_check upon running to check for tasks due today and then check again every hour
schedule_task_check()

load_data()

root.mainloop()
