import os
import pickle

class FileStalker:

	def __init__(self,path='/Users/kunalsuthar/Downloads/'):
		self.path=path

	def get_files_snapshot(self):
		return os.listdir(self.path)

	def get_previous_files_snapshot(self):
		try:
			f=open('fs.pickle','rb')
			list_=pickle.load(f)
			return list_

		except Exception as e:
			print('File does not exist....Saving a snapshot right now')
			f=open('fs.pickle','wb')
			list_=os.listdir(self.path)
			pickle.dump(list_,f)
			return list_	

	def get_files_to_upload(self):
		diff_=list(set(self.get_files_snapshot())-set(self.get_previous_files_snapshot()))
		return diff_

if __name__ == '__main__':
	fs=FileStalker()
	print(fs.get_files_to_upload())