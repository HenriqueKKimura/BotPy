import discord
import os
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.Channel.send(f'{message.author.name} as regras do servidor são:{os.linesep}1- Não Desrespeitar os Membros{os.linesep}2- Não Utilizar de Palavrões{os.linesep}3- Não é tolerado Racismo ou qualquer tipo de PRECONCEITO{os.linesep}4- Divirtam-se')
        elif message.content == '?nivel':
            await message.author.send('Nível 1')
    
    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)



client = MyClient(intents=intents)
client.run('Token HERE')