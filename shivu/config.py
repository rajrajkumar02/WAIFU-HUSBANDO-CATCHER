class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7809385991"
    sudo_users = "7639271205", "8191247703"
    GROUP_ID = --1002566763639
    TOKEN = "7621110601:AAEDfn2i3mfg9wP-v0dzDohKD_hKb2x4Fak"
    mongo_url = "mongodb+srv://sayanray089:sayanray089@cluster0.zbvi7fx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://envs.sh/Yjd.jpg", "https://envs.sh/Yjd.jpg"]
    SUPPORT_CHAT = "bot_databese"
    UPDATE_CHAT = "bot_databese"
    BOT_USERNAME = "Raiden_waifu_bot"
    CHARA_CHANNEL_ID = "-1002566763639"
    api_id = 20160788
    api_hash = "192838ffc9ddeaf78ef96cb48aec7aa5"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
