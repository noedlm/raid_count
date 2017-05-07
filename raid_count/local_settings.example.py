"""
These are local settings that should not be in github, shared.
"""
import os


# SECURITY WARNING: keep the secret key used in production secret!
os.environ['SECRET_KEY'] = 'fill_in'


os.env['BLIZZARD_WEB_API_URL'] = 'https://us.api.battle.net'
os.env['BLIZZARD_WEB_API_PUBLIC_KEY'] = 'fill_in'
os.env['BLIZZARD_WEB_API_PRIVATE_KEY'] = 'fill_in'
