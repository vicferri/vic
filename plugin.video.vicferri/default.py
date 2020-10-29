# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/channel/UCGVXCP8-soIb79aQx9bkYSw
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------
import xbmcaddon
import xbmcgui

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')

line1 = "Hola!"
line2 = "Benvinguts al canal iutup"
line3 = "de sa família Caragol"

xbmcgui.Dialog().ok(__addonname__, line1, line2, line3)

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.vicferri'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "UC8oiXzfJepmuuvSMURLo_BA"
YOUTUBE_CHANNEL_ID2 = "UC-VTbGxwaaPYJY64xCSoYaw"
YOUTUBE_CHANNEL_ID3 = "UC-pPXl0YahnWni4ma61htLw"
YOUTUBE_CHANNEL_ID4 = "UCWgGFybfaR-p7fqISsV9nVw"
YOUTUBE_CHANNEL_ID5 = "UCYRhvF4DwgWNKnhOLQaOR0Q"
YOUTUBE_CHANNEL_ID6 = "UCL7lk3Hp5yjOxvTeN7beNUA"
YOUTUBE_CHANNEL_ID7 = "UCQOVMBh9JdWez4QdibgX4Gg"
YOUTUBE_CHANNEL_ID8 = "UCbeN1oDMuGQrzFa5Ruqrojw"
YOUTUBE_CHANNEL_ID9 = "UCc4ZPbVLP6ivIr0LCguUXww"
YOUTUBE_CHANNEL_ID10 = "UCqGQ1UZ1FbS8W8Gy7mcRyHw"
YOUTUBE_CHANNEL_ID11 = "UCtOBoiWwEQUYHy1wU3we1bw"
YOUTUBE_CHANNEL_ID12 = "UCmYZq-mqbREGrS0e__b3cag"
YOUTUBE_CHANNEL_ID13 = "UC13DGVBnDt-cps8TsurWJMw"

# Entry point
def run():
    plugintools.log("vicferri.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("vicferri.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="David",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxkLIG2AhxgSeCOQDDjj6HdrjVNZkS2aWmdABfpeg=s176-c-k-c0xffffffff-no-rj-mo",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Ulisses",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail=icon,
        folder=True )
   	
    plugintools.add_item( 
        #action="", 
        title="Eugeni",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJx9BPcUffvNOe65D2vt2dKPX09ih-dU7TLxlvk9=s176-c-k-c0xffffffff-no-rj-mo",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Photomiki",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJyQIlKmAc11HvaUJyb7WtI5UsjFpCjTTiyBQiNisA=s176-c-k-c0xffffffff-no-rj-mo",
        folder=True )
 
    plugintools.add_item( 
        #action="", 
        title="Víctor",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJzenNzaQ__fqjCLXJLVQNu2VYAd6BXZ6vUBHL_8=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )
   
    plugintools.add_item( 
        #action="", 
        title="Pèl de Gall",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxDDFzVM6p5l3ecS2e7zhASYyve9HO6HoaVWMTZ=s176-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Xisca",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxRzxQNk8oZ24pkMnaq7WeyLOD0he3kdQXCcQQV=s176-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Eugeni",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJwDVfl4E5PMgRUeL1k8xJubNbWe5Gw_N3CqS2aUyQ=s176-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Maria",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJyqjal65KLz2pRx2ykZ_KGSRwSQqstOd7rBGbJF-Q=s176-c-k-c0xffffffff-no-rj-mo",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ivanjot",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID10+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxAIiLqpIpVgR5WqjL5Ut90ryXunj5N6VIUtAnX=s176-c-k-c0xffffffff-no-rj-mo",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cuina de confinament",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID11+"/",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxM1tNTpz5jcgi5km4JL3YexgXTrdT2LZzHQjwH=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Adra",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID12+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Rut",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID13+"/",
        thumbnail=icon,
        folder=True )    
run()
