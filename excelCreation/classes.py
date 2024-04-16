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

@dataclass
class ExamTariffesSpreadsheet:
    id_exam : str
    name_exam : str
    id_tariff : str
    name_tariff : str
    price : float

