import os
import shutil

# Folder names
source_folder = "source_images"
destination_folder = "moved_images"

# Create source folder if missing
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print(f"📁 Created folder: {source_folder}")
    print("⚠ Please add JPG files inside the folder and run again.")
    exit()

# Create destination folder if missing
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move JPG files
moved_count = 0

for file_name in os.listdir(source_folder):

    if file_name.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        shutil.move(source_path, destination_path)

        moved_count += 1
        print(f"✅ Moved: {file_name}")

# Final result
if moved_count == 0:
    print("⚠ No JPG files found in source_images folder.")
else:
    print(f"\n🎯 Total JPG files moved: {moved_count}")