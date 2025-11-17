import os
from urllib.parse import quote_plus

DB_URI = (
    f"postgresql://{os.getenv('DB_USER')}:{quote_plus(os.getenv('DB_PASS'))}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
