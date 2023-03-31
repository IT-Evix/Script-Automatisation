#Import necessary libraries
import ftplib
import zipfile
import os

# Define the local directories for downloading and extracting files
download_dir = "Local directory of your choice"
extract_dir = "Local directory of your choice"

print('Connexion au serveur ...')
#Connect to the FTP server using FTP class from ftplib
ftp = ftplib.FTP("The server")

#Login to the FTP server with the given credentials
ftp.login("Your login name", "your login password")
print('Connexion au serveur réussie !')

#Define a list of folder paths to download files from
paths = ["folder paths"]
print('Récupération et extraction  des fichiers...')

#Loop over each folder path
for path in paths:
    # Change the current working directory to the folder path
    ftp.cwd(path)
    # Get a list of filenames in the current working directory
    filenames = ftp.nlst()
    # Loop over each filename in the current working directory
    for filename in filenames:
        # Check if the filename ends with ".zip"
        if filename.endswith(".zip"):
            # Define the local filename where the file will be saved
            local_filename = os.path.join(download_dir, filename)
            # Download the file from the FTP server to the local file
            ftp.retrbinary("RETR " + filename, open(local_filename, 'wb').write)
            # Define the directory where the contents of the zip file will be extracted
            extract_to = os.path.join(extract_dir, os.path.splitext(filename)[0])
            # Open the zip file using zipfile library
            zip_ref = zipfile.ZipFile(local_filename, 'r')
            # Extract all the contents of the zip file to a folder
            zip_ref.extractall(extract_to)
            # Close the zip file
            zip_ref.close()
print('Récupération et extraction réussie !')
print('Fin du script')

