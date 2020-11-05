![pic](https://i.imgur.com/2BqkM3J.jpg)

Sync My Music
=============


Этот модуль поможет вам сохранить всю вашу музыкальную библиотеку вовремя.

## Перед началом

На данный момент доступны такие модули, как:

* VK
* Yandex Music
* Spotify

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
audios = syncmm.vk(log,passw) # на место vk можно вставить yandex/spotify
audios.get()
>> True
audios.favs
>> [['CoolArtist#1','CoolSong#1','LinkToACoolSong#1'], ['CoolArtist#2','CoolSong#2','LinkToACoolSong#2]]
audios.albums
>> [['CoolGroup#1','CoolTitle',[['CoolSong#3','LinkToACoolSong#3'],['CoolSong#4','LinkToACoolSong#4'],'['CoolSong#5','LinkToACoolSong#5']]],['BadGroup#1','BadTitle',[['BadSong#1','LinkToABadSong#1'],['BadSong#2','LinkToABadSong#2'],['BadSong#3','LinkToABadSong#3']]]]
self.playlists
>> [['CoolAuthor#1','CoolTitle',[['CoolArtist#6','CoolSong#6','LinkToACoolSong#6'],['CoolArtist#7','CoolSong#8','LinkToACoolSong#8'],['CoolArtist#8','CoolSong#3','LinkToACoolSong#3']]],['BadAuthor#1','BadTitle',[['BadArtist#4','BadSong#4','LinkToABadSong#4'],['BadArtist#5','BadSong#5','LinkToABadSong#5'],['BadArtist#6','BadSong#6','LinkToABadSong#6']]]]
```

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. в файле [LICENSE.TXT](LICENSE.TXT)
