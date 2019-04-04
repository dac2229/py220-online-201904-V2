""" Furniture class """

from .inventory_class import Inventory


class Furniture(Inventory):
    """ Furniture class """

    def __init__(self, product_code, description,
                 market_price, rental_price, material, size):
        # Creates common instance variables from the parent class
        super().__init__(product_code, description,
                         market_price, rental_price)

        self.material = material
        self.size = size

    def return_as_dictionary(self):
        """ Returns output_dict with contents of self. """
        # output_dict = {}
        output_dict = super().return_as_dictionary()
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
