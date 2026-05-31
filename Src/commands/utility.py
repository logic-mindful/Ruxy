import discord
import blacklist

def setup(tree, client):
    @tree.command(
        name="ping",
        description="Replies with pong"
    )
    async def ping(interaction: discord.Interaction):
        if (blacklist.is_blacklisted(interaction.user.id)):
            await interaction.response.send_message("You are blacklisted")
            return
        latency = round(client.latency * 1000)

        await interaction.response.send_message(
            f"Pong!\n"
            f"took `{latency}ms`"
        )