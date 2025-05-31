import os #provides function to interact with operating system
import shutil #provides function for copying and moving files


TARGET_FOLDER = "/Users/anne/Downloads"

# File categories with extensions
extension_map = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Executables": [".exe", ".msi"],
}

def get_category(extension):
    for category, extensions in extension_map.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder():
    for item in os.listdir(TARGET_FOLDER):
        item_path = os.path.join(TARGET_FOLDER, item)

        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            category = get_category(ext)
            destination_folder = os.path.join(TARGET_FOLDER, category)

            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(destination_folder, item))
            print(f"Moved '{item}' to '{category}'")

if __name__ == "__main__":
    organize_folder()
    print("Done organizing")
