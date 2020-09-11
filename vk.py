#   Written by Sergievsky&Finogenova
#   https://github.com/yepiwt
#   2020


from vk_api import VkApi
from vk_api import audio

class smmvk(object):

	__slots__ = ('vk_audio','albums','favs','playlists')

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
		self.get_playlists(owner_id)
		return True

	def get_favs(self,owner_id):
		self.favs = []
		for i in self.vk_audio.get(owner_id):
			self.favs.append([i['artist'],i['title']])
		return self.favs
	
	def get_albums(self,owner_id):
		self.albums = []
		songs = []
		lib = self.vk_audio.get_albums(owner_id)
		for alb in lib:
			if alb['owner_id'] < 0:
				title = alb['title'] #Название альбома
				alb_song = self.vk_audio.get(album_id=alb['id'],owner_id=alb['owner_id'],access_hash=alb['access_hash'])
				art = alb_song[0]['artist']
				for song in alb_song:
					songs.append(song['title'])
				
				self.albums.append([art,title,songs])
			songs = []
		return self.albums
	
	def get_playlists(self,owner_id):
		self.playlists = []
		songs = []
		lib = self.vk_audio.get_albums(owner_id)
		for alb in lib:
			if alb['owner_id'] > 0:
				title = alb['title'] #Название плейлиста
				alb_song = self.vk_audio.get(album_id=alb['id'],owner_id=alb['owner_id'],access_hash=alb['access_hash'])
				art = alb_song[0]['artist']
				for song in alb_song:
					songs.append(song['title'])
				
				self.playlists.append([art,title,songs])
			songs = []
		return self.playlists

if __name__ == "__main__":
	print('This is module smm-vk. Smoke docs')