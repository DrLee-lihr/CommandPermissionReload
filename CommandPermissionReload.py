# CommandPermissionReload Copyright(C) 2020 HuoranLi
import random

commandpermission_help=1
commandpermission_advancements=4
commandpermission_ban=4
commandpermission_ban_ip=4
commandpermission_banlist=4
commandpermission_bossbar=4
commandpermission_clear=4
commandpermission_clone=4
commandpermission_data=4
commandpermission_datapack=4
commandpermission_debug=4
commandpermission_defaultgamemode=4
commandpermission_deop=4
commandpermission_difficulty=4

def on_user_info(server,info):
    if info.content.startswith("!?") and server.get_permission_level(info)>=commandpermission_help:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))

    if info.content.startswith("!advancements") and server.get_permission_level(info)>=commandpermission_advancements:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))

    if info.content.startswith("!ban") and server.get_permission_level(info)>=commandpermission_ban:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!ban-ip") and server.get_permission_level(info)>=commandpermission_ban_ip:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!bossbar") and server.get_permission_level(info)>=commandpermission_bossbar:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!clear") and server.get_permission_level(info)>=commandpermission_clear:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!clone") and server.get_permission_level(info)>=commandpermission_clone:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!data") and server.get_permission_level(info)>=commandpermission_data:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!datapack") and server.get_permission_level(info)>=commandpermission_datapack:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!debug") and server.get_permission_level(info)>=commandpermission_debug:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!defaultgamemode") and server.get_permission_level(info)>=commandpermission_defaultgamemode:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!difficulty") and server.get_permission_level(info)>=commandpermission_difficulty:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    if info.content.startswith("!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!'))
    
    
