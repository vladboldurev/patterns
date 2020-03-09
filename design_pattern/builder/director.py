from builder import Builder


class Director:

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def simple_config(self):
        self._builder.product_part_a()

    def advanced_config(self):
        self._builder.product_part_a()
        self._builder.product_part_b()
        self._builder.product_part_c()