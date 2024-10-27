from os import path
from tkinter import ttk, filedialog
import tkinter as tk
from rename_logic import rename_files
from config import DynamicConfig, StaticConfig

# # This is for app dev precision widget moving
# def display_coordinates(event):
#     x, y = event.x, event.y
#     print(f"Clicked at coordinates: ({x}, {y})")


class Window(DynamicConfig, StaticConfig):
    def __init__(self, dynamic_config, static_config):
        super().__init__()
        self.configuration = static_config
        self.main_config = dynamic_config

    def create_main_window(self):
        # Main window creation
        root = tk.Tk()

        # Window name
        root.title("Simple Mass Rename")

        # Window size setting  (width x height)
        root.geometry("580x500")
        # Fixes window size
        root.resizable(False, False)

        # # This is for app dev precision widget moving
        # root.bind("<Button-1>", display_coordinates)

        # Creation of box for listbox and scroll bar
        listbox_frame = ttk.Frame(root, width=500, height=350)
        listbox_frame.place(x=20, y=60)

        # Creation of list box
        self.file_listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, yscrollcommand=lambda first, last: None)
        self.file_listbox.place(x=0, y=0, width=480, height=350)  # Setting size and parameters of listbox

        # Creation of scroll barr
        scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        scrollbar.place(x=480, y=0, height=350)  # Setting of location and parameters of scroll bar

        # Creation of remove all selected files button
        self.remove_all_button = tk.Button(root, text="Odebrat všechny soubory",
                                           command=lambda: self.remove_all_files(part1_entry), width=19)
        self.remove_all_button.place(x=428, y=420)

        # Creation of remove selected files button
        self.remove_button = tk.Button(root, text="Odebrat soubor",
                                       command=lambda:
                                       self.remove_selected(self.file_list, self.file_listbox, part1_entry))
        self.remove_button.place(x=316, y=420)

        # Fixing scrollbar to listbox
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        # Creation of select file button
        self.select_file_button = tk.Button(root, text="Vyber soubory",
                                            command=lambda: self.select_files(self.file_list, part1_entry))
        self.select_file_button.place(x=20, y=420)

        # Creation of label on file name text field
        self.part1_label = tk.Label(root, text="Název souboru:")
        self.part1_label.place(x=20, y=10)

        # Creation of text field for file name
        part1_entry = tk.Entry(root, width=40)
        part1_entry.place(x=20, y=30)

        # Creation of button to move one up
        self.move_up_button = tk.Button(root, text="△", command=lambda: self.move_up(self.file_list, self.file_listbox))
        self.move_up_button.place(x=525, y=60, width=30, height=30)

        # Creation of button to move one down
        self.move_down_button = tk.Button(root, text="▽",
                                          command=lambda: self.move_down(self.file_list, self.file_listbox))
        self.move_down_button.place(x=525, y=385, width=30, height=30)

        # Creation of button to move top
        self.move_to_top_button = tk.Button(root, text="Nahoru",
                                            command=self.move_to_top)
        self.move_to_top_button.place(x=525, y=90, width=50, height=30)

        # Creation of button to move bottom
        self.move_to_bottom_button = tk.Button(root, text="Dolů", command=self.move_to_bottom)
        self.move_to_bottom_button.place(x=525, y=355, width=50, height=30)

        # Creation of label on rename type
        self.part2_label = tk.Label(root, text="Metoda:")
        self.part2_label.place(x=300, y=10)

        # Creation of rolling menu for rename type
        counter_type = tk.StringVar()
        counter_type.set("Čísla")  # Default settings

        self.counter_menu = ttk.Combobox(root, textvariable=counter_type)
        self.counter_menu['values'] = ("Čísla", "Písmena")
        self.counter_menu.place(x=300, y=29)

        # Creation of button for file rename
        self.rename_button = tk.Button(root, text="Přejmenuj Soubory",
                                       command=lambda: rename_files(part1_entry.get(),
                                                                    counter_type.get(), self.file_list, self))
        self.rename_button.place(x=115, y=420)

        # Button for language toggle
        self.toggle_button = tk.Button(root, text="EN", command=self.toggle_language)
        self.toggle_button.place(x=550, y=1)

        # Start main application loop so window stay open
        root.mainloop()

    def select_files(self, file_list, part1_entry):
        files = filedialog.askopenfilenames()
        if files:
            file_list.clear()
            file_list.extend(files)
            self.update_file_listbox(file_list)

            # Call and activation of prepopulate entry for creating common name of selected files.
            self.prepopulate_entry(file_list, part1_entry)

    # Function for prepopulate entry
    def prepopulate_entry(self, file_list, part1_entry):
        common_prefix = self.get_common_prefix(file_list)
        part1_entry.delete(0, tk.END)
        part1_entry.insert(0, common_prefix)

    # Function for updating and displaying selected files into the filebox

    def update_file_listbox(self, file_list, selected_indices=None):
        self.file_listbox.delete(0, tk.END)
        for file in file_list:
            self.file_listbox.insert(tk.END, path.basename(file))  # Show only the file name
        if selected_indices:
            for index in selected_indices:
                self.file_listbox.select_set(index)

    # Short function for getting the common name of all selected files

    def get_common_prefix(self, file_list):
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
    def remove_all_files(self, part1_entry):
        self.file_listbox.delete(0, tk.END)
        part1_entry.delete(0, tk.END)

    # Remove selected files
    def remove_selected(self, file_list, file_listbox, part1_entry):
        selected_indices = file_listbox.curselection()
        for index in reversed(selected_indices):
            file_list.pop(index)
        self.update_file_listbox(file_list)
        self.prepopulate_entry(file_list, part1_entry)

    # Move selected files one up
    def move_up(self, file_list, file_listbox):
        selected_indices = file_listbox.curselection()
        if not selected_indices:
            return
        for index in selected_indices:
            if index == 0:
                continue
            file_list[index], file_list[index - 1] = file_list[index - 1], file_list[index]
        self.update_file_listbox(file_list, [index - 1 if index > 0 else index for index in selected_indices])

    # Moving selected files one down
    def move_down(self, file_list, file_listbox):
        selected_indices = file_listbox.curselection()
        if not selected_indices:
            return
        for index in reversed(selected_indices):
            if index == len(file_list) - 1:
                continue
            file_list[index], file_list[index + 1] = file_list[index + 1], file_list[index]
        self.update_file_listbox(file_list,
                                 [index + 1 if index < len(file_list) - 1 else index for index in selected_indices])

    # Moving selected top
    def move_to_top(self):
        selected_indices = list(self.file_listbox.curselection())
        if not selected_indices:
            return
        selected_files = [self.file_listbox.get(i) for i in selected_indices]
        for i in reversed(selected_indices):
            self.file_listbox.delete(i)
        for i, file in enumerate(selected_files):
            self.file_listbox.insert(i, file)
            self.file_listbox.selection_set(i)

    # Moving selected files one bottom
    def move_to_bottom(self):
        selected_indices = list(self.file_listbox.curselection())
        if not selected_indices:
            return
        selected_files = [self.file_listbox.get(i) for i in selected_indices]
        for i in reversed(selected_indices):
            self.file_listbox.delete(i)
        for file in selected_files:
            self.file_listbox.insert(tk.END, file)
            self.file_listbox.selection_set(tk.END)

    # Language toggle button
    def toggle_language(self):
        if self.toggle_button.config('text')[-1] == 'CZ':
            self.toggle_button.config(text='EN')
            self.current_lang = 'CZ'
            print("Přepnuto na češtinu")
        else:
            self.toggle_button.config(text='CZ')
            self.current_lang = 'EN'
            print("Switched to English")
        self.update_texts()

    # List and map of widgets
    def update_texts(self):

        widgets = {
            self.remove_all_button: "remove_all",
            self.remove_button: "remove_file",
            self.part1_label: "name_label",
            self.part2_label: "method_label",
            self.move_to_top_button: "move_to_top_button",
            self.move_to_bottom_button: "move_to_bottom_button",
            self.rename_button: "rename_button",
            self.select_file_button: "select_file_button",
            self.counter_menu: "counter_menu_label",
        }

        # Text update for all widgets
        for widget, text_key in widgets.items():
            if isinstance(widget, ttk.Combobox):
                # This part is for rolling menu text update
                widget['values'] = self.configuration.texts[self.current_lang][text_key]['values']
                widget.set(
                    self.configuration.texts[self.current_lang][text_key]['default'])  # Setting default value
            else:
                widget.config(text=self.configuration.texts[self.current_lang][text_key])
