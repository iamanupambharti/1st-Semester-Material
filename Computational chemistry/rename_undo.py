import os

def remove_prefix_from_files(folder_path, prefix):
    try:
        for filename in os.listdir(folder_path):
            old_path = os.path.join(folder_path, filename)

            # Check if the file starts with the given prefix
            if os.path.isfile(old_path) and filename.startswith(prefix):
                # Remove the prefix by slicing the string
                new_filename = filename[len(prefix):]
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)

        print("Prefix removed successfully from all files.")

    except Exception as e:
        print("Error:", e)


# -------- USER INPUT --------
folder_path = input("Enter folder path: ")
prefix = input("Enter prefix to remove: ")

remove_prefix_from_files(folder_path, prefix)
