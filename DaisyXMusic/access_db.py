from DaisyXMusic import config
from DaisyXMusic.database import Database

db = Database(config.MONGODB_URI, config.SESSION_NAME)
