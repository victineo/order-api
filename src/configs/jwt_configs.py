from dotenv import load_dotenv
import os

load_dotenv()

jwt_config = {
    "KEY": os.getenv("JWT_KEY"),
    "ALGORITHM": os.getenv("JWT_ALGORITHM"),
    "EXP_HOURS": int(os.getenv("JWT_EXP_HOURS"))
}
