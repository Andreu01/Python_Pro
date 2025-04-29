import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Activar acceso a la información de los miembros
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')
    
@bot.command()
async def saludar(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        
        await ctx.send('Hola, ¿cómo estás?')
        
    elif mensaje == 'que onda':
        
        await ctx.send('Todo bien')
    
    elif mensaje == 'klk':
        
        await ctx.send('Todo bien')

@bot.command()
async def despedirse(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'adios':
        
        await ctx.send('Hasta luego')
        
    elif mensaje == 'chao me voy':
        
        await ctx.send('Que Dios te acompañe')
    
    elif mensaje == 'me tengo que ir':
        
        await ctx.send('Chao, estoy disponible cuando lo necesites')

@bot.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
    await ctx.send(msg)

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')





        
token = ''
bot.run(token)