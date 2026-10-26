from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    uid: str
    name: str
    email: str
    created_at: datetime = field(default_factury=datetime.utcnow)