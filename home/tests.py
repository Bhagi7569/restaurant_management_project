# cart.py
class Cart:
    def __init__(self, request):
            self.session = request.session
                    cart = self.session.get('cart')
                            if not cart:
                                        cart = self.session['cart'] = {}
                                                self.cart = cart

                                                    def add_item(self, product_id):
                                                            if product_id not in self.cart:
                                                                        self.cart[product_id] = 1
                                                                                else:
                                                                                            self.cart[product_id] += 1
                                                                                                    self.session.modified = True

                                                                                                        def get_item_count(self):
                                                                                                                return sum(self.cart.values())