from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
STATE_CHOICES = (
    ("Maharashtra", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Karnataka", "Karnataka"),
    ("Telangana", "Telangana"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("West Bengal", "West Bengal"),
    ("Gujarat", "Gujarat"),
    ("Maharashtra", "Maharashtra"),
    ("Rajasthan", "Rajasthan"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Gujarat", "Gujarat"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Bihar", "Bihar"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Kerala", "Kerala"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Gujarat", "Gujarat"),
    ("Andhra Pradesh", "Andhra Pradesh")
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    city = models.CharField(max_length = 50)
    state = models.CharField(choices = STATE_CHOICES, max_length = 50)
    zipcode = models.IntegerField()
    locality = models.CharField(max_length = 200, default = 'None')

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW','Top Wear'),
    ('BW', 'Bottom Wear'),
)
class Product(models.Model):
    title = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.CharField(max_length = 2, choices = CATEGORY_CHOICES)
    brand = models.CharField(max_length = 50)
    discription = models.TextField()
    product_image = models.ImageField(upload_to = 'product_image')
 
def __str__(self):
    return str(self.id) 

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return str(self.id) 
    
STATUS_CHOICE = (
    ('Accepted', 'Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Cancle','Cancle'),
)
class OrderedPlaced(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    status = models.CharField(max_length = 50, choices = STATUS_CHOICE, default = 'Pending')
    order_date = models.DateTimeField(auto_now_add = True)