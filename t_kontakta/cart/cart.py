from decimal import Decimal
from django.conf import settings
from core.models import Tires


"""
changed:
    cart on basket - everywhere
    product.id on product.vencode
    product_id on product_vencode
    product_ids on product_vencodes in method __iter__
"""

class Cart(object):

    def __init__(self, request):
        """
        Initialization cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add product in cart & update quantity
        """
        product_vencode = str(product.vencode)
        if product_vencode not in self.cart:
            self.cart[product_vencode] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_vencode]['quantity'] = quantity
        else:
            self.cart[product_vencode]['quantity'] += quantity
        self.save()

    def save(self):
        # Updating session basket
        self.session[settings.CART_SESSION_ID] = self.cart
        # Check session as changed, for sure that it saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove product from basket
        """
        product_vencode = str(product.vencode)
        if product_vencode in self.cart:
            del self.cart[product_vencode]
            self.save()

    def __iter__(self):
        """
        Iteration elements in basket & get products from db
        """
        product_vencodes = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Tires.objects.filter(vencode__in=product_vencodes)
        for product in products:
            self.cart[str(product.vencode)]['product'] = product


        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Counting all products inside basket
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Counting summary price in basket
        """
        return sum(
            Decimal(item['price']) * item['quantity'] for item in
            self.cart.values())

    def clear(self):
        # clear basket from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True