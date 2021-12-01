from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Promotion

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    details = models.ManyToManyField(Product, through='OrderDetails')
    details2 = models.ManyToManyField(Promotion, through='OrderDetails')
    is_finished = models.BooleanField()

    def __str__(self):
        return 'User: '+ self.user.username + ', Order id: ' + str(self.id)

class OrderDetails(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE, null=True, blank=True)
    promotion = models.ForeignKey(Promotion , on_delete=models.CASCADE, null=True, blank=True )
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6 , decimal_places = 2)


    def __str__(self):
        return 'User: ' + self.order.user.username + ', Product: ' + self.product.name + ', Order id: ' + str(self.id)

    class Meta:
        ordering=['-id']
