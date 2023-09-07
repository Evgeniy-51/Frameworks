from django.db import models
from django.urls import reverse


class Women(models.Model):  # 1 экземпляр == 1 строка БД
    # id  создается по дефолту
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     age = models.IntegerField()

# class Order(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)