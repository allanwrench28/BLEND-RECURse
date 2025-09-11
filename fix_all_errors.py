import os
from colorama import Fore, init

# Initialize colorama for Windows compatibility
init(autoreset=True)


def display_duke_nukem():
    duke_art = """
      _   _   _   _   _   _
     / \\ / \\ / \\ / \\ / \\ / \\
    (🔥 | D | U | K | E | 💥)
     \\_/ \\_/ \\_/ \\_/ \\_/ \\_/

    """
    print(Fore.YELLOW + duke_art)
    print(
        Fore.RED + "💣 Duke Nukem: Press any key to nuke empty files! 💣"
    )
    input(Fore.GREEN + "\n🚀 Press Enter to continue... 🚀")


def nuke_empty_files_and_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                os.remove(file_path)
                print(Fore.BLUE + f"🗑️ Deleted empty file: {file_path}")

        for name in dirs:
            dir_path = os.path.join(root, name)
            if os.path.isdir(dir_path) and not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(Fore.MAGENTA + f"📂 Deleted empty folder: {dir_path}")


if __name__ == "__main__":
    display_duke_nukem()
    base_directory = os.getcwd()  # Use the current working directory
    nuke_empty_files_and_folders(base_directory)
    print(Fore.CYAN + "\n🎉 All empty files and folders have been nuked! 🎉")