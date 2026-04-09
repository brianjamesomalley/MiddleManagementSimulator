import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
   #LLM
   DEEPSEEK_API_KEY =
   os.environ.get("DEEPSEEK_API_KEY")
      LLM_MODEL =
      os.environ.get("LLM_MODEL", "deepseek-chat")

      # Database
      DATABASE_URL = 
      os.enviorn.get("DATABASE_URL", postgresql://localhost/burger_rohyale")

      # Game
      COWARDICE_THRESHOLDS = {
           "Store Manager": 0,
           "Regional Supervisor": 25,
           "VP of People Operations": 50,
           "Executive": 75
           }

           #Redis
           REDIS_URL =
      os.environ.get("REDIS_URL", "redis://localhost: 6739")

        #Analytics
        ANALYTICS_ENABLED =
      os.environ.get("ANALYTICS_ENABLED" , "true").lower() == "true"
      settings = Settings()
