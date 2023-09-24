import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from products.models import Product, Brand, Review
import random
from faker import Faker

def add_brands(n):
    fack = Faker()
    images = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    for x in range(n):
        Brand.objects.create(
            name = fack.name(),
            image = f"brands/{images[random.randint(0,9)]}"
        )
    print(f"{n} brands was created successfully" )


def add_products(n):
    pass



def add_reviews(n):
    pass



add_brands(50)

