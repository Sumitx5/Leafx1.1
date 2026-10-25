import discord, os, config, random, yaml
from discord.ext import commands, tasks

# Config File Location
config_file = "settings/config.yml"
with open(config_file, "r", encoding="utf-8") as file:
    settings = yaml.safe_load(file)

TOKEN = config.Token if config.Token else settings["TOKEN"]
ACTIVITY_MAP = {
    "listening": discord.ActivityType.listening,
    "watching": discord.ActivityType.watching,
    "playing": discord.ActivityType.playing
}

# main loop & prefix
prefix = settings["Prefix"]
activity_loop_time = settings["activity_loop_time"]

# Main Bots Data
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

def botStats(message: str, border = "=" * 40):
    print(f"\n{border}\n  {message}\n{border}\n")

# Activity loop 
@tasks.loop(seconds=activity_loop_time)
async def change_activity():
    members = len(bot.users)
    guilds = len(bot.guilds)

    if settings["random_activities"] == True:
        chosen_type = random.choice(list(settings["activities"].keys()))
        activity_data = settings["activities"][chosen_type]
    else:
        chosen_type = settings.get("activity_type", "playing")
        activity_data = settings["activities"].get(chosen_type)

    if activity_data:
        format_name = activity_data.get("name", "").format(guilds=guilds, members=members)
        format_state = activity_data.get("state", "").format(guilds=guilds, members=members)
        
        activity_obj = discord.Activity(
            type=ACTIVITY_MAP.get(chosen_type, discord.ActivityType.playing),
            name=format_name,
            state=format_state if format_state else None
        )
        await bot.change_presence(status=discord.Status.online, activity=activity_obj)

        if settings["activity_logs_on_console"] == True:
            print(f"| Activity Logs> Updated to - Type: {activity_obj.type.name}, Name: {activity_obj.name}, State: {activity_obj.state if activity_obj.state != None else None}")

@bot.event
async def on_ready():
    bot_name = bot.user.name
    bot_id = bot.user.id

    if bot_name.isascii():
        print(f"Logged in as {bot_name} \nBot ID:{bot_id}")
    else:
        print(f"Logged in With this Bot ID: {bot_id}")

    botStats("Bot Logs> Bot Started Reading Cogs:")
    try:
        for filename in os.listdir("./cmds"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cmds.{filename[:-3]}")
                print(f"| Bot Logs> Loaded cog: {filename[:-3]}")
        print("\t")
    except Exception as e:
        print(f"{e}")
    await bot.tree.sync()
    change_activity.start()
    print("\n| Activity Logs> Activity Changer Initialised")
    botStats("Bot is Fully Online")

if __name__ == "__main__":
    bot.run(TOKEN)
