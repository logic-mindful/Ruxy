from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

BLACKLIST_FILE = "../blacklist.txt"

OWNERS = {
    1318991936455053464,  # Alex
    1508944026781483139,  # Nathan
    288063589179326464    # Ivan
}

MOD_ROLE_ID = 1509981231775748196
ADMIN_ROLE_ID = 1509989094132940880
