import vlc

instance = vlc.Instance()
player = instance.media_player_new()
medialist = instance.media_list_new()
listplayer = instance.media_list_player_new()
listplayer.set_media_player(player)
for i in (range(1, 10)):          # the second value for range() can be set without problem also higher
    track = instance.media_new("cdda:///F:/", (":cdda-track=" + str(i)))
    medialist.add_media(track)
listplayer.set_media_list(medialist)
listplayer.play()

while True:
    pass
