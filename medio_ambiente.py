import discord
import random
import os
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Activar acceso a la información de los miembros
from discord.ext import commands
bot = commands.Bot(command_prefix='&', intents=intents)

datos_ambientales = [                   #lista
    "El 70 de la Tierra está cubierta de agua.",
    "Los árboles ayudan a limpiar el aire que respiramos.",
    "Reciclar una lata de aluminio ahorra energía para 3 horas de TV.",
    "La deforestación causa gran pérdida de biodiversidad.",
    "Energías renovables son clave para el futuro."
]
    



@bot.command()                                 #datos random
async def dato_aleatorio(ctx):
    dato = random.choice(datos_ambientales)
    await ctx.send(dato)


@bot.command()                                 #preguntas especificas
async def dato_AB(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'como reciclar':
         await ctx.send('Reciclar es sencillo y marca la diferencia. Separa papel, plástico, vidrio y metal en contenedores distintos en casa. Lleva tus propias bolsas al comprar y prefiere envases reciclables. ')
    elif mensaje == 'datos del medio ambiente':
        await ctx.send('Nueve de cada diez personas respiran aire contaminado a nivel mundial.')
    elif mensaje == 'contaminacion del agua':
        await ctx.send('Más del 80 de las aguas residuales a nivel mundial llegan a los mares y océanos sin ser depuradas.')
    else:
        await ctx.send(f'No tengo esa informacion')


@bot.command()                          #imagenes random
async def foto_random(ctx):
    
    nombre_imagen = random.choice(os.listdir('imagenes2'))
    
    with open(f'imagenes2/{nombre_imagen}', 'rb') as f:
      
        picture = discord.File(f)
    
    await ctx.send(file=picture)







token = ''
bot.run(token)