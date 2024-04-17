from dataclasses import dataclass

@dataclass
class ExamData:
    id: str
    name: str
    price: float
    tariff_type: str

@dataclass
class Tariff:
    id: str
    name : str
    discountPercentage : int