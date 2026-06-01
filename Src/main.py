import discord
from discord import app_commands
from config import TOKEN

from commands import utility
from commands import user
from commands import github
from commands import owner
from commands import moderation
from commands import fun

class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.synced = False

    async def on_ready(self):
        print(f"Logged in as {self.user}")

        if not self.synced:
            for guild in self.guilds:
                try:
                    tree.copy_global_to(guild=guild)

                    synced = await tree.sync(
                        guild=guild
                    )

                    print(
                        f"Instantly synced {len(synced)} command(s) "
                        f"to guild: {guild.name}"
                    )

                except Exception as e:
                    print(
                        f"Failed to sync to guild "
                        f"{guild.name}: {e}"
                    ) 

            self.synced = True


intents = discord.Intents.default()

client = Client(
    intents=intents
)

tree = app_commands.CommandTree(client)

utility.setup(tree, client)
user.setup(tree, client)
github.setup(tree, client)
owner.setup(tree, client)
moderation.setup(tree, client)
fun.setup(tree, client)

client.run(TOKEN)