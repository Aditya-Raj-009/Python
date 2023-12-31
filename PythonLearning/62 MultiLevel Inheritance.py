class Dad:
    basket = 1


class son(Dad):
    dance = 1
    basket = 3

    def isDance(self):
        print(f"yes I dance {self.dance}")


class GrandSon(son):
    dance = 6

    def isDance(self):
        print(f"jackson, I dance very incredibly {self.dance}")


darry = Dad()
larry = son()
harry = GrandSon()

# harry.isDance() # before overriding, this will use son method.

harry.isDance()  # after overriding.
print(harry.basket)  # first this will find data in itself , then in son and last in Dad.
