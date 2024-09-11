#GardenReminders
import tkinter as tk
from tkinter import ttk

root =  tk.Tk()
#Set the title displayed on the window
root.title("Garden Reminders")
#Set the size of the window
root.geometry("1200x600")

#List of plants
plants = ["Potatoes", "Garlic", "Tomatoes", "Peppers", "Cilantro", "Carrots", "Cucumber", "Broccoli", "Blackberries"]
#Frame/container for selecting plants
plant_frame = tk.LabelFrame(root, text="Select Plants to Grow", padx=10, pady=10)
plant_frame.pack(padx=10, pady=10, fill="both")

#Dictionary that holds state of check boxes/selection status of plants
plant_vars = {}

#Loop to make checkboxes for every plant
for plant in plants:
    #variable to track each checkbox state
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(plant_frame, text=plant, variable=var)
    #Position checkboxes to the left of the window
    checkbox.pack(anchor='w')
    #store plant name and selection status in the dictionary
    plant_vars[plant] = var

#Container for more plant info such as timelines, harvest dates etc
timeline_frame = tk.LabelFrame(root, text="Planting Timelines", padx=5, pady=5)
timeline_frame.pack(padx=5, pady=5, fill="both")
# Make timeline frame fit any size window
timeline_frame.grid_rowconfigure(0, weight=1)
timeline_frame.grid_columnconfigure(0, weight=1)

# add a treeview widget and define the headings for each process
timeline_tree = ttk.Treeview(timeline_frame, columns=("Plant", "Start", "Sow", "Transplant", "Harvest", "Fertilize", "Prune"), show="headings")
timeline_tree.pack(fill="both", expand=True)
#headings
timeline_tree.heading("Plant", text="Plant Name")
timeline_tree.heading("Start", text="Start Indoors")
timeline_tree.heading("Sow", text="Sow")
timeline_tree.heading("Transplant", text="Transplant")
timeline_tree.heading("Harvest", text="Harvest")
timeline_tree.heading("Fertilize", text="Fertilize")
timeline_tree.heading("Prune", text="Prune")

#define plant data for each plant
# order: plant name, start indoors, sow, transplant, harvest, fertilize, prune
# this information is sort of a placeholder as of Sept 10 (format Month-Month). Will add more specific dates later
# after doing more research on DateTime.
plant_data = [
    ("Tomatoes", "Feb-Apr", "Apr-Jun", "Apr-Jun", "Jul-Sep", "", ""),
    ("Potatoes", "", "Jan-Mar", "", "Jun-Jul", "", ""),
    ("Garlic", "", "Sept-Nov", "", "Jul-Aug", "", ""),
    ("Broccoli", "Feb-Mar", "Mar-Apr", "Mar-Apr", "May-Jun", "", ""),
    ("Peppers", "Feb-Mar", "Apr-May", "Apr-May", "Jul-Nov", "", ""),
    ("Cilantro", "", "Apr-May", "", "Jun-Sept", "", ""),
    ("Carrots", "", "Mar-Apr", "", "Jun-Jul", "", ""),
    ("Cucumber", "Mar-Apr", "Apr-Jun", "Apr-Jul", "Aug-Sept", "", ""),
    ("Blackberries", "", "Feb-Mar", "", "Jun-Jul", "Feb-Mar", "Feb-Mar")

]
#populate plant data into treeview widget
for item in plant_data:
    timeline_tree.insert("", "end", values=item)

root.mainloop()