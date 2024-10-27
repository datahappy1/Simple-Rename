# Main global variables
class DynamicConfig:
    counter_menu = None
    file_listbox = None
    toggle_button = None
    remove_all_button = None
    remove_button = None
    select_file_button = None
    part1_label = None
    part2_label = None
    move_up_button = None
    move_down_button = None
    move_to_top_button = None
    move_to_bottom_button = None
    rename_button = None
    current_lang = "CZ"
    file_list = []


# Text variables for multilanguage support
class StaticConfig:

    texts = {
        "EN": {
            "remove_all": "Remove all files",
            "remove_file": "   Remove file    ",
            "name_label": "File name:  ",
            "method_label": "Method:",
            "move_to_top_button": " Top  ",
            "move_to_bottom_button": "Bottom",
            "rename_button": "     Rename Files      ",
            "select_file_button": "   Select Files    ",
            "counter_menu_label": {
                "values": ("Numbers", "Letters"),
                "default": "Numbers"},
        },
        "CZ": {
            "remove_all": "Odebrat všechny soubory",
            "remove_file": "Odebrat soubor",
            "name_label": "Název souboru:",
            "method_label": "Metoda:",
            "move_to_top_button": "Nahoru",
            "move_to_bottom_button": "Dolů",
            "rename_button": "Přejmenuj Soubory",
            "select_file_button": "Vyber soubory",
            "counter_menu_label": {
                "values": ("Čísla", "Písmena"),
                "default": "Čísla"},
        }
    }
