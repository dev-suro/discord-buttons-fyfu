from discord import Embed, Colour
from discord.utils import get
from discord_slash import SlashContext
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from utilities import get_rgb_from_hex

def register(slash, guild_id):
    """Register the command

    Args:
        slash ([type]): [description]
        guild_id ([type]): [description]
    """
    
    @slash.slash(name="halloween", guild_ids=[guild_id])
    async def role_buttons(ctx: SlashContext):
        """Handle role buttons

        Args:
            ctx (SlashContext): [description]
        """

        # Define role buttons
        buttons = [
            # Add first role
            create_button(
                style=ButtonStyle.red,
                label='Halloween',
                emoji='🎃',

                # custom_id must be set to roleID!!!
                custom_id='893149008166543380'
            )
        ]
        action_row = create_actionrow(*buttons)

        # Message to appear above the buttons
        embed = Embed(
            title="🎃 Zeitlich limitierte Event Rolle 🎃",
            description="**Hole dir die schaurige limitierte Halloween Rolle. **\n\n> • Mit dem Knopf unter dieser Nachricht kannst du die Event Rollen wählen.\n\n> • Um die Rolle wieder abzuwählen, drücke erneut auf den entsprechenden Knopf unter dieser Nachricht.",
            color=Colour.from_rgb(*get_rgb_from_hex('2f3136')))
        embed.set_image(url="https://cdn.discordapp.com/attachments/892813927711400036/893161680111017985/Spokipng.png")
        await ctx.send(embed = embed, components=[action_row])
