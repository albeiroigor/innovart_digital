import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DATABASE", "InnovartDigital")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
    MYSQL_CHARSET = os.getenv("MYSQL_CHARSET", "utf8mb4")
    MYSQL_INIT_RETRIES = int(os.getenv("MYSQL_INIT_RETRIES", "15"))
    MYSQL_INIT_DELAY = int(os.getenv("MYSQL_INIT_DELAY", "2"))
