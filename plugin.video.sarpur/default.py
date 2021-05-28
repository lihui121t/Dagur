#!/usr/bin/env python
# encoding: UTF-8


import sarpur
import urlparse
import xbmcplugin
from sarpur import actions

xbmcplugin.setContent(sarpur.ADDON_HANDLE, 'episodes')

params = dict(urlparse.parse_qsl(sys.argv[2][1:]))


action_key = params.get("action_key")
action_value = params.get("action_value")
name = params.get("name")

try:
    if action_key is None:
        actions.index()
    elif action_key == 'view_channel_index':
        actions.channel_index(int(action_value))
    elif action_key == 'view_channel_category':
        channel, category = action_value.split(';')
        actions.channel_category(int(channel), int(category))
    elif action_key == 'view_channel_category_show':
        actions.channel_category_show(action_value, name)
    elif action_key == 'play':
        actions.play(action_value, name)
    elif action_key == 'view_tab':
        actions.tab_index(action_value)
    else:

        print "Action: {0}, Value: {1}, Name: {2}".format(action_key, action_value, name)

finally:
    xbmcplugin.endOfDirectory(sarpur.ADDON_HANDLE)
