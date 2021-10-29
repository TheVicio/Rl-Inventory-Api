from rl_inventory_api.constants.colors import *
from rl_inventory_api.constants.types import *
from rl_inventory_api.constants.series import *
from rl_inventory_api.constants.certifies import *
from rl_inventory_api.constants.tradeable import *
from dataclasses import dataclass, field
from rl_data_utils.item.abc_item import ABCItem


@dataclass
class Item(ABCItem):
    product_id: int = field(repr=False)
    name: str
    slot: str
    paint: str
    certification: str = field(repr=False)
    certification_value: int = field(repr=False)
    certification_label: str
    quality: str
    crate: str
    tradeable: str
    amount: int
    instance_id: int = field(repr=False)

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_color(self):
        return self.paint

    def set_color(self, color: str):
        self.paint = color

    def set_rarity(self, rarity: str):
        self.quality = rarity

    def get_rarity(self):
        return self.quality

    def get_type(self):
        return self.slot

    def set_type(self, type_: str):
        self.slot = type_

    def get_certified(self):
        return self.certification_label

    def set_certified(self, certified: str):
        self.certification_label = certified

    def get_quantity(self) -> int:
        return int(self.amount)

    def set_quantity(self, quantity: int):
        self.amount = quantity

    def is_painted(self):
        return self.paint != NONE

    def is_certificate(self):
        return self.certification_label != NONE

    def is_tradeable(self):
        return self.tradeable == TRUE

    def is_non_crate(self):
        return self.crate == NON_CRATE

    def is_ncr(self):
        return self.is_non_crate() and self.is_rare()

    def is_ncvr(self):
        return self.is_non_crate() and self.is_very_rare()

    def is_nci(self):
        return self.is_non_crate() and self.is_import()

    def is_nce(self):
        return self.is_non_crate() and self.is_exotic()

    def is_blueprint(self):
        return self.slot == BLUEPRINT

    def get_product_series(self) -> int:
        from re import search
        result = search(r"\?INT\?TAGame\.ProductSeries\.Series(\d{2,4})\?", self.crate)
        return int(result.group(1))
