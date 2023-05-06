import sys
import os
import zipfile

#"C:\Python38\python.exe" "C:\Users\Codia\Desktop\dev projects\ignore_zipper\app.py" "%V"
print()
print("This is CDX's zip utility.");
testVal = "C:/Users/Codia/Desktop/dev_projects/ignore_zipper/test_dir"
if (len(sys.argv) > 1):
    curDir = sys.argv[1]
else:
    curDir = testVal
print("Running in dir: " , curDir)

def zipdir(path, archive):
    # Iterate over all files in the directory
    for root, dirs, files in os.walk(path): #root is cur dir path
        name = archive.filename
        for file in files:
            # Get the full file path
            file_path = os.path.join(root, file)
            file_path = file_path[len(path) + 1:]
            print(file_path)
            # Add the file to the ZIP archive
            if (file != name):
                print("writing: " , file_path)
                archive.write(file_path)


# Specify the directory to zip and the output zip file name
#dir_path = '/path/to/directory'
zip_file_name = 'output.zip'

# Create a new ZIP archive
zipf = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)

base_name = curDir.split("\\")[-1]
print("base name: " , base_name)
# Zip all files in the specified directory
zipdir(curDir, zipf)

# Close the ZIP archive
zipf.close()

print("zipping complete")