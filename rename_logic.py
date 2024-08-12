# import os
from widget_logic import update_file_listbox
from os import path, rename


def rename_file(old_path, new_name):
    try:
        directory = path.dirname(old_path)
        extension = path.splitext(old_path)[1]
        new_path = path.join(directory, new_name + extension)
        rename(old_path, new_path)
        print(f"Soubor byl úspěšně přejmenován na {new_path}.")
    except FileNotFoundError:
        print(f"Soubor {old_path} nebyl nalezen.")
    except PermissionError:
        print(f"Nemáte oprávnění k přejmenování souboru {old_path}.")
    except Exception as e:
        print(f"Nastala chyba: {e}")


def rename_files(part1, counter_type, file_list):
    new_file_list = []
    if file_list:
        if counter_type == "Čísla":
            count = 1
            file_count = len(file_list)  # Find the number of selected files
            zero_padding = len(str(file_count))  # Length of the biggest number set the default number of zeroes.
            for file_path in file_list:
                new_name: str = f"{part1}{count:0{zero_padding}d}"
                rename_file(file_path, new_name)
                new_file_list.append(
                    path.join(path.dirname(file_path), new_name + path.splitext(file_path)[1]))
                count += 1

        elif counter_type == "Písmena":
            count = 'a'
            for file_path in file_list:
                new_name = f"{part1}{count}"
                rename_file(file_path, new_name)
                count = chr(ord(count) + 1) if count != 'z' else 'a'
        else:
            print("Neplatný typ počítadla.")
    else:
        print("Žádné soubory k přejmenování.")
    file_list.clear()
    file_list.extend(new_file_list)
    update_file_listbox(file_list)
