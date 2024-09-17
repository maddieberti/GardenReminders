#GardenReminders
import tkinter as tk
from tkinter import ttk
from datetime import date, datetime
from plyer import notification

root =  tk.Tk()
#Set the title displayed on the window
root.title("Garden Reminders")
#Set the default size of the window, as well as the layout
root.geometry("1200x600")
root.configure(bg="#4A5D23")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

#List of plants
plants = ["Test", "Potatoes", "Garlic", "Tomatoes", "Peppers", "Cilantro", "Carrots", "Cucumber", "Broccoli", "Blackberries"]
#Frame/container for selecting plants
plant_frame = tk.LabelFrame(root, text="Select Plants to Grow", padx=10, pady=10)
plant_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# responsiveness feature for frame
plant_frame.grid_rowconfigure(0, weight=1)
plant_frame.grid_columnconfigure(0, weight=1)

#Dictionary that holds state of check boxes/selection status of plants
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
    ("Test", "September 16", None, None, None, None, None),
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
                        #parse the date
                        task_date_obj = parse_date(task_date)
                        task_date_tuple = (task_date_obj.month, task_date_obj.day) if task_date_obj else None
                    except ValueError:
                        task_date_tuple = None
                else:
                    task_date_tuple = None
                #
                if task_date_tuple == today_formatted:
                    # declare a string for the task so we can check if it's already in the list
                    task_str = f"{plant}: {task_name}"
                    #Add the task if it's not already on the list
                    if task_str not in tasks_due:
                        task_listbox.insert(tk.END, task_str)
                        notify_user(task_str)

#function to notify the user
def notify_user(task_str):
    notification.notify(
        title='Garden Reminder',
        message=f'Time to do: {task_str}',
        app_name='Garden Reminders',
        timeout=10  # Notification duration in seconds
    )

# Function to remove selected tasks from the listbox
def remove_completed_tasks():
    """Removes selected tasks from the task listbox. Select the task you would like to remove,
    then click Remove Completed Tasks button"""
    #get index of selected task
    selected_tasks = task_listbox.curselection()
    #remove tasks from end first (avoids index shifting)
    for index in reversed(selected_tasks):
        task_listbox.delete(index)

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

root.mainloop()