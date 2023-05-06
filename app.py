import sys
import os
import zipfile

def zipdir(path, archive, exclusions):
    # Iterate over all files in the directory
    for root, dirs, files in os.walk(path): #root is cur dir path
        name = archive.filename
        for file in files:
            # Get the full (absolute) file path
            file_path = os.path.join(root, file)
            #print(file_path)
            #print("\\old datasets\\" in file_path)
            #chopping that absolute path into a relative path
            
            dir_check = file_path[len(path):]
            file_path = dir_check[1:]
            extension = "." + file.split(".")[-1]
            
            # Add the file to the ZIP archive after checking if it's on the exclusion list
            if (file in exclusions or extension in exclusions):
                continue;
            
            found_excluded_directory = False;
            for dir in excludedDirs:
                if dir in dir_check:
                    found_excluded_directory = True;
                    break
    
            if not found_excluded_directory:
                archive.write(file_path)

def getExclusions(exclusionSet):
    filename = "exclude.txt"  # Replace with the name of your file
    excludedDirs = set()
    if not os.path.exists(filename):
        print("No exclude.txt found");
        return
    
    with open(filename, "r") as file:
        for line in file:
            # Strip the newline character and add the string to the set
            str = line.strip()
            if ("." not in str):
                excludedDirs.add("\\" + str + "\\")
            else:
                exclusionSet.add(str)
    
    return exclusionSet, excludedDirs


print("This is CDX's zip utility.");

testVal = "C:/Users/Codia/Desktop/dev_projects/ignore_zipper/test_dir"
if (len(sys.argv) > 1):
    curDir = sys.argv[1]
else:
    curDir = testVal
print("Running in dir: " , curDir)

exclusions = set()
zip_file_name = 'output.zip'
exclusions.add(zip_file_name)
exclusions.add("exclude.txt")

exclusions, excludedDirs = getExclusions(exclusions);

print("Excluded Files and Extensions: " , exclusions)
print("Excluded Directories: " , excludedDirs)

# Create a new ZIP archive file
zipf = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
zipdir(curDir, zipf, exclusions) 

# Close the ZIP archive
zipf.close()

print("Zipping Complete")