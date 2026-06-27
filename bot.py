import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from ai import ask_ai

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


@bot.event
async def on_ready():
    print("=" * 50)
    print(f"Logged in as {bot.user}")
    print(f"ID: {bot.user.id}")
    print("NG AI Agent is ONLINE")
    print("=" * 50)


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions:
        await message.reply(
            "👋 Hello! I'm NG AI Agent.\n"
            "Use **!help** to see available commands."
        )

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! `{round(bot.latency * 1000)} ms`")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention} 👋")


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="NG AI Agent",
        description="Discord AI Agent",
        color=0x5865F2,
    )

    embed.add_field(name="Version", value="1.0")
    embed.add_field(name="Python", value="3.x")
    embed.add_field(name="discord.py", value="2.x")

    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Commands",
        color=0x57F287,
    )

    embed.add_field(name="!ping", value="Check latency", inline=False)
    embed.add_field(name="!hello", value="Greeting", inline=False)
    embed.add_field(name="!info", value="Bot information", inline=False)

    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions:
        await message.reply(
            "👋 Hello! I'm NG AI Agent.\n"
            "Use !help to see available commands."
        )

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! {round(bot.latency * 1000)} ms")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention} 👋")


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="NG AI Agent",
        description="Discord AI Agent",
        color=0x5865F2
    )

    embed.add_field(name="Version", value="1.0", inline=False)
    embed.add_field(name="Developer", value="Nanang", inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="NG AI Agent Commands",
        color=0x57F287
    )

    embed.add_field(name="!ping", value="Check bot latency", inline=False)
    embed.add_field(name="!hello", value="Say hello", inline=False)
    embed.add_field(name="!info", value="Bot information", inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def uptime(ctx):
    await ctx.send("🟢 NG AI Agent is running.")


@bot.command()
async def invite(ctx):
    await ctx.send("Invite link coming soon.")


@bot.command()
async def server(ctx):
    guild = ctx.guild
    await ctx.send(
        f"**{guild.name}**\n"
        f"Members: {guild.member_count}"
    )


@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.display_avatar.url)


@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author

    embed = discord.Embed(
        title=str(member),
        color=0x5865F2
    )

    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Display Name", value=member.display_name, inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def ask(ctx, *, question):
    await ctx.send("🧠 Thinking...")

    answer = ask_ai(question)

    await ctx.send(answer)

bot.run(TOKEN)