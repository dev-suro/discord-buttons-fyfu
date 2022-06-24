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
    
    @slash.slash(name="farben", guild_ids=[guild_id])
    async def role_buttons(ctx: SlashContext):
        """Handle role buttons

        Args:
            ctx (SlashContext): [description]
        """

        # Define role buttons
        buttons = [
            # Add first role
            create_button(
                style=ButtonStyle.grey,
                label='Grau',
                emoji=get(ctx.guild.emojis, id = int(893156674469261323)),

                # custom_id must be set to roleID!!!
                custom_id='887833048853397524'
            ),

            # Add second role
            create_button(
                style=ButtonStyle.grey,
                label='Grün',
                emoji=get(ctx.guild.emojis, id = int(893156674431500348)),

                # custom_id must be set to roleID!!!
                custom_id='797552919092133929'
            ),
            
            create_button(
                style=ButtonStyle.grey,
                label='Gelb',
                emoji=get(ctx.guild.emojis, id = int(893156674431516702)),

                # custom_id must be set to roleID!!!
                custom_id='797553111321280552'
            ),

            create_button(
                style=ButtonStyle.grey,
                label='Rot',
                emoji=get(ctx.guild.emojis, id = int(893156674846732358)),

                # custom_id must be set to roleID!!!
                custom_id='797553536237305867'
            ),

            create_button(
                style=ButtonStyle.grey,
                label='Violett',
                emoji=get(ctx.guild.emojis, id = int(893156674544754738)),

                # custom_id must be set to roleID!!!
                custom_id='797553832392917002'
            ),
        ]
        action_row = create_actionrow(*buttons)

        # Message to appear above the buttons
        embed = Embed(
            title=":art: Farbauswahl :art:",
            description="> • Mit den Knöpfen unter dieser Nachricht kannst du zwischen verschiedenen farbigen Rollen wählen, dazu musst du nur auf den entsprechenden Knopf drücken.\n\n> • Um eine bestimmte Farbe wieder abzuwählen, drücke erneut auf den entsprechenden Knopf unter dieser Nachricht.",
            color=Colour.from_rgb(*get_rgb_from_hex('2f3136')))
        await ctx.send(embed = embed, components=[action_row])
