import dataclasses as s

@s.dataclass
class ProductDAO:
    codProdotto: str
    unitCost: float
    unitPrice: float
    productType: str