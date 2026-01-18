
class Config:
   ENVIROMENTS = {
       "prod": "https://www.twitch.tv",
   }

   @classmethod
   def base_url(cls, env="prod"):
       return cls.ENVIROMENTS[env]