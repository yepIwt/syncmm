![pic](https://i.imgur.com/2BqkM3J.jpg)

Sync My Music
=============


Этот модуль поможет вам сохранить всю вашу музыкальную библиотеку вовремя.

## Перед началом

На данный момент доступны такие модули, как:

* VK
* Yandex Music

### Установка

`syncmm` теперь можно установить через `pip`.

```python
pip install syncmm
```

## Документация

#### Примитивы

Все модули имеют схожее строение и в каждом из них есть три слота:

`albums` - содержимое раздела "Альбомы"

`playlists` - содержимое раздела "Плейлисты"

`favs` - разделы "Моя Музыка" или "Понравившиеся треки"

#### Пример использования syncmm
```
log = 'cooldude@coolemail.com'
passw = 'passwordforcoolguy'
audios = syncmm.vk(log,passw) # на место vk можно вставить yandex
audios.get()
>> True
audios.favs
>> [['CoolArtist#1','CoolSong#1'], ['CoolArtist#2','CoolSong#2']
audios.albums
>> [['CoolGroup#1','CoolTitle',['CoolSong#3','CoolSong#4','CoolSong#5'],['BadGroup#1','BadTitle',['BadSong#1','BadSong#2','BadSong#3']]]
self.playlists
>> [['CoolAuthor#1','CoolTitle',['CoolSong#6','CoolSong#7','CoolSong#8']],['BadAuthor#1','BadTitle',['BadSong#4','BadSong#5','BadSong#6']]]
```

## Авторы

@[yepiwt](http://github.com/yepiwt "какой у меня классный ник")
 и @[gepeusea](https://github.com/gepeusea "классно рисует кстати")

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. в файле [LICENSE.TXT](LICENSE.TXT)
