import discord
from discord import app_commands


def setup(tree, client):
    @tree.command(
        name="repo",
        description="Get a link to a Rux repository"
    )
    @app_commands.choices(repository=[
        app_commands.Choice(name="Rux (Compiler)", value="rux"),
        app_commands.Choice(name="Standard Library", value="std"),
        app_commands.Choice(name="Windows Library", value="windows"),
        app_commands.Choice(name="Linux Library", value="linux"),
        app_commands.Choice(name="BSD Library", value="bsd"),
        app_commands.Choice(name="MacOS Library", value="macos"),
        app_commands.Choice(name="Illumos Library", value="illumos"),
        app_commands.Choice(name="Ruxy Bot", value="bot"),
        app_commands.Choice(name="Rux Website", value="website")
    ])
    async def repo(
        interaction: discord.Interaction,
        repository: str = "rux"
    ):
        repos = {
            "rux": "https://github.com/rux-lang/Rux",
            "std": "https://github.com/rux-lang/Std",
            "windows": "https://github.com/rux-lang/Windows",
            "linux": "https://github.com/rux-lang/Linux",
            "bsd": "https://github.com/rux-lang/BSD",
            "macos": "https://github.com/rux-lang/MacOS",
            "bot": "https://github.com/rux-lang/Ruxy-Bot",
            "website": "https://github.com/rux-lang/Web",
            "illumos": "https://github.com/rux-lang/Illumos"
        }

        url = repos.get(repository.lower())

        if url is None:
            await interaction.response.send_message(
                "Unknown repository.",
                ephemeral=True
            )
            return

        view = discord.ui.View()

        view.add_item(
            discord.ui.Button(
                label=f"Open {repository}",
                url=url
            )
        )

        embed = discord.Embed(
            title="Repository",
            description=f"Repository: **{repository}**",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="URL",
            value=url,
            inline=False
        )

        await interaction.response.send_message(
            embed=embed,
            view=view
        )