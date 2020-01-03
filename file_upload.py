from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from quickstart import get_google_drive_auth_service

folder_id={
	"Docx":"1K9KRQ_Hqgnwp0PDlYTMPN1UqWTvMiLIB",
	"Images":"1-WSZyox5B7U1xvU93CQo5WLZwJdCgy3T",
	"MISC":"1TZvuS_nkD-hJ0-_daLzlYE5gQzv05Dxh",
	"PDFs":"1g1alvjf2dCpB_H2TvrFkTsB2AWyzg9Tw",
	"PPTs":"1hXx5ahjjzyqj7aBZ4RRq3FmT0_UrVeUP",
	"Spreadsheets":"1TJrPb45YbnlN-AjRATT8JYoK0silOiDE",
	"Videos":"1SsAKlEhbX5VoRLg-g5zlAyFqjlysM47c",
	"ZIPs":"17sfXSxk8DH_W2g_KvLn8PlRcQ_5cM_CV"
}
supported_types=["doc",
	"docx",
	"jpg",
	"jpeg",
	"gif",
	"bmp",
	"png",
	"tiff",
	"tif",
	"heic",
	"pdf",
	"ppt",
	"pptx",
	"pptm",
	"xls",
	"xlt",
	"xlsx",
	"xltx",
	"xlsm",
	"mkv",
	"avi",
	"mp4",
	"m4v",
	"7z",
	"rar",
	"zip",
	"zipx"]
mime_types={
	"doc":"application/msword",
	"docx":"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
	"jpg":"image/jpeg",
	"jpeg":"image/jpeg",
	"gif":"image/gif",
	"bmp":"image/bmp",
	"png":"image/png",
	"tiff":"image/tiff",
	"tif":"image/tiff",
	"heic":"image/heic",
	"pdf":"application/pdf",
	"ppt":"application/vnd.ms-powerpoint",
	"pptx":"application/vnd.openxmlformats-officedocument.presentationml.presentation",
	"pptm":"application/vnd.ms-powerpoint.presentation.macroEnabled.12",
	"xls":"application/vnd.ms-excel",
	"xlt":"application/vnd.ms-excel",
	"xlsx":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
	"xltx":"application/vnd.openxmlformats-officedocument.spreadsheetml.template",
	"xlsm":"application/vnd.ms-excel.sheet.macroEnabled.12",
	"mkv":"video/x-matroska",
	"avi":"video/avi",
	"mp4":"video/mp4",
	"m4v":"video/x-m4v",
	"7z":"application/x-7z-compressed",
	"rar":"application/x-rar-compressed",
	"zip":"application/zip",
	"zipx":"application/zip",
	"misc":"application/octet-stream"
}
types={
	"doc":"Docx",
	"docx":"Docx",
	"jpg":"Images",
	"jpeg":"Images",
	"gif":"Images",
	"bmp":"Images",
	"png":"Images",
	"tiff":"Images",
	"tif":"Images",
	"heic":"Images",
	"pdf":"PDFs",
	"ppt":"PPTs",
	"pptx":"PPTs",
	"pptm":"PPTs",
	"xls":"Spreadsheets",
	"xlt":"Spreadsheets",
	"xlsx":"Spreadsheets",
	"xltx":"Spreadsheets",
	"xlsm":"Spreadsheets",
	"mkv":"Videos",
	"avi":"Videos",
	"mp4":"Videos",
	"m4v":"Videos",
	"7z":"ZIPs",
	"rar":"ZIPs",
	"zip":"ZIPs",
	"zipx":"ZIPs",
	"misc":"MISC"
}

class FileUploader:
	def __init__(self):
		pass

	def upload_file_to_drive(self,filename):
		file_type=self.get_file_type(filename)

		file_metadata = {'name': filename,
						  'parents': [folder_id.get(types.get(file_type))]}

		media = MediaFileUpload(filename='/Users/kunalsuthar/Downloads/'+filename,
		                        mimetype=mime_types.get(file_type),resumable=True)

		drive_service=get_google_drive_auth_service()
		file = drive_service.files().create(body=file_metadata,
		                                    media_body=media,
		                                    fields='id').execute()
		print(file.get('id'))

		self.write_to_log(filename)

	def get_file_type(self,filename):
		list_=filename.split('.')
		type_=list_[len(list_)-1].lower()
		
		if type_ not in supported_types:
			type_= "misc"
		
		return type_	
		
	def write_to_log(self,filename):
		pass

	def upload_to_drive(self,file_list):		
		for file in file_list:
			self.upload_file_to_drive(filename=file)