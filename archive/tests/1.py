def something(*args):
    print(type(args))
    for n in args:
        print(f"   n:{n}")

    print(f"args[1] {args[1]}" )


something(1,2,3,4)

something(1,2)

print("--------------------------------")


def something2(**kwargs):
    print(type(kwargs))

    for k,v in kwargs.items():
        print(f"   key:{k}, value: {v}")

    print(kwargs["add"])


something2(add=3, multiply = 5)

print("--------------------------------")

def something3(n , **kwargs):
    print(type(kwargs))

    for k,v in kwargs.items():
        print(f"   key:{k}, value: {v}")

    print(kwargs["add"])

something3(2 , add=11, multiply = 22)

print("--------------------------------")

class Product:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.manufacturer = kwargs["manufacturer"]
        # self.barcode = kwargs.["barcode"] -> Error
        self.barcode = kwargs.get("barcode")

prod1 = Product(name = "Pepsi" , manufacturer = "Pepsico")

print(f"prod1.name: {prod1.name}, prod1.manufacturer: {prod1.manufacturer}, prod1.barcode: {prod1.barcode}")