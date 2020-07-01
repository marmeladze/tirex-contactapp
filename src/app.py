import os
from config import app

class Application:
    def __init__(self, conf):
        self.conf = conf

    def run(self):
        print(self.conf.ROCKETS)
        print(self.conf.SPACE_SHIPS)
        print(self.conf.NAME)
        print(self.conf.DEBUG)
        print(self.conf.FILE_PATH)

env = os.getenv("ENVIRONMENT")
app = Application(app[env])
app.run()