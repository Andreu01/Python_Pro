#Lista de palabras 
meme_dict = {               
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY":" aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "TUANIS": "Excelente, genial",
            "CHUNCHE": "Cosa, objeto"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ") #Pregunta hacia el usuario
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esa palabra no esta en el dicionario!")
