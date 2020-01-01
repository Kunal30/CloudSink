from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from quickstart import get_google_drive_auth_service

file_metadata = {'name': 'photo.jpg',
				  'parents': ['15m-GmJ2YzG1hk70A21DxkgANRi5mH9oT']}
media = MediaFileUpload(filename='/Users/kunalsuthar/Downloads/Apple_Macbook_air_2018_Stock_wallpapers02.jpg',
                        mimetype='image/jpeg',resumable=True)
drive_service=get_google_drive_auth_service()
print(drive_service.files().list().execute())
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
print(file.get('id'))