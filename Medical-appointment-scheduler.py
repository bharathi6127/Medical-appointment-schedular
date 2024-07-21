import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import csv
import webbrowser

def save_to_csv(data):
    with open('appointments.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def submit_form():
    name = name_entry.get()
    phone = phone_entry.get()
    date = date_entry.get_date().strftime('%d-%m-%Y')  # Format date as DD-MM-YYYY
    time = time_combo.get()
    appointment_data = [name, phone, date, time]
    save_to_csv(appointment_data)
    clear_fields()

def clear_fields():
    name_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    date_entry.set_date(datetime.now())
    time_combo.set('')  # Clear the selected time

def open_appointments_url():
    webbrowser.open_new_tab('appointments.csv')

def validate_name_input(text):
    if text.isalpha() or text == "":
        return True
    else:
        return False

def validate_phone_input(text):
    if text.isdigit() or text == "":
        return True
    else:
        return False

root = tk.Tk()
root.title("Medical Appointment Scheduler")
root.configure(background='purple')

name_validator = root.register(validate_name_input)
phone_validator = root.register(validate_phone_input)

name_label = tk.Label(root, text="Name:", background='purple', foreground='white')
name_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
name_entry = tk.Entry(root, validate="key", validatecommand=(name_validator, '%P'))
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Phone Number:", background='purple', foreground='white')
phone_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
phone_entry = tk.Entry(root, validate="key", validatecommand=(phone_validator, '%P'))
phone_entry.grid(row=1, column=1, padx=5, pady=5)

date_label = tk.Label(root, text="Date :", background='purple', foreground='white')
date_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
date_var = tk.StringVar()
date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy', state='readonly')
date_entry.grid(row=2, column=1, padx=5, pady=10)
date_entry.set_date(datetime.now())  # Set default date to current date

time_label = tk.Label(root, text="Time:", background='purple', foreground='white')
time_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
time_options = ['10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM', '12:00 PM', '02:00 PM', '02:30 PM', '03:30 PM', '04:30 PM']
time_combo = ttk.Combobox(root, values=time_options, state="readonly")
time_combo.grid(row=3, column=1, padx=5, pady=5)

submit_button = tk.Button(root, text="Create Appointment", command=submit_form, background='green', foreground='white')
submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

open_url_button = tk.Button(root, text="Open Appointments URL", command=open_appointments_url, background='blue', foreground='white')
open_url_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
