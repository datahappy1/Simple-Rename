#from window import create_main_window
from window import Window
from config import StaticConfig, DynamicConfig

def main():
    # call for main window creation
    dynamic_configuration = DynamicConfig()
    static_configuration = StaticConfig()
    window = Window(dynamic_configuration, static_configuration)
    window.create_main_window()


if __name__ == "__main__":
    main()

