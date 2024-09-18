# Zone 7a Garden Reminders

Zone 7a Garden Reminders is a desktop application designed for gardeners in hardiness zone 7a. It helps users track the planting, sowing, transplanting, harvesting, pruning, and fertilizing tasks for various plants by providing timely desktop notifications and a task management system.

## Table of Contents

- Features
- Installation
- Usage
- Plants Included
- Notifications and Sounds
- Data Storage
- Dependencies

## Features

- **Desktop Notifications**: Receive reminders for important gardening tasks such as starting seeds indoors, sowing, transplanting, harvesting, pruning, and fertilizing.
- **Task List**: Track your gardening to-dos and mark tasks as completed.
- **Customizable**: Select which plants you are growing to receive tailored reminders.
- **Automatic Scheduling**: The app automatically checks for tasks that are due today and notifies the user.
- **Sound Alerts**: Plays an alert sound when notifications are triggered.
- **Data Persistence**: Saves the state of selected plants and tasks so you can continue where you left off after closing the app.

## Installation

### Requirements

Ensure you have the following installed:

- Python 3.12 or higher
- pip3 for managing Python packages

### Setup

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies from the `requirements.txt` file:
4. Run the application with the following command:

## Usage

1. **Start the App**: Run `main.py`. The main window will display a list of plants to grow and a task management system.
2. **Select Plants**: Choose the plants you are growing by selecting the checkboxes. This will enable notifications for tasks related to these plants.
3. **Task List**: Any tasks due today will be automatically added to your to-do list. Once completed, you can remove them by selecting the task and clicking "Remove Completed Tasks."
4. **Notifications**: You will receive desktop notifications for any tasks that are due, along with a sound alert.
5. **Data Persistence**: The app automatically saves your selected plants and task list so you can resume from where you left off.

## Plants Included

The app includes pre-configured planting timelines for the following plants commonly grown in zone 7a:

- Potatoes
- Garlic
- Tomatoes
- Peppers
- Cilantro
- Carrots
- Cucumbers
- Broccoli
- Blackberries

## Notifications and Sounds

- **Desktop Notifications**: Notifications are powered by the plyer library and include a brief description of the task due.
- **Sound Alerts**: Notification sounds are provided to alert users when tasks are due. Sounds are stored in the `/sounds` directory and include:
- `leaves_notification_sound.mp3`: Plays when a task is due.
- `startup_bubble_sound.mp3`: Plays when the app starts.

## Data Storage

The app saves user data in the user's home directory, under a hidden folder `.garden_reminders`. This includes:

- **Selected Plants**: Which plants have been selected for growing.
- **To-Do List**: The current gardening tasks in the task list.

The data is stored in a file named `garden_data.pkl`, which is automatically created and updated during app usage.

## Dependencies

This project relies on the following Python libraries:

- **tkinter**: For the graphical user interface (GUI).
- **plyer**: For desktop notifications.
- **playsound3**: For playing audio alerts.
- **pickle**: For saving and loading user data.

The dependencies are listed in the `requirements.txt` file. To install them, use:

### Running Locally

After setting up the environment, you can run the app by executing:
`python3 main.py`
