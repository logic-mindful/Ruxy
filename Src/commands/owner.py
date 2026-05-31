import discord
from discord import app_commands
import os
import sys

from config import OWNERS


def setup(tree, client):
    @tree.command(
        name="shutdown",
        description="Shuts down Ruxy"
    )
    async def shutdown(interaction: discord.Interaction):
        if interaction.user.id not in OWNERS:
            await interaction.response.send_message(
                "You cannot use this command.",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            "Shutting down...",
            ephemeral=True
        )

        await client.close()

    @tree.command(
        name="restart",
        description="Restarts Ruxy"
    )
    async def restart(interaction: discord.Interaction):
        if interaction.user.id not in OWNERS:
            await interaction.response.send_message(
                "You cannot use this command.",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            "Restarting...",
            ephemeral=True
        )

        os.execv(
            sys.executable,
            [sys.executable] + sys.argv
        )

    @tree.command(
        name="sync",
        description="Clears duplicates and syncs commands locally"
    )
    async def sync(interaction: discord.Interaction):
        if interaction.user.id not in OWNERS:
            await interaction.response.send_message(
                "You cannot use this command.",
                ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)

        try:
            global_cmds = tree.get_commands(guild=None)

            for cmd in global_cmds:
                tree.remove_command(
                    cmd.name,
                    guild=None
                )

            await tree.sync(guild=None)

            for cmd in global_cmds:
                tree.add_command(
                    cmd,
                    guild=None
                )

            if interaction.guild is not None:
                tree.copy_global_to(
                    guild=interaction.guild
                )

                synced = await tree.sync(
                    guild=interaction.guild
                )

                await interaction.followup.send(
                    f"Cleared global duplicates and synced {len(synced)} commands locally!"
                )
            else:
                await interaction.followup.send(
                    "Must be run inside a server."
                )

        except Exception as e:
            await interaction.followup.send(
                f"Failed to sync: {e}"
            )