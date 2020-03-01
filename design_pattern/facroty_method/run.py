from creator import Creator, Creator1, Creator2


def client_code(creator: Creator) -> None:
    print(creator.some_operation())


if __name__ == "__main__":
     creator1 = Creator1()
     creator2 = Creator2()

     client_code(creator1)
     client_code(creator2)