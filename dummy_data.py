import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from products.models import Categories, Product, ProductImages, Reviews


def seed_brand(n):
    fake = Faker()
    for _ in range(n):
        Categories.objects.create(
            title = fake.name(),
        )

    print(f"Seed {n} Categories Successfully")


def seed_product(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg', '22.jpg']
    size = ['XL', 'XXL', 'XXXL']
    color = ['Red', 'Black', 'White', 'Blue']
    additional_information = ['Weight 0.79 kg - Dimensions 110 x 33 x 100 cm - Materials 60% cotton', 'Weight 0.62 kg - Dimensions 80 x 31 x 100 cm - Materials 30% cotton']




    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f'products/{images[random.randint(0,21)]}',
            # flag = flags[random.randint(0, 2)],
            size = size[random.randint(0, 2)],
            color = color[random.randint(0, 3)],
            additional_information = additional_information[random.randint(0,1)],
            price = round(random.uniform(20.99, 99.99),2),
            sku = random.randint(1000,100000) ,
            # rate = random.randint(0,4) ,
            subtile = fake.text(max_nb_chars=250),
            description = fake.text(max_nb_chars=1000),
            quantity = random.randint(0,30),
            categore = Categories.objects.get(id=random.randint(1,10)),

        )

    print(f"Seed {n} Products Successfully")


def seed_product_images(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg']
    for _ in range(n):
        ProductImages.objects.create(
            product = Product.objects.get(id=random.randint(1,1020)),
            image = f'product_images/{images[random.randint(0,20)]}'
        )

    print(f"Seed {n} images in product Successfully")


def seed_reviews(n):
    fake = Faker()
    for _ in range(n):
        Reviews.objects.create(
            product = Product.objects.get(id=random.randint(1,1100)),
            rate = random.randint(0,4) , 
            review = fake.text(max_nb_chars=250), 
        )

    print(f"Seed {n} Reviews Successfully")


seed_product_images(1000)