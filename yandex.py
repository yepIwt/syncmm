#	Written by Sergievsky&Finogenova
#	https://github.com/serg1evsky	
#								2020


import requests as r
import re

MUSIC = "https://music.yandex.ru/users/"
DEMAND_ALB = "deco-link_muted\" title=\""                           #These
DEMAND_FAV = "<span class=\"d-track__artists\"><a href=\"/artist/"  #are filters
IA = 24  #indent on albums (offset)
IF = 7  #indent on fav (offset)

class smmyandex(object):
	__slots__ = ('groups','me')
	
	def __init__(self,name):
		self.me = name
		self.check_availavility()

	def check_availavility(self):
		try:
			r.get(MUSIC+self.me+"/tracks").raise_for_status()
		except:
			raise r.exceptions.HTTPError('[ADOE] Access Denied or Empty')

	def get(self):
		self.groups = []
		dt = r.get(MUSIC+self.me+"/albums")
		n = [m.start() for m in re.finditer(DEMAND_ALB,dt.text)]
		for i in range(len(n)):
			self.groups.append(dt.text[n[i]+IA:dt.text.index('"', n[i]+IA)])

		dt = r.get(MUSIC+self.me+"/tracks")
		n = [m.start() for m in re.finditer(DEMAND_FAV, dt.text)]
		for i in range(len(n)):
			d = dt.text.index('title="', n[i])  #Вспомогательная переменная, без нее труднее понять код
			self.groups.append(dt.text[d+IF:dt.text.index('"',d+IF)])
		self.groups = list(set(self.groups))
		
		for i in self.groups:
			if ',' in i:  #"Bi-2" - "Bi-2, Syphonic Orcestr"
				self.groups[self.groups.index(i)] = i[:i.index(',')]
				i = i[:i.index(',')]  #Исключение, если в названии и ',' и 'feat'
			if 'feat' in i:  #"Noize Mc feat Sonny" - "Noize Mc"
				self.groups[self.groups.index(i)] = i[:i.index(' feat')]
			if '&#' in i:  #Убрать юни-коды
				self.groups[self.groups.index(i)] = i[:i.index('&')] + i[i.index(';')+1:] 
		return list(set(self.groups))
if __name__ == "__main__":
	print('This is module smm-yandex. Smoke docs')