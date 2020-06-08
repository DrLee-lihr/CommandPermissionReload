# CommandPermissionReload - A MCDR plugin
# Copyright(C) DrLee_lihr 2020
# GNU General Public License 3.0

# Parts can be modified Start
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
commandpermission_effect=4
commandpermission_enchant=4
commandpermission_execute=4
commandpermission_experience=4
commandpermission_fill=4
commandpermission_forceload=4
commandpermission_function=4
commandpermission_gamemode=4
commandpermission_gamerule=4
commandpermission_give=4
commandpermission_kick=4
commandpermission_kill=4
commandpermission_list=4
commandpermission_locate=4
commandpermission_loot=4
commandpermission_me=4
commandpermission_msg=4
commandpermission_op=4
commandpermission_pardon=4
commandpermission_particle=4
commandpermission_playsound=4
commandpermission_recipe=4
commandpermission_reload=4
commandpermission_replaceitem=4
commandpermission_say=4
commandpermission_schedule=4
commandpermission_scoreboard=4
commandpermission_seed=4
commandpermission_setblock=4
commandpermission_setidletimeout=4
commandpermission_setworldspawn=4
commandpermission_spawnpoint=4
commandpermission_spreadplayers=4
commandpermission_stop=4
commandpermission_stopsound=4
commandpermission_summon=4
commandpermission_tag=4
commandpermission_team=4
commandpermission_teleport=4
commandpermission_teammsg=4
commandpermission_tell=4
commandpermission_tellraw=4
commandpermission_time=4
commandpermission_title=4
commandpermission_trigger=4
commandpermission_w=4
commandpermission_weather=4
commandpermission_whitelist=4
commandpermission_worldborder=4
commandpermission_xp=4
# Parts can be modified end

def on_load(server, old):
	server.add_help_message('!!<command>', '以MCDR可控制的权限系统执行指令§7<command>§r')

def on_user_info(server,info):
    
    if info.content.startswith("!!?") and server.get_permission_level(info)>=commandpermission_help:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))

    if info.content.startswith("!!advancements") and server.get_permission_level(info)>=commandpermission_advancements:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))

    if info.content.startswith("!!ban") and server.get_permission_level(info)>=commandpermission_ban:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!ban-ip") and server.get_permission_level(info)>=commandpermission_ban_ip:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!bossbar") and server.get_permission_level(info)>=commandpermission_bossbar:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!clear") and server.get_permission_level(info)>=commandpermission_clear:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!clone") and server.get_permission_level(info)>=commandpermission_clone:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!data") and server.get_permission_level(info)>=commandpermission_data:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!datapack") and server.get_permission_level(info)>=commandpermission_datapack:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!debug") and server.get_permission_level(info)>=commandpermission_debug:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!defaultgamemode") and server.get_permission_level(info)>=commandpermission_defaultgamemode:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!deop") and server.get_permission_level(info)>=commandpermission_deop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!difficulty") and server.get_permission_level(info)>=commandpermission_difficulty:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!effect") and server.get_permission_level(info)>=commandpermission_effect:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!execute") and server.get_permission_level(info)>=commandpermission_execute:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!experience") and server.get_permission_level(info)>=commandpermission_experience:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!fill") and server.get_permission_level(info)>=commandpermission_fill:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!forceload") and server.get_permission_level(info)>=commandpermission_forceload:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!function") and server.get_permission_level(info)>=commandpermission_function:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!gamemode") and server.get_permission_level(info)>=commandpermission_gamemode:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!gamerule") and server.get_permission_level(info)>=commandpermission_gamerule:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!give") and server.get_permission_level(info)>=commandpermission_give:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!help") and server.get_permission_level(info)>=commandpermission_help:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!kick") and server.get_permission_level(info)>=commandpermission_kick:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!kill") and server.get_permission_level(info)>=commandpermission_kill:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!list") and server.get_permission_level(info)>=commandpermission_list:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!locate") and server.get_permission_level(info)>=commandpermission_locate:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!loot") and server.get_permission_level(info)>=commandpermission_loot:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!me") and server.get_permission_level(info)>=commandpermission_me:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!msg") and server.get_permission_level(info)>=commandpermission_msg:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!op") and server.get_permission_level(info)>=commandpermission_op:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!pardon") and server.get_permission_level(info)>=commandpermission_pardon:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!particle") and server.get_permission_level(info)>=commandpermission_particle:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!playsound") and server.get_permission_level(info)>=commandpermission_playsound:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!recipe") and server.get_permission_level(info)>=commandpermission_recipe:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!reload") and server.get_permission_level(info)>=commandpermission_reload:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!replaceitem") and server.get_permission_level(info)>=commandpermission_replaceitem:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!say") and server.get_permission_level(info)>=commandpermission_say:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!schedule") and server.get_permission_level(info)>=commandpermission_schedule:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!scoreboard") and server.get_permission_level(info)>=commandpermission_scoreboard:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!seed") and server.get_permission_level(info)>=commandpermission_seed:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!setblock") and server.get_permission_level(info)>=commandpermission_setblock:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))

    if info.content.startswith("!!setidletimeout") and server.get_permission_level(info)>=commandpermission_setidletimeout:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))

    if info.content.startswith("!!setworldspawn") and server.get_permission_level(info)>=commandpermission_setworldspawn:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!spawnpoint") and server.get_permission_level(info)>=commandpermission_spawnpoint:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))

    if info.content.startswith("!!spreadplayers") and server.get_permission_level(info)>=commandpermission_spreadplayers:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!stop") and server.get_permission_level(info)>=commandpermission_stop:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!stopsound") and server.get_permission_level(info)>=commandpermission_stopsound:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!summon") and server.get_permission_level(info)>=commandpermission_summon:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!tag") and server.get_permission_level(info)>=commandpermission_tag:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!team") and server.get_permission_level(info)>=commandpermission_team:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!teleport") and server.get_permission_level(info)>=commandpermission_teleport:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!teammsg") and server.get_permission_level(info)>=commandpermission_teammsg:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!tell") and server.get_permission_level(info)>=commandpermission_tell:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!tellraw") and server.get_permission_level(info)>=commandpermission_tellraw:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!time") and server.get_permission_level(info)>=commandpermission_time:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!title") and server.get_permission_level(info)>=commandpermission_title:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!tp") and server.get_permission_level(info)>=commandpermission_teleport:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!trigger") and server.get_permission_level(info)>=commandpermission_trigger:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!w") and server.get_permission_level(info)>=commandpermission_w:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!weather") and server.get_permission_level(info)>=commandpermission_weather:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
    
    if info.content.startswith("!!whitelist") and server.get_permission_level(info)>=commandpermission_whitelist:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))

    if info.content.startswith("!!worldborder") and server.get_permission_level(info)>=commandpermission_worldborder:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))    

    if info.content.startswith("!!xp") and server.get_permission_level(info)>=commandpermission_experience:
        server.execute("execute as "+info.player+" at "+info.player+" run "+info.content.lstrip('!!'))
   
