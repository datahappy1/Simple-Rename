from tkinter import filedialog
from os import path
import tkinter as tk
import config


# Function for selecting files and call for display them inside the filebox
def select_files(file_list, part1_entry):
    files = filedialog.askopenfilenames()
    if files:
        file_list.clear()
        file_list.extend(files)
        update_file_listbox(file_list)

        # Call and activation of prepopulate entry for creating common name of selected files.
        prepopulate_entry(file_list, part1_entry)


# Function for prepopulate entry
def prepopulate_entry(file_list, part1_entry):
    common_prefix = get_common_prefix(file_list)
    part1_entry.delete(0, tk.END)
    part1_entry.insert(0, common_prefix)


# Function for updating and displaying selected files into the filebox
def update_file_listbox(file_list, selected_indices=None):
    config.file_listbox.delete(0, tk.END)
    for file in file_list:
        config.file_listbox.insert(tk.END, path.basename(file))  # Show only the file name
    if selected_indices:
        for index in selected_indices:
            config.file_listbox.select_set(index)


# Short function for getting the common name of all selected files
def get_common_prefix(file_list):
    if not file_list:
        return ""

    base_names = [path.splitext(path.basename(file))[0] for file in file_list]
    if len(base_names) == 1:
        return base_names[0]

    prefix = path.commonprefix(base_names)
    if prefix:
        return prefix

    else:
        # If there is no common prefix return the first selected file name
        return base_names[0]


# Removing all files from selection box and clearing the common prefix
def remove_all_files(part1_entry):
    config.file_listbox.delete(0, tk.END)
    part1_entry.delete(0, tk.END)


# Remove selected files
def remove_selected(file_list, file_listbox, part1_entry):
    selected_indices = file_listbox.curselection()
    for index in reversed(selected_indices):
        file_list.pop(index)
    update_file_listbox(file_list)
    prepopulate_entry(file_list, part1_entry)


# Move selected files one up
def move_up(file_list, file_listbox):
    selected_indices = file_listbox.curselection()
    if not selected_indices:
        return
    for index in selected_indices:
        if index == 0:
            continue
        file_list[index], file_list[index - 1] = file_list[index - 1], file_list[index]
    update_file_listbox(file_list, [index - 1 if index > 0 else index for index in selected_indices])


# Moving selected files one down
def move_down(file_list, file_listbox):
    selected_indices = file_listbox.curselection()
    if not selected_indices:
        return
    for index in reversed(selected_indices):
        if index == len(file_list) - 1:
            continue
        file_list[index], file_list[index + 1] = file_list[index + 1], file_list[index]
    update_file_listbox(file_list, [index + 1 if index < len(file_list) - 1 else index for index in selected_indices])


# Moving selected top
def move_to_top():
    selected_indices = list(config.file_listbox.curselection())
    if not selected_indices:
        return
    selected_files = [config.file_listbox.get(i) for i in selected_indices]
    for i in reversed(selected_indices):
        config.file_listbox.delete(i)
    for i, file in enumerate(selected_files):
        config.file_listbox.insert(i, file)
        config.file_listbox.selection_set(i)


# Moving selected files one bottom
def move_to_bottom():
    selected_indices = list(config.file_listbox.curselection())
    if not selected_indices:
        return
    selected_files = [config.file_listbox.get(i) for i in selected_indices]
    for i in reversed(selected_indices):
        config.file_listbox.delete(i)
    for file in selected_files:
        config.file_listbox.insert(tk.END, file)
        config.file_listbox.selection_set(tk.END)
