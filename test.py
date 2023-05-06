import sys
import os
import zipfile

def zipdir(path, archive):
    # Iterate over all files in the directory
    name = archive.filename
    print(name)
    

    for root, dirs, files in os.walk(path): #root is cur dir path
        base = root.split("/")[-1]
        print("base: " , base)
        for file in files:
            # Get the full file path
            file_path = os.path.join(root, file)
            
            # Add the file to the ZIP archive
            if (file != name):
                print("writing: " , file)

                archive.write(file_path)

curDir = "C:/Users/Codia/Desktop/dev_projects/ignore_zipper/test_dir";
file_name = 'output.zip'
zipf = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
zipdir(curDir, zipf)

# Close the ZIP archive
zipf.close()
