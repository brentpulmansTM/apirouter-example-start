import os
from dotenv import load_dotenv

load_dotenv()

db_connection = os.environ.get('DB_CONNECTION')
cors_origins = os.environ.get("ALLOWED_ORIGINS", "*")
documentation_url = os.environ.get("DOCS_URL", None)