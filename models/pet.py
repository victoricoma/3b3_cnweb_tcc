from dataclasses import dataclass
from datetime import datetime
import users

@dataclass
class Pet:
    id: str
    name: str
    tutor: str
    pet_type:str
    born: datetime
    vaccine_rage: bool
    vaccine_bultose: bool
    vaccine_felve: bool
    vaccine_filv: bool
    created_at: datetime = field(default_factury=datetime.utcnow)