# Author: Brandi Cook
# Date: 10/5/2020
# Description: This program is a simulated store. It has members, grocery items, and keeps track of items in cart as
# well as price

"""
For invalid checkouts
"""
class InvalidCheckoutError(Exception):
    pass

class Product:
    """
    Represents a product. Contains methods for
    getting id, title, description, price, and quantity available
    """

    def __init__(self, id, tl, des, pri, qnty):
        self.__id = id
        self.__title = tl
        self.__description = des
        self.__price = pri
        self.__quantity_available = qnty

    def get_product_id(self):
        """
        returns id
        """
        return self.__id

    def get_title(self):
        """
        returns title
        """
        return self.__title

    def get_description(self):
        """
        returns description
        """
        return self.__description

    def get_price(self):
        """
        returns price
        """
        return self.__price

    def get_quantity_available(self):
        """
        returns quantity available
        """
        return self.__quantity_available

    def decrease_quantity(self):
        self.__quantity_available -= 1


class Customer:
    """
    represents a customer. Contains
    methods for getting name, id, whether or not premium member is true, and the cart
    """
    def __init__(self, nm, id, pm):
        self.__name = nm
        self.__account_ID = id
        self.__premium_member = pm
        self.__cart = []

    def get_name(self):
        """
        returns price
        """
        return self.__name

    def get_account_ID(self):
        """
        returns ID
        """
        return self.__account_ID

    def get_cart(self):
        """
        retuns the cart
        """
        return self.__cart

    def is_premium_member(self):
        """
        returns whether or not premium member
        """
        return self.__premium_member

    def add_product_to_cart(self, pid):
        """
        returns premium id
        """
        self.__cart.append(pid)

    def empty_cart(self):
        """
        empties the cart
        """
        self.__cart = []


class Store:
    """
    This class represents a store. It contains methods for
    adding a product, adding a member, getting the product,
    getting the member, searching for products, adding
    products to cart, and checking out members
    """
    def __init__(self):
        """
        initializes and sets inventory and members to a dictionary
        """
        self.__inventory = dict()
        self.__members = dict()

    def add_product(self, prod):
        """
        adds product
        """
        self.__inventory[prod.get_id_code()] = prod

    def add_member(self, mem):
        """
        adds member
        """
        self.__members[mem.get_account_ID()] = mem

    def get_product_from_id(self, id):
        """
        gets product using id code
        """
        for x in self.__inventory:
            if x == id:
                return self.__inventory[x]
            return None

    def get_member_from_id(self, id):
        """
        gets member using id code
        """
        for x in self.__members:
            if x == id:
                return self.__members[x]
            return None

    def product_search(self, src):
        """
        searches for product and returns sorted list
        """
        id_list = []
        for x in self.__inventory:
            tt = self.__inventory[x].get_title()
            des = self.__inventory[x].get_description()
            if src.lower() in tt.lower() or src.lower() in des.lower():
                id_list.append(x)
            return sorted(id_list)

    def add_product_to_member_cart(self, pid, mid):
        """
        adds the product to cart if the product is
        found and in stock and if the member id is confirmed
        """
        if pid not in self.__inventory:
            return "Product ID was not found"
        if mid not in self.__members:
            return "Member ID was not found"
        if self.__inventory[pid].get_quantity_available() > 0:
            self.__members[mid].add_product_to_cart(pid)
            return "Product has been added to cart"
        return "Product is out of stock"

    def check_out_member(self, mid):
        """
        Checks out member calculating the charge
        based on whether or not they are premium.
        Empties cart.
        """
        if mid not in self.__members:
            raise (InvalidCheckoutError())
        charge = 0
        member = self.__members[mid]
        for pid in member.get_cart():
            prod = self.__inventory[pid]
            if prod.get_quantity_available() > 0:
                charge += prod.get_price()
                prod.decrease_quantity()
        member.empty_cart()
        if not member.is_premium_member():
            charge += .07 * charge
        return charge


if __name__ == '__main__':
    p1 = Product("889", "Rodent of unusual size",
                 "when a rodent of the unusual size just won't do", 33.45, 8)
    c1 = Customer("Yinsheng", "QWF", False)
    myStore = Store()
    myStore.add_product(p1)
    myStore.add_member(c1)
    myStore.add_product_to_member_cart("889", "QWF")

    try:
        result = myStore.check_out_member("QWF")
        print("Total Cost: $" + str(result))
    except InvalidCheckoutError:
        print("Member not found, sorry. Please check Member ID")
    finally:
        print("\t::Thanks! Have a nice day::")
