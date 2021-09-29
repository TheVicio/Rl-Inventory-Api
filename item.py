class Item:
    def __init__(self, product_id, name, slot, paint, certification, certification_value, certification_label, quality,
                 crate, tradeable, amount, instanceid):
        self.product_id = product_id
        self.name = name
        self.slot = slot
        self.paint = paint
        self.certification = certification
        self.certification_value = certification_value
        self.certification_label = certification_label
        self.quality = quality
        self.crate = crate
        self.tradeable = tradeable
        self.amount = amount
        self.instanceid = instanceid

    @staticmethod
    def get_arguments():
        return Item.__init__.__code__.co_varnames[1:]