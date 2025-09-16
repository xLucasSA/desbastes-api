from pydantic import BaseModel
from typing import Union, List, Dict, Any

class ParamsProps(BaseModel):
    factorS: float = None
    gama: float = None
    beta: float = None
    idade: float = None


class DataSitio(BaseModel):
    diameter: int = None
    freq: int = None


class DataProps(BaseModel):
    numSitio: int
    dataSitio: List[DataSitio]


class BodyProps(BaseModel):
    numDesbastes: int
    numSitios: int
    params: List[ParamsProps]
    percent: float
    data: List[DataProps]


class DesbasteSitioResult(BaseModel):
    diameter: int
    ft: int
    fd: int
    fr: int


class DesbasteResult(BaseModel):
    results: List[DesbasteSitioResult]
    final_items: int
    quant_remove: int