import io
import os
from random import randint
from Google import Create_Service
import  pandas as pd
import sys
import numpy as np
import data_retriever
from googleapiclient.http import MediaIoBaseDownload

file_name = 'image.jpeg'
token = 'token.json'
api_name = 'drive'
api_version = 'v3'
folders_ids = data_retriever.get_folder_ids()
scopes = ['https://www.googleapis.com/auth/drive']

service = Create_Service(token,api_name,api_version,scopes)
def get_ids():
        ids = []
        for folder in folders_ids:
                query = f"parents =  '{folder}'"
                response = service.files().list(q=query,pageSize=1000).execute()
                files = response.get('files')
                next_page_token = response.get('nextPageToken')
                df = pd.DataFrame(files)
                temp = df['id'].tolist()
                ids = ids + temp
        return ids


def download(id):
        request = service.files().get_media(fileId=id)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh,request=request)

        done = False
        while not done:
                status,done = downloader.next_chunk()

        fh.seek(0)

        with open(file_name,'wb') as f:
                f.write(fh.read())
                f.close()

def save_random_file():
        ids = get_ids()
        index = randint(0,10*len(ids))
        index = index%len(ids)
        download(ids[index])







