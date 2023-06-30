from typing import Dict, List

from pydantic import BaseModel


class Cargo(BaseModel):
    cargo_type: str
    rate: float


class InputData(BaseModel):
    data: Dict[str, List[Cargo]]

    class Config:
        schema_extra = {
            "example":
                {
                    "data": {
                        "2022-12-12": [
                            {
                                "cargo_type": 'Glass',
                                "rate": 0.123
                            }
                        ]
                    }
                }
        }
