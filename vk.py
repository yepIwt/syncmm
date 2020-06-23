#	Written by Sergievsky&Finogenova
#	https://github.com/serg1evsky
#								2020


import vk_api
from vk_api import audio

class smmvk(object):
	__slots__ = ('vk_audio', 'groups')
	
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
		"""
		:param login: Логин для входа
		:param password: Пароль для входа
		:param id: ID пользователя библиотеки
		
		"""
		self.check_availability(owner_id)
		self.groups = []
		for i in self.vk_audio.get(owner_id):  #Это просто аудиозаписи
			self.groups.append(str(i['artist']).lower().rstrip())
		for i in self.vk_audio.get_albums(owner_id):  #А это исполнители
			self.groups.append(self.vk_audio.get(album_id=i['id'],owner_id=i['owner_id'],access_hash=i['access_hash'])[0]['artist'].lower().rstrip())
		self.groups = list(set(self.groups))
		for i in self.groups:
			if ',' in i:  #"Bi-2" - "Bi-2, Syphonic Orcestr"
				self.groups[self.groups.index(i)] = i[:i.index(',')]
				i = i[:i.index(',')]  #Исключение, если в названии и ',' и 'feat'
			if 'feat' in i:  #"Noize Mc feat Sonny" - "Noize Mc"
				self.groups[self.groups.index(i)] = i[:i.index(' feat')]
		return list(set(self.groups))
if __name__ == "__main__":
	print('This is module smm-yandex. Smoke docs')