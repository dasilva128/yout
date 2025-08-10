# utils/gdrive_utils.py
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
import os
from config import DOWNLOAD_DIR

SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def get_drive_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("drive", "v3", credentials=creds)

def upload_to_gdrive(file_path, file_name):
    service = get_drive_service()
    file_metadata = {"name": file_name}
    media = MediaFileUpload(file_path)
    file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    return file.get("id")

def download_from_gdrive(file_id):
    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)
    file_path = f"{DOWNLOAD_DIR}/{file_id}.file"
    with io.FileIO(file_path, "wb") as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
    return file_path