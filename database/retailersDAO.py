import dataclasses as s

@s.dataclass
class RetailerDAO:
    codRetailer: str
    type: str
    country: str