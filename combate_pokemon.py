# Importamos funciones random para obtener pokémons de forma aleatoria.
import random

# Importación del archivo de carga de pokémons a través de página web.
from pokeload import get_all_pokemons

# Importación de diccionario de primera y segunda evolución en archivo externo.
from evolution import first_evolution, second_evolution

# Importación de las fortalezas de ataques en archivo externo.
from mult_attack import attack_force


#---------------------------------------FUNCIÓN PERFIL ENTRENADOR POKÉMON-----------------------------------------------
# Función introducción y creación de perfil de entrenador

def get_player_profile(pokemon_list):
    print("\n¡Hola!. Soy el profesor Oak. Vamos a saltarnos toda la parafernalia típica de los juegos de pokémon tradicionales.")
    print("Esto no va de llevale el mapa a tu amigo. Hacerle un recado a mamá o de hablar con desconocidos que dicen cosas que ni te importa.")
    print("Esto es un juego de supervivencia luchando contra varios pokémon aleatorios uno detrás de otro. ¡Aquí vamos a saco!.\n")

    input("Enter para continuar...")

    return {
        "player_name": input("¿Cuál es tu nombre? "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0, # Se puede modificar las pociones y pokébals para añadirle facilidad o dificultad al juego.
    }

#---------------------------------------FIN FUNCIÓN PERFIL ENTRENADOR POKÉMON-------------------------------------------

#------------------------------------------------FUNCIÓN DIFICULTAD-----------------------------------------------------

def dificult(player_profile):
    print("Bien {}. Elige dificultad:\n"
          "Facil. El camino del cobarde. Te da tu mamaita 5 pociones y 5 pokéballs por si te pierdes. Y una rebequica para que no pases frío.\n"
          "Medio. Para gente que ni fu ni fa. Tu mamaita te da un par de pociones y de pokéballs por pena y por perderte de vista.\n"
          "Dificil. El camino del guerrero. Tu mamaita te manda a la aventura con lo puesto y a buscarte la vida.\n".format(player_profile["player_name"]))
    dificultad = input("Elige: (F)ácil, (M)edio o (D)ifícil: ")

    if dificultad == "F":
        player_profile["pokeballs"] = 5
        player_profile["health_potion"] = 5
        print("Has obtenido 5 pociones y 5 pokéballs. ¿Qué pasa, tienes miedo?.")
        input("Enter para continuar...")

    elif dificultad == "M":
        player_profile["pokeballs"] = 2
        player_profile["health_potion"] = 2
        print("Has obtenido 2 pociones y 2 pokéballs. Bueno no está mal. Sal arreando.")
        input("Enter para continuar...")

    elif dificultad == "D":
        player_profile["pokeballs"] = 0
        player_profile["health_potion"] = 0
        print("No obtienes ni pociones ni pokéballs. ¡Ahí ahí esa es la actitud!.")
        input("Enter para continuar...")
    else:
        print("Venga va, elige bien que no tenemos todo el día.")
        dificult(player_profile)


#-----------------------------------FUNCIÓN POKEMONS PARA COMBATE BUCLE-------------------------------------------------
# Esta función marca si hay pokémons vivos en nuestro equipo. Si la suma de las vidas de nuestros pokémons es 0 significa que han caido todos y el juego se ha acabado.

def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0

#----------------------------------------FIN FUNCIÓN POKEMONS PARA COMBATE----------------------------------------------

#---------------------------------------------FUNCIÓN BARRAS DE VIDA----------------------------------------------------
# Función para barras de vida tuyas y del enemigo.

def pokemon_health_bar(pokemon):
    bar_size = 20
    pokemon_segment1 = pokemon["current_health"] / pokemon["base_healt"]
    pokemon_segment2 = bar_size * pokemon_segment1
    pokemon_bar = "#" * int(pokemon_segment2)
    return pokemon_bar

#--------------------------------------------FUNCIÓN INFORMACIÓN COMBATE------------------------------------------------
# Función que muestra una previa información sobre el combate.

def fight_information(player_profile, enemy_pokemon):
    print("\nComienza el combate número {}.".format(player_profile["combats"] + 1))
    print("El pokémon enemigo es {}.".format(enemy_pokemon["name"]))
    print("Dispones de los siguientes pokémons:")
    return choice(player_profile)

#----------------------------------------FUNCIÓN ELEGIR POKÉMON---------------------------------------------------------
# Función que muestra la información de los pokémons disponibles y la selección de uno de ellos.

def choice(player_profile):

    chosen = None
    while not chosen:
        for pokemons in range(len(player_profile["pokemon_inventory"])):
            print("{} - {} {}".format(pokemons, pokemon_info(player_profile["pokemon_inventory"][pokemons]),pokemon_health_bar(player_profile["pokemon_inventory"][pokemons])))
        try:
            choose = player_profile["pokemon_inventory"][int(input("¿Cuál de ellos eliges? "))]
            if choose["current_health"] == 0:
                print("El pokémon está debilitado. Pobrecillo, míralo. ¿Es que no tienes corazón?")
                input("Enter para continuar...")
            else:
                print("¡Te elijo a ti {}!".format(choose["name"]))
                return choose
        except (ValueError, IndexError):
            print("A ver tronco, ¡elige bien anda!")

#----------------------------------------FIN FUNCIÓN ELEGIR POKÉMON-----------------------------------------------------

#----------------------------------------FUNCIÓN INFORMACIÓN POKÉMON----------------------------------------------------
# Función que muestra una lista de los pokémons disponibles.

def pokemon_info(pokemon):
    return "{} | Nv {} | PS {}/{}". format(pokemon["name"],
                                           pokemon["level"],
                                           pokemon["current_health"],
                                           pokemon["base_healt"])

#----------------------------------------FIN FUNCIÓN INFORMACIÓN POKÉMON------------------------------------------------

#----------------------------------------FUNCIÓN COMBATE----------------------------------------------------------------
# Esta función muestra un panel de la situación de los dos pokémons combatientes, la situación del combate y las opciones de combate disponibles, lucha, poción, etc.

def fight(my_pokemon, enemy_pokemon, player_profile):
    capture = 0  # El valor es 0 si el pokémon enemigo no es capturado.
    history_attack = [] # Linta de pokémons tuyos que han atacado al rival para asignarles experiencia.
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:

        if my_pokemon["current_health"] == 0:
            print("{} ha sido debilitado.".format(my_pokemon["name"]))  # Mensaje de que tu pokémon ha sido derrotado
            my_pokemon = choice(player_profile)  # FUNCIÓN ELECCIÓN POKÉMON
        else:
            print("\nPOKÉMON ENEMIGO:")
            print("{}".format(enemy_pokemon["name"]))
            print("Nivel: {}".format(enemy_pokemon["level"]))
            print("Tipo: {}".format(enemy_pokemon["type"][0]))
            print(pokemon_health_bar(enemy_pokemon))
            print("PS: {}/{}\n".format(enemy_pokemon["current_health"], enemy_pokemon["base_healt"]))

            print("TU POKÉMON:")
            print("{}".format(my_pokemon["name"]))
            print("Nivel: {}".format(my_pokemon["level"]))
            print("Tipo: {}".format(my_pokemon["type"][0]))
            print(pokemon_health_bar(my_pokemon))
            print("PS: {}/{}".format(my_pokemon["current_health"], my_pokemon["base_healt"]))
            print("EXP: {}".format(my_pokemon["current_exp"]))


            print("\nTienes las siguientes opciones: \n"
                "L-Luchar\n"
                "V-Poción de vida. Dispones de {} pociones.\n"
                "P-Pokéball. Dispones de {} pokéballs.\n"
                "C-Cambio de pokémon\n"
                "H-Huida".format(player_profile["health_potion"], player_profile["pokeballs"]))
            combat_option = input("¿Cuál eliges?: ")

            if combat_option == "L":
                player_attack(enemy_pokemon, my_pokemon)  # FUNCIÓN ATAQUE JUGADOR
                history_attack.append(my_pokemon) # Almacenas en la lista el pokémon que ha atacado para su reparto de experiencia.
                if enemy_pokemon ["current_health"] <= 0:  # !HAS GANADO EL COMBATE! SE ASIGNAN LAS RECOMPENSAS
                    print("El {} enemigo ha sido debilitado.".format(enemy_pokemon["name"]))
                    pokemon_experience(history_attack, my_pokemon)  # FUNCIÓN EXPERIENCIA SUBIDA DE NIVEL Y EVOLUCIÓN
                    player_profile["combats"] += 1
                    random_object(player_profile) # FUNCIÓN OBTENCIÓN ALEATORIA DE POKÉBALL O POCIÓN DE VIDA
                    input("Enter para continuar...")
                else:
                    input("Turno del contrincante. Enter para continuar...")
                    enemy_attack(my_pokemon, enemy_pokemon,player_profile)  # FUNCIÓN ATAQUE ENEMIGO
            elif combat_option == "V":
                potion(player_profile, my_pokemon)  # FUNCIÓN POCIÓN
                enemy_attack(my_pokemon, enemy_pokemon, player_profile)  # FUNCIÓN ATAQUE ENEMIGO
            elif combat_option == "P":
                capture = pokeball(player_profile, enemy_pokemon, capture)  # FUNCIÓN POKÉBALL
                if capture == 1:  # Esto es cierto si el pokémon enemigo ha sido capturado,
                    print("El combate ha terminado.")  # El combate termina y se rompe el bucle del mismo.
                    break
                else:
                    enemy_attack(my_pokemon, enemy_pokemon, player_profile)  # FUNCIÓN ATAQUE ENEMIGO
            elif combat_option == "C":
                print("\n¡{} ya está bien vuelve!\n".format(my_pokemon["name"]))
                my_pokemon = choice(player_profile)
                enemy_attack(my_pokemon, enemy_pokemon, player_profile)  # FUNCIÓN ATAQUE ENEMIGO
            elif combat_option == "H":
                print("Tío eres un cobarde. ¡Anda y ponte a luchar! Por listo has perdido un turno.")
                input("Enter para continuar...")
                enemy_attack(my_pokemon, enemy_pokemon, player_profile)  # FUNCIÓN ATAQUE ENEMIGO

#----------------------------------------FIN FUNCIÓN COMBATE------------------------------------------------------------

#----------------------------------------FUNCIÓN INFORMACIÓN ATAQUES----------------------------------------------------
# Esta función muestra una lista de los ataques ordenada para la función player_attack.
def attack_info(attack):
    return ("{} - Tipo: {} - Daño: {} - Nivel mínimo uso: {}".format(attack["name"],
                                  attack["type"],
                                  attack["damage"],
                                  attack["min_level"]))

#----------------------------------------FIN FUNCIÓN INFORMACIÓN ATAQUES------------------------------------------------

#-------------------------------------------FUNCIÓN ATAQUE JUGADOR------------------------------------------------------
# Esta función muestra una lista de los ataques del pokémon, elige uno y daña al contrincante.
def player_attack(enemy_pokemon, my_pokemon):
    print("{} tiene los siguientes ataques:".format(my_pokemon["name"]))
    for chosen_attack in range(len(my_pokemon["attacks"])):
        print("{} - {}".format(chosen_attack,
                               attack_info(my_pokemon["attacks"][chosen_attack])))
    attack_chosen = int(input("Elige un ataque: "))

    # El try es por si se sale del índice de ataques máximo.
    try:
        # Se compara el nivel del pokémon del usuario con el mínimo nivel de uso del ataque. Si no se cumple, el ataque no se puede realizar.
        """if int(my_pokemon["attacks"][attack_chosen]["min_level"]) > int(my_pokemon["level"]):
            print("No se puede usar {}. El mínimo nivel para utilizarlo es {}.".format(my_pokemon["attacks"][attack_chosen]["name"],
                                                                                      my_pokemon["attacks"][attack_chosen]["min_level"]))
            print("Elige otro ataque.")
            input("Pulsa enter para continuar...")
            player_attack(enemy_pokemon, my_pokemon)  # Se llama de nuevo a la FUNCIÓN ATAQUE JUGADOR como si fuera un bucle while.
        else:"""
        print("¡{} usa el ataque {}!".format(my_pokemon["name"],
                                                my_pokemon["attacks"][attack_chosen]["name"]))
        attack_mult(my_pokemon["attacks"][attack_chosen], enemy_pokemon, attack_force)
        print("El {} enemigo recibe {} de daño.".format(enemy_pokemon["name"],
                                                            my_pokemon["attacks"][attack_chosen]["damage"]))
        if my_pokemon["attacks"][attack_chosen]["damage"] == 0:
            print("No has hecho absolutamente nada. ¡Macho. Has perdido tiempo y saliba al decir el ataque!")
        else:
            enemy_pokemon["current_health"] = enemy_pokemon["current_health"] - my_pokemon["attacks"][attack_chosen]["damage"]
    except (ValueError, IndexError):
        print("No ves que hay {} ataques, no merecerías seguir jugando a Pokemon Survivor, solo pierdes un turno y la próxima vez te espabilas.".format(chosen_attack + 1))

#-----------------------------------------FIN FUNCIÓN ATAQUE JUGADOR----------------------------------------------------

#-------------------------------------------FUNCIÓN ATAQUE ENEMIGO------------------------------------------------------
# Esta función desarrolla de manera aleatoria el ataque del enemigo.
def enemy_attack(my_pokemon, enemy_pokemon, player_profile):
    chosen_enemy_attack = random.randint(0, len(enemy_pokemon["attacks"]) - 1)

    print("El {} enemigo ha usado el ataque {}".format(enemy_pokemon["name"],
                                                       enemy_pokemon["attacks"][chosen_enemy_attack]["name"]))
    attack_mult(enemy_pokemon["attacks"][chosen_enemy_attack], my_pokemon, attack_force)
    print("Tu pokémon {} ha recibido {} de daño".format(my_pokemon["name"],
                                                        enemy_pokemon["attacks"][chosen_enemy_attack]["damage"]))

    if enemy_pokemon["attacks"][chosen_enemy_attack]["damage"] == 0:
        print("El {} enemigo no ha hecho absolutamente nada. Ha perdido el tiempo así que mejor para tí.". format(enemy_pokemon["name"]))
        input("Enter para continuar...")
    else:
        my_pokemon["current_health"] = my_pokemon["current_health"] - enemy_pokemon["attacks"][chosen_enemy_attack]["damage"]
        input("Enter para continuar...")

    if my_pokemon["current_health"] <= 0:
        my_pokemon["current_health"] = 0


#-----------------------------------------FIN FUNCIÓN ATAQUE ENEMIGO----------------------------------------------------

#----------------------------------------FUNCIÓN MULTIPLICADOR ATAQUE---------------------------------------------------
# Si el ataque de tu pokémon o del enemigo es muy eficaz.
def attack_mult(pokemon_attack, type_pokemon, attack_force):
    type = {pokemon_attack["type"]: type_pokemon["type"][0]}

    for attack, types in attack_force.items():
        if pokemon_attack["type"] in attack and type_pokemon["type"][0] in types:

            pokemon_attack["damage"] *= 1.25  # Si es efectivo el daño del ataque aumenta
            print("Es muy eficaz")


#----------------------------------------FIN FUNCIÓN MULTIPLICADOR ATAQUE-----------------------------------------------

#------------------------------------------------FUNCIÓN EVOLUCIÓN------------------------------------------------------
# La función realiza según el nivel del pokémon la primera o segunda evolución del mismo con la lista de evolution exportada de un archivo py externo. evolution.py.
def evolution_pokemon(my_pokemon, first_evolution, second_evolution):
    if my_pokemon["level"] == 1: # Si se llega al nivel adecuado, el pokémon experimenta su primera evolución.
        for evo1 in first_evolution:
            if my_pokemon["name"] in evo1:
                print("¡Anda!. Tu pokémon {} está evolucionando... (Imagina que se escucha la típica música de evolución de los juegos de pokémon)".format(my_pokemon["name"]))
                input(("Pulsa Enter para continuar..."))
                my_pokemon["name"] = first_evolution[evo1] # Se guarda el nombre de la evolución en el nombre de pokémon original (mirar archivo evolution).
                print("Tu pokémon ha evolucionado en {}".format(my_pokemon["name"]))
                input(("Pulsa Enter para continuar..."))

    if my_pokemon["level"] == 1:  # Si se llega al nivel adecuado, el pokémon experimenta su segunda evolución
        for evo2 in second_evolution:
            if my_pokemon["name"] in evo2:
                print("¡Anda!. Tu pokémon {} está evolucionando... (Imagina que se escucha la típica música de evolución de los juegos de pokémon)".format(my_pokemon["name"]))
                input(("Pulsa Enter para continuar..."))
                my_pokemon["name"] = second_evolution[evo2]  # Se guarda el nombre de la evolución en el nombre de pokémon original (mirar archivo evolution).
                print("Tu pokémon ha evolucionado en {}".format(my_pokemon["name"]))
                input(("Pulsa Enter para continuar..."))

#---------------------------------------------FIN FUNCIÓN EVOLUCIÓN-----------------------------------------------------

#----------------------------------------FUNCIÓN POCIÓN-----------------------------------------------------------------
# Función que muetra la opción de tomar poción
def potion(player_profile, my_pokemon): # Si no tienes pociones de vida en el inventario, se muestra esto.
    if player_profile["health_potion"] == 0:
        print("No dispones de pociones de vida. Lo pone claramente, ¿es usted tonto, eh?")

        input("Enter para continuar...")

    else: # Si tienes pociones de vida en el inventario pero la vida completa se muestra esto.
        if my_pokemon["current_health"] == my_pokemon["base_healt"]:
            print("El pokemon ya tiene la vida al completo.")
        else: # Si tienes pociones de vida en el inventario y menos de 100 de vida se muestra esto.
            print("Usas poción, restauras 50 PS a tu pokémon")
            player_profile["health_potion"] -= 1
            my_pokemon["current_health"] += 50
            if my_pokemon["current_health"] > my_pokemon["base_healt"]:
                my_pokemon["current_health"] = my_pokemon["base_healt"]
            print("Ahora tu pokemon tiene {}/{}".format(my_pokemon["current_health"],my_pokemon["base_healt"]))
            print("Ahora tienes {} pociones de vida.".format(player_profile["health_potion"]))

            input("Enter para continuar...")

#--------------------------------------FIN FUNCIÓN POCIÓN---------------------------------------------------------------

#----------------------------------------FUNCIÓN POKEBALL---------------------------------------------------------------
# Muestra si dispones o no de pokébol y da paso a la función captura.
def pokeball(player_profile, enemy_pokemon, capture):
    if player_profile["pokeballs"] == 0:
        print("No dispones de pokeballs. Lo pone claramente. Ahora pierdes un turno y la próxima vez estás más al loro.")

        input("Enter para continuar...")
    else:
        player_profile["pokeballs"] -= 1
        print("Arrojas la pokéball al {} enemigo.".format(enemy_pokemon["name"]))
        input("Enter para continuar...")
        capture = catch_pokemon(player_profile, enemy_pokemon, capture)  # FUNCIÓN CAPTURA POKÉMON
        print("Ahora dispones de {} pokeballs.".format(player_profile["pokeballs"]))
        return capture
        input("Enter para continuar...")

#--------------------------------------FIN FUNCIÓN POKEBALL-------------------------------------------------------------

#--------------------------------------FUNCIÓN CAPTURA POKÉMON----------------------------------------------------------
# Marca una posibilidad de capturar el pokémon enemigo en función de la vida del mismo.
def catch_pokemon(player_profile, enemy_pokemon, capture):
    if enemy_pokemon["current_health"] > 50:  # Si el pokémon enemigo tiene más del 50% de vida, no se puede capturar.
      print("¡Oh, no! el {} enemigo se ha escapado".format(enemy_pokemon["name"]))
      input("Enter para continuar...")
    elif 25 < enemy_pokemon["current_health"] <= 50:  # Si el pokémon enemigo tiene entre 25 y 50 ps entra en probabilidad del 50%.
        catch = random.randint(0,1)
        if catch == 1:
            print("¡Felicidades!. Has atrapado a {}".format(enemy_pokemon["name"]))
            player_profile["pokemon_inventory"].append(enemy_pokemon)
            capture = 1
            return capture
            input("Enter para continuar...")
        else:
            print("¡Oh, no! el {} enemigo se ha escapado".format(enemy_pokemon["name"]))
            input("Enter para continuar...")
    else:
        print("¡Felicidades!. Has atrapado a {}".format(enemy_pokemon["name"]))
        player_profile["pokemon_inventory"].append(enemy_pokemon)
        capture = 1
        return capture
        input("Enter para continuar...")

#--------------------------------------FIN FUNCIÓN CAPTURA POKÉMON------------------------------------------------------

#----------------------------------------FUNCIÓN OBJETOS ALEATORIOS-----------------------------------------------------
# Función que da probabilidad a obtener un objeto al acabar un combate.
def random_object(player_profile):
    object = random.randint(0, 1)  # Se genera de manera aleatoria un 0 o un 1.
    if object == 0:
        print("Has obtenido una poción de vida.")
        player_profile["health_potion"] += 1
    else:
        print("Has obtenido una pokéball.")
        player_profile["pokeballs"] += 1
#----------------------------------------FIN FUNCIÓN OBJETOS ALEATORIOS-------------------------------------------------

#----------------------------------------FUNCIÓN EXPERIENCIA POKÉMON----------------------------------------------------
# Función que asigna experiencia al acabar el combate.
def pokemon_experience(history_attack, my_pokemon):
    for pokemon in history_attack:
        if pokemon["current_health"] == 0:
            print("El pokémon ha sido debilitado, no obtiene experiencia.")
        else:
            experience = random.randint(1, 5)
            pokemon["current_exp"] += experience
            print("{} ha ganado {}/20 puntos de experiencia.".format(pokemon["name"], pokemon["current_exp"]))

    if pokemon["current_exp"] >= 20:  # Se fija en 20 puntos de experiencia la subida de nivel pokémon.
        pokemon["current_exp"] = pokemon["current_exp"] - 20  # Esto es para añadir experiencia si sobra.
        pokemon["level"] += 1  # El pokémon sube de nivel.
        pokemon["base_healt"] += 20  # La vida del pokémon aumenta con el aumento de nivel.
        pokemon["current_health"] = pokemon["base_healt"]  # El pokémon recupera la vida con el añadido.
        print("¡{} ha subido al nivel {}!".format((pokemon["name"]), pokemon["level"]))
    evolution_pokemon(my_pokemon, first_evolution, second_evolution) # Función evolución Pokémon.

#---------------------------------------FIN FUNCIÓN EXPERIENCIA POKÉMON-------------------------------------------------

#--------------------------------------FUNCIÓN PRINCIPAL----------------------------------------------------------------
def main():
    # Obtenemos la lista de los 150 pokémons a través del archivo pokeload.
    pokemon_list = get_all_pokemons()
    input("Enter para continuar...")

    # Creamos el perfil de entrenador pokémon.
    player_profile = get_player_profile(pokemon_list)

    # Seleccionamos nivel de dificultad del juego

    dificult(player_profile)

    # Bucle que se repite mientras el entrenador tenga pokémons, combate tras combate.
    while any_player_pokemon_lives(player_profile):
        # Pokémon enemigo de forma aleatoria.
        enemy_pokemon = random.choice(pokemon_list)
        # Información antes de combate y elección de pokémon.
        my_pokemon = fight_information(player_profile, enemy_pokemon)
        # Combate pokémon
        fight(my_pokemon, enemy_pokemon, player_profile)
    # Mensaje de fin del juego al perder los pokémons.
    print("{} Has perdido en el combate número {}".format(player_profile["player_name"], player_profile["combats"] + 1))
    if player_profile["combats"] < 5:
        print("Solo {} combates. ¡Eres una lastima!".format(player_profile["combats"]))
    elif player_profile["combats"] >= 5:
        print("{} combates. ¡Bueno venga una medallita!".format(player_profile["combats"]))
    print("FIN DEL JUEGO")


if __name__ == "__main__":
    main()

#--------------------------------------FIN FUNCIÓN PRINCIPAL------------------------------------------------------------