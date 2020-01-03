from file_stalker import FileStalker
from watchers_of_the_wall import Watcher
from file_upload import FileUploader
import logging

class CloudSinkManager:
	
	def __init__(self):
		self.fs=FileStalker()
		self.wow=Watcher() # Will deprecate it in later version
		self.fu=FileUploader()

	def write_to_run_log(self):
		logging.basicConfig(filename='run.log', filemode='a', format=' %(message)s %(asctime)s',level=logging.INFO)
		logging.info('Ran at')	

if __name__ == '__main__':
	print("#########################")
	print("#######  START  #########")
	print("#########################")
	csm=CloudSinkManager()
	upload_files=csm.fs.get_files_to_upload()
	csm.fu.upload_to_drive(file_list=upload_files)		
	csm.fs.update_snapshots()
	csm.write_to_run_log()
	print("#########################")
	print("#######  FINISH #########")
	print("#########################")
