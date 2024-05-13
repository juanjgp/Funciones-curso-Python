# Creamos un diccionario con fortalezas y debilidades de ataques, izquierda = tipo del ataque, derecha contra que tipo es fuerte

attack_force = {
    "fuego":["planta","bicho","hielo"],
    "agua":["fuego","roca","tierra"],
    "planta":["agua","roca","tierra"],
    "electrico":["agua","volador"],
    "lucha":"normal",
    "hielo":["dragon","planta","tierra","volador"],
    "veneno":"planta",
    "tierra":["electrico","fuego","roca","veneno"],
    "volador":["bicho","lucha","planta"],
    "psiquico":["lucha","veneno"],
    "bicho":["planta","psiquico"],
    "roca":["fuego","bicho","volador","hielo"],
    "fantasma":"fantasma",
    "dragon":"dragon"
    }

