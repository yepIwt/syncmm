#   Written by Sergievsky&Finogenova
#   https://github.com/yepiwt
#   2020


from vk_api import VkApi
from vk_api import audio

class smmvk(object):

	__slots__ = ('vk_audio','albums','favs')

	def __init__(self,login,password):
		vk_session = VkApi(login=login, password=password)
		vk_session.auth()
		self.vk_audio = audio.VkAudio(vk_session)

	def check_availability(self,owner_id):
		try:
			self.vk_audio.get(owner_id=owner_id)
		except:
			raise ValueError('[ADOE] Access Denied or Empty')

	def get(self,owner_id=None):
		self.check_availability(owner_id)
		self.get_favs(owner_id)
		self.get_albums(owner_id)
		return True

	def get_favs(self,owner_id):
		self.favs = []
		for i in self.vk_audio.get(owner_id):
			self.favs.append([i['artist'],i['title']])
		return self.favs
	def get_albums(self,owner_id):
		self.albums = []
		k = 0
		tmp=[]
		for i in self.vk_audio.get_albums(owner_id):
			k += 1
			self.albums.append([self.vk_audio.get(album_id=i['id'],owner_id=i['owner_id'],access_hash=i['access_hash'])[0]['artist'],i['title']])
			for i in self.vk_audio.get(album_id=i['id'],owner_id=i['owner_id'],access_hash=i['access_hash']):
				tmp.append(i['title'])
			self.albums[k-1].append(tmp)
			tmp = []
		return self.albums

	def download_albums(self,dir=None,owner_id=None):
		import requests
		import os
		if not dir:
			dir = 'muisc-lib'
		try:
			os.chdir(dir)
		except:
			os.mkdir(dir)
			os.chdir(dir)
		cur_dir = os.getcwd()
		print('Скачано: ')
		for i in self.vk_audio.get_albums(owner_id):
			alb = self.vk_audio.get(album_id=i['id'],owner_id=i['owner_id'],access_hash=i['access_hash'])
			try:
				os.chdir(str(alb[0]['artist']).rstrip().lstrip())
			except:
				os.mkdir(str(alb[0]['artist']).rstrip().lstrip())
				os.chdir(str(alb[0]['artist']).rstrip().lstrip())
			try:
				os.chdir(i['title'].rstrip().lstrip()) ##Title зд. это название альбома
			except:
				os.mkdir(i['title'].rstrip().lstrip())
				os.chdir(i['title'].rstrip().lstrip())
			for song in alb:
				r = requests.get(song['url'])
				if os.path.isfile(str(song['title']).rstrip().lstrip() + '.mp3') != True:
					with open(str(song['title']).rstrip().lstrip() + '.mp3', 'wb') as track:
						track.write(r.content)
						print(str(song['title']).rstrip().lstrip())
			os.chdir(cur_dir)
		print('')

if __name__ == "__main__":
	print('This is module smm-vk. Smoke docs')
