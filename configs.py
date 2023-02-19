from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:AdDfgFRFVVfDEhdhyjjvjjftSEW")
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://a:a@cluster0.x6vmjau.mongodb.net/?retryWrites=true&w=majority")
    

cfg = Config()
