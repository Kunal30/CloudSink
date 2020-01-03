from file_stalker import FileStalker
from watchers_of_the_wall import Watcher
from file_upload import FileUploader

class CloudSinkManager:
	
	def __init__(self):
		self.fs=FileStalker()
		self.wow=Watcher()
		self.fu=FileUploader()

if __name__ == '__main__':
	csm=CloudSinkManager()
	upload_files=csm.fs.get_files_to_upload()
	print(upload_files)
	csm.fu.upload_to_drive(file_list=upload_files)		
