import jwt
from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_config

class JWTHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(hours=jwt_config["EXP_HOURS"]),
                **body
            },
            key=jwt_config["KEY"],
            algorithm=jwt_config["ALGORITHM"]
        )
        return token
    
    def decode_jwt_token(self, token: str) -> dict:
        token_info = jwt.decode(
            token,
            key=jwt_config["KEY"],
            algorithms=[jwt_config["ALGORITHM"]]
        )
        return token_info
