from director import Director
from builder import ConcreteBuilder1

if __name__ == "__main__":

    director = Director()
    concrete_builder_1 = ConcreteBuilder1()
    director.builder = concrete_builder_1

    director.simple_config()
    simple_product = concrete_builder_1.product
    simple_product.list_parts()

    director.advanced_config()
    advanced_product = concrete_builder_1.product
    advanced_product.list_parts()








