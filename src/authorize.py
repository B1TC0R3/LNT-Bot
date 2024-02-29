import discord

from config import AUTHORIZED_ROLE_IDS

def has_authorized_role(interaction):
    user_roles    = interaction.user.roles
    user_role_ids = [role.id for role in user_roles]

    for authorized_role in AUTHORIZED_ROLE_IDS:
        if authorized_role in user_role_ids:
            return True

    return False
