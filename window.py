
from tkinter import ttk
import tkinter as tk
import config
from widget_logic import select_files, remove_all_files, remove_selected, move_up, move_down, move_to_top, move_to_bottom, toggle_language
from rename_logic import rename_files

# # This is for app dev precision widget moving
# def display_coordinates(event):
#     x, y = event.x, event.y
#     print(f"Clicked at coordinates: ({x}, {y})")


def print_button_size(event):
    # Zjistí aktuální velikost tlačítka v pixelech
    widget = event.widget

    # Získání velikosti tlačítka v pixelech
    pixel_width = widget.winfo_width()
    pixel_height = widget.winfo_height()

    # Získání velikosti tlačítka v textových a řádkových jednotkách
    char_width = pixel_width // widget.winfo_fpixels('1c')
    row_height = pixel_height // widget.winfo_fpixels('1c')

    print(f"Button clicked has size: {char_width} characters wide and {row_height} rows high")

def create_main_window():
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
    root.bind("<Button-1>", print_button_size)

    # Creation of box for listbox and scroll bar
    listbox_frame = ttk.Frame(root, width=500, height=350)
    listbox_frame.place(x=20, y=60)

    # Creation of list box
    config.file_listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, yscrollcommand=lambda f, l: None)
    config.file_listbox.place(x=0, y=0, width=480, height=350)  # Setting size and parameters of listbox

    # Creation of scroll barr
    scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=config.file_listbox.yview)
    scrollbar.place(x=480, y=0, height=350)  # Setting of location and parameters of scroll bar

    # Creation of remove all selected files button
    config.remove_all_button = tk.Button(root, text=config.texts[config.current_lang]["remove_all"], command=lambda: remove_all_files(part1_entry), width=19)
    config.remove_all_button.place(x=428, y=420)

    # Creation of remove selected files button
    remove_button = tk.Button(root, text="Odebrat soubor", command=lambda: remove_selected(file_list, config.file_listbox, part1_entry))
    remove_button.place(x=316, y=420)

    # Fixing scrollbar to listbox
    config.file_listbox.config(yscrollcommand=scrollbar.set)

    # Creation of select file button
    file_list = []

    select_file_button = tk.Button(root, text="Vyber soubory", command=lambda: select_files(file_list, part1_entry))
    select_file_button.place(x=20, y=420)

    # Creation of label on file name text field
    part1_label = tk.Label(root, text="Název souboru:")
    part1_label.place(x=20, y=10)

    # Creation of text field for file name
    part1_entry = tk.Entry(root, width=40)
    part1_entry.place(x=20, y=30)

    # Creation of button to move one up
    move_up_button = tk.Button(root, text="△", command=lambda: move_up(file_list, config.file_listbox))
    move_up_button.place(x=525, y=60, width=30, height=30)

    # Creation of button to move one down
    move_down_button = tk.Button(root, text="▽", command=lambda: move_down(file_list, config.file_listbox))
    move_down_button.place(x=525, y=385, width=30, height=30)

    # Creation of button to move top
    move_to_top_button = tk.Button(root, text="Top", command=move_to_top)
    move_to_top_button.place(x=525, y=90, width=50, height=30)

    # Creation of button to move bottom
    move_to_bottom_button = tk.Button(root, text="Bottom", command=move_to_bottom)
    move_to_bottom_button.place(x=525, y=355, width=50, height=30)

    # Creation of label on rename type
    part2_label = tk.Label(root, text="Metoda:")
    part2_label.place(x=300, y=10)

    # Creation of rolling menu for rename type
    counter_type = tk.StringVar()
    counter_type.set("Čísla")  # Default settings

    counter_menu = ttk.Combobox(root, textvariable=counter_type)
    counter_menu['values'] = ("Čísla", "Písmena")
    counter_menu.place(x=300, y=29)

    # Creation of button for file rename
    rename_button = tk.Button(root, text="Přejmenuj soubory", command=lambda: rename_files(part1_entry.get(), counter_type.get(), file_list))
    rename_button.place(x=115, y=420)

    # Button for language toggle
    config.toggle_button = tk.Button(root, text="EN", command=toggle_language)
    config.toggle_button.place(x=550, y=1)

    # Start main application loop so window stay open
    root.mainloop()

