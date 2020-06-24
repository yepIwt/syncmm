# Sync My Music

Этот модуль поможет вам сохранить всю вашу музыкальную библиотеку вовремя.

Eng - 

## Перед началом 

На данный момент доступны такие модули, как:

* VK

### Установка

`syncmm` теперь можно установить через `pip`.

```python
pip3 install syncmm
```

## Модули

#### VK

`class smmvk()` имеет `albums`, `favs`

`albums` - это  то, что хранится в разделе "Плейлисты".

`favs` - В разделе "Моя Музыка".

##### Connection

Модуль `vk` принимает следующие аргументы:

* Логин
* Пароль
* ID страницы (Если вы хотите сохранить музыкальную библиотеку другого человека)

```
log = 'cooldude@coolemail.com'
passw = 'passwordforcoolguy'
audios = syncmm.vk(log,passw)
audios.get()
>> True
audios.favs
>> [['CoolArtist#1','CoolSong#1'], ['CoolArtist#2','CoolSong#2']
audios.albums
>> [['CoolGroup#1','CoolTitle',['CoolSong#3','CoolSong#4','CoolSong#5'],['BadGroup#1','BadTitle',['BadSong#1','BadSong#2','BadSong#3']]]
```

## Авторы

Над этим проектом работаем я (@serg1evsky) и @gepeusea. 

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. В файле [LICENSE.txt](LICENSE.txt) 