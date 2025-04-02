import dataclasses as s
import datetime

@s.dataclass
class VenditeDAO:
    codProdotto: str
    codRetailer: str
    date: datetime.date
    quantity: float
    unitPrice: float
    unitSaledPrice: float