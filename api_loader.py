import dotenv, os

# TELEGRAM BOT API KEY
try:
    dotenv.load_dotenv()
    AyUSASalesTaxBot_API_KEY = os.getenv("AyUSASalesTaxBot_API_KEY")
except:
    AyUSASalesTaxBot_API_KEY = os.environ.get("AyUSASalesTaxBot_API_KEY")
