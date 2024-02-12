import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from products.models import Product, Brand, Review , ProductImages
from django.contrib.auth.models import User
import random
from faker import Faker

def add_brands(n):
    fake = Faker()
    images = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    for x in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f"brands/{images[random.randint(0,9)]}"
        )
    print(f"{n} brands was created successfully" )


def add_products(n):
    fake = Faker()
    images = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    flags = ['Sale','New','Feature']
    for x in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f"product/{images[random.randint(0,9)]}",
            price = round(random.uniform(20.99,99.99),2),
            flag = flags[random.randint(0,2)],
            brand = Brand.objects.get(id=random.randint(1,10)),
            sku = random.randint(1000,1000000),
            subtitle = fake.text(max_nb_chars=200),
            description = fake.text(max_nb_chars=1000),
            quantity = random.randint(5,30),
        )
    print(f"{n} Product was created successfully" )


def add_productimages(n):
    fake = Faker()
    images = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    for x in range(n):
        ProductImages.objects.create(            
            image = f"product_images/{images[random.randint(0,9)]}",
            product = Product.objects.get(id=random.randint(1,100)),
        )
    print(f"{n} ProductImages was created successfully" )



def add_reviews(n):
    fake = Faker()
    for x in range(n):
        Review.objects.create(
            user = User.objects.get(id=random.randint(1,4)),
            product = Product.objects.get(id=random.randint(1,100)),
            review = fake.text(max_nb_chars=200),
            rate = random.randint(1,5),

        )
    print(f"{n} Review was created successfully" )

def add_users(n):
    for x in range(n):
        fake = Faker()
        User.objects.create(
            username = f"user_{x}",
            email = fake.email(),
            password = '12345'
        )









add_users(5)
add_brands(10)
add_products(100)
add_reviews(300)