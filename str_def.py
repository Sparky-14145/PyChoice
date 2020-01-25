'''
str_def.py
Define some strings to fit the different languages.
'''

# init
settings, lang = {}, {}
with open("assets/cfg.txt", "r") as file:
    for i in file:
        if not i: break
        k, v = i.replace('\n', '').split(':')
        settings[k] = v
with open("assets/" + settings["lang"] + ".txt", "r") as file:
    for i in file:
        if not i: break
        k, v = i.replace('\n', '').split(':')
        lang[k] = v

def get_setting(key):
    return settings[key]

def set_setting(key, value):
    global settings
    settings[key] = value

def get_lang(key):
    return lang[key]