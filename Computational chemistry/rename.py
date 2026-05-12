import os

def add_prefix_to_files(folder_path, prefix):
    try:
        for filename in os.listdir(folder_path):
            old_path = os.path.join(folder_path, filename)

            # Process only files (skip folders)
            if os.path.isfile(old_path) and not filename.startswith(prefix):
                new_filename = prefix + filename
                new_path = os.path.join(folder_path, new_filename)

                os.rename(old_path, new_path)

        print("Prefix added successfully to all files.")

    except Exception as e:
        print("Error:", e)


# -------- USER INPUT --------
folder_path = input("Enter folder path: ")
prefix = input("Enter prefix to add: ")

add_prefix_to_files(folder_path, prefix)
