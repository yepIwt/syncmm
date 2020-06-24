#	Written by Sergievsky&Finogenova
#	https://github.com/serg1evsky
#	2020


import vk_api
from vk_api import audio

class smmvk(object):
	__slots__ = ('vk_audio','albums','favs')

	def __init__(self,login,password):
		vk_session = vk_api.VkApi(login=login, password=password)
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
		tmp=[]
		k = 0
		for i in self.vk_audio.get_albums(owner_id):
			k += 1
			self.albums.append([self.vk_audio.get(album_id=i['id'],owner_id=i['owner_id'],access_hash=i['access_hash'])[k]['artist'],i['title']])
			for i in self.vk_audio.get(album_id=i['id'],owner_id=i['owner_id'],access_hash=i['access_hash']):
				tmp.append(i['title'])
			self.albums[k-1].append(tmp)
			tmp = []
		return self.albums

if __name__ == "__main__":
	print('This is module smm-vk. Smoke docs')

