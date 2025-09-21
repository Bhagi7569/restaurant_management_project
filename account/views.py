from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

        def __str__(self):
                return self.nameimport secrets
                import string
                from .models import Coupon  # Assuming you have a Coupon model

                def generate_coupon_code(length=10):
                    """Generate a unique alphanumeric coupon code."""
                        while True:
                                code = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(length))
                                        if not Coupon.objects.filter(code=code).exists():
                                                    return code