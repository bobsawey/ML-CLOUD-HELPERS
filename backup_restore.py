# Simple Google Drive backup script with automatic authentication
# for Google Colaboratory (Python 3)

# Instructions:
# 1. Run this cell and authenticate via the link and text box.
# 2. Copy the JSON output below this cell into the `mycreds_file_contents`
#    variable.  Authentication will occur automatically from now on.
# 3. Create a new folder in Google Drive and copy the ID of this folder
#    from the URL bar to the `folder_id` variable.
# 4. Specify the directory to be backed up in `dir_to_backup`.

# Caveats:
# 1. The backup/restore functions override existing files both locally and
#    remotely without warning.
# 2. Empty directories and files are ignored.
# 3. Use at your own risk.

#!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import google.colab
from oauth2client.client import GoogleCredentials
import glob, os

folder_id = 'GOOGLE_DRIVE_FOLDER_ID_HERE'
dir_to_backup = 'LOCAL_BACKUP_DIRECTORY_HERE'
mycreds_file_contents = 'PASTE_JSON_STRING_HERE'
mycreds_file = 'mycreds.json'

with open(mycreds_file, 'w') as f:
  f.write(mycreds_file_contents)

def authenticate_pydrive():
  gauth = GoogleAuth()
  
  # https://stackoverflow.com/a/24542604/5096199
  # Try to load saved client credentials
  gauth.LoadCredentialsFile(mycreds_file)
  if gauth.credentials is None:
    # Authenticate if they're not there
    google.colab.auth.authenticate_user()
    gauth.credentials = GoogleCredentials.get_application_default()
  elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
  else:
    # Initialize the saved creds
    gauth.Authorize()
  # Save the current credentials to a file
  gauth.SaveCredentialsFile(mycreds_file)
  
  drive = GoogleDrive(gauth)
  return drive

def backup_pydrive():
  drive = authenticate_pydrive()
  paths = list(glob.iglob(os.path.join(dir_to_backup, '**'), recursive=True))
  print(paths)
  
  # Delete existing files
  files = drive.ListFile({'q': "'%s' in parents" % folder_id}).GetList()
  for file in files:
    if file['title'] in paths:
      file.Delete()
  
  for path in paths:
    if os.path.isdir(path) or os.stat(path).st_size == 0:
      continue
    file = drive.CreateFile({'title': path, 'parents':
           [{"kind": "drive#fileLink", "id": folder_id}]})
    file.SetContentFile(path)
    file.Upload()
    print('Backed up %s' % path)

def restore_pydrive():
  drive = authenticate_pydrive()
  files = drive.ListFile({'q': "'%s' in parents" % folder_id}).GetList()
  for file in files:
    os.makedirs(os.path.dirname(file['title']), exist_ok=True)
    file.GetContentFile(file['title'])
    print('Restored %s' % file['title'])

authenticate_pydrive()
