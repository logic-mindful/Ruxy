import discord
import blacklist
from config import MOD_ROLE_ID, ADMIN_ROLE_ID

# only mods and up can use it
# blacklist = can't use the bot
def setup(tree, client):
    @tree.command(
        name="blacklist",
        description="blacklists someone",
    )
    async def blacklist_command(interaction: discord.Interaction, user: discord.Member):
        if not any(role.id in (MOD_ROLE_ID, ADMIN_ROLE_ID) for role in interaction.user.roles):
            await interaction.response.send_message(
                "No permission.",
                ephemeral=True
            )
            return
        if (blacklist.is_blacklisted(user.id)):
            await interaction.response.send_message(user.name + " is already blacklisted")
            return
        
        blacklist.blacklist_user(user.id)


        await interaction.response.send_message(user.name + " has been successfully blacklisted")

    @tree.command(
        name="unblacklist",
        description="Unblacklists someone",
    )
    async def unblacklist_command(
        interaction: discord.Interaction,
        user: discord.Member
    ):
        if not any(role.id in (MOD_ROLE_ID, ADMIN_ROLE_ID)
                for role in interaction.user.roles):
            await interaction.response.send_message(
                "No permission.",
                ephemeral=True
            )
            return

        if not blacklist.is_blacklisted(user.id):
            await interaction.response.send_message(
                f"{user.name} is not blacklisted"
            )
            return

        blacklist.unblacklist_user(user.id)

        await interaction.response.send_message(
            f"{user.name} has been successfully unblacklisted"
        )
