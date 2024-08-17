import discord
from discord.ext import commands

bot_name = "Enli"


client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Enli V1"))
    print(f'{bot_name}: I am running smooth as pie')


@client.event
async def on_member_join(member):
    print(f'{bot_name}:{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f"{bot_name}:{member} has left a server")


@client.command()
async def devtest(ctx):
    await ctx.send("The bot command Works just fine!")
    
@client.command()
async def clearscreen(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print(f'{member} has been banned for {reason}')  

@client.command()
async def helpEnli(ctx):
    await ctx.send(f"//English\\")
    await ctx.send(f"{bot_name}: Hi there i'm Enli and these are my commands:")
    await ctx.send(f"{bot_name}: .helpEnli: This gives you my command sheet")
    await ctx.send(f"{bot_name}: .clearscreen: this clears the top 3 msgs above ")
    await ctx.send(f"{bot_name}: for the time being these are the only commands avalivable for members more commands wil follow")
    await ctx.send("//Dutch/Nederlands\\")
    await ctx.send(f"{bot_name}: hey ik ben Enli en dit zijn mijn commands:")
    await ctx.send(f"{bot_name}: .helpEnli: dit geeft mijn commands weer")
    await ctx.send(f"{bot_name}: .clearscreen: dit verwijderd de 3 berichten boven je")
    await ctx.send(f"{bot_name}: tot nu toe zijn dit de enige commands beschikbaar voor leden meer commands volgen")
    
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print(f'{member} has been kicked for {reason}') 



@client.command()
async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('8')

        for ban_entry in banned_users:
            user =  ban_entry.user

            if (user.name, user.discriminator) == (member.name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                print(f'Unbanned {user.name}#{user.discriminator}')
                return



client.run('#youre bot token')import discord
from discord.ext import commands

bot_name = "Enli"


client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Enli V1"))
    print(f'{bot_name}: I am running smooth as pie')


@client.event
async def on_member_join(member):
    print(f'{bot_name}:{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f"{bot_name}:{member} has left a server")


@client.command()
async def devtest(ctx):
    await ctx.send("The bot command Works just fine!")
    
@client.command()
async def clearscreen(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print(f'{member} has been banned for {reason}')  

@client.command()
async def helpEnli(ctx):
    await ctx.send(f"//English\\")
    await ctx.send(f"{bot_name}: Hi there i'm Enli and these are my commands:")
    await ctx.send(f"{bot_name}: .helpEnli: This gives you my command sheet")
    await ctx.send(f"{bot_name}: .clearscreen: this clears the top 3 msgs above ")
    await ctx.send(f"{bot_name}: for the time being these are the only commands avalivable for members more commands wil follow")
    await ctx.send("//Dutch/Nederlands\\")
    await ctx.send(f"{bot_name}: hey ik ben Enli en dit zijn mijn commands:")
    await ctx.send(f"{bot_name}: .helpEnli: dit geeft mijn commands weer")
    await ctx.send(f"{bot_name}: .clearscreen: dit verwijderd de 3 berichten boven je")
    await ctx.send(f"{bot_name}: tot nu toe zijn dit de enige commands beschikbaar voor leden meer commands volgen")
    
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print(f'{member} has been kicked for {reason}') 



@client.command()
async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('8')

        for ban_entry in banned_users:
            user =  ban_entry.user

            if (user.name, user.discriminator) == (member.name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                print(f'Unbanned {user.name}#{user.discriminator}')
                return



client.run('#youre bot token')
