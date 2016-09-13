import re


def get_congresistas(string_input):
    """
    Este codigo te permite sacar el nombre de los congresistas que fueron
    autores en el proyecto de ley, basandome en el formato del API de
    "Proyectos De Ley"
    """
    result = re.search('"congresistas":(.*)",', string_input)
    return result.group(1)
