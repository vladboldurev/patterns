from factory import ConcreteFactory1, ConcreteFactory2


def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    product_a.useful_function()
    product_b.useful_function()


if __name__ == '__main__':

    concrete_factory1 = ConcreteFactory1()
    client_code(concrete_factory1)

    concrete_factory2 = ConcreteFactory2()
    client_code(concrete_factory2)