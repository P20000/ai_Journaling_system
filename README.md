Here's a **README.md** for your GitHub repository that describes the code and gives a brief overview of the app:

---

# 🧠 Smart Behavior Logger

Smart Behavior Logger is a Python-based desktop application built with **CustomTkinter** and **Tkinter** that helps you log and analyze your behavior through journaling. The app features an auto-fill system that extracts key data from your journal entries and organizes them into structured fields for better reflection and analysis. It then saves each entry into a file for future reference.

## Features

- **Smart Journal Entry**: Input your thoughts and the app will auto-fill relevant fields such as **Title**, **Tags**, **Mood**, **Type**, **Description**, and **Reaction**.
- **Mood Detection**: Based on the journal entry, the app auto-detects the mood (e.g., Positive, Negative, Sad, Angry).
- **Auto-fill Tags**: The app generates up to 5 tags based on keywords from the entry to help categorize your thoughts.
- **Save Logs**: Entries are saved as **JSON** files, organized with timestamps for easy tracking.
- **Beautiful Interface**: CustomTkinter-based UI with a sleek and user-friendly design.
- **Cross-Platform**: Works on Windows, macOS, and Linux (as long as Python is installed).

## Prerequisites

To run the app, you'll need the following Python libraries:

- `customtkinter`
- `tkinter` (comes with Python)
- `json`
- `os`
- `datetime`

You can install the required dependencies using the following command:

```bash
pip install customtkinter
```

## How to Run

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/smart-behavior-logger.git
   cd smart-behavior-logger
   ```

2. **Install Dependencies** (if you haven't already):

   ```bash
   pip install customtkinter
   ```

3. **Run the Application**:

   ```bash
   python app.py
   ```

   This will launch the Smart Behavior Logger application window.

## How It Works

### 1. **Writing Your Journal**
   - Open the app and start typing your journal entry in the **text box**.
   - The **Auto-Fill Fields** button will analyze the content of your entry and fill in the relevant fields, such as **Title**, **Tags**, **Mood**, **Description**, **Reaction**, and **Type**.

### 2. **Saving Your Entry**
   - After reviewing or editing the fields, click the **Submit Entry** button to save the log.
   - The log will be saved in the **behavior_logs** folder as a **JSON file** with the timestamp as the filename.

### 3. **Log Organization**
   - Logs are saved in the **behavior_logs** directory inside your project folder.
   - Each log contains a structured format with fields like **title**, **type**, **tags**, **mood**, **description**, **reaction**, and **timestamp**.

## Screenshots

![Smart Behavior Logger](screenshots/smart_behavior_logger_ui.png)

## Folder Structure

```
smart-behavior-logger/
│
├── app.py                    # Main app script
├── behavior_logs/             # Folder where logs are saved
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

## Contributing

Feel free to open issues or submit pull requests. Any contributions or suggestions for improvement are welcome!

## License

This project is licensed under the MIT License.

---

Let me know if you want to adjust or add any details to this README!
