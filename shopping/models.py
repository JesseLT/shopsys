# coding:utf-8
from django.db import models
from datetime import datetime


# Create your models here.
class Base(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True


# 用户模型
class User(Base):
    pwd = models.CharField(max_length=50, default="88888888")
    email = models.EmailField(unique=True)
    is_exist = models.IntegerField(default=1)

    class Meta:
        db_table = "user"


# 用户具体信息模型
class UserInfo(models.Model):
    SEX = (("M", "male"), ("F", "female"))

    user = models.ForeignKey(User)
    gender = models.CharField(max_length=30, choices=SEX, default="M")
    birthdate = models.DateField()
    home_num = models.CharField(max_length=40)
    phone_num = models.CharField(max_length=40)
    addr = models.CharField(max_length=100)
    addr_backup = models.CharField(max_length=100)
    register_date = models.DateTimeField(auto_now_add=True)
    info = models.TextField()

    class Meta:
        db_table = "userinfo"


# 产品分类模型
class Category(Base):
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


# 品牌分类模型
class Brands(Base):
    class Meta:
        db_table = "brands"

    def __str__(self):
        return self.name


# 产品模型
class Product(Base):
    OBJ = (("M", "MAN"), ("W", "WOMAN"))
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.ForeignKey(Brands)
    is_bestseller = models.BooleanField("设为热卖", default=False)
    is_featured = models.BooleanField("设为推荐", default=False)
    quantity = models.IntegerField(default=1)
    tags = models.CharField(help_text="产品标签，以逗号隔开！", max_length=50)
    desc = models.TextField()
    obj = models.CharField(max_length=20, choices=OBJ)
    edit_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    img = models.ImageField(upload_to="./static/images")

    class Meta:
        db_table = "product_image"


# 产品评论模型
class ProductComment(models.Model):
    prod = models.ForeignKey(Product)
    auth = models.ForeignKey(User)
    content = models.TextField()
    level = models.IntegerField()
    sub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product_comment"
        ordering = ["sub_date"]


# 购物车模型
class Cart(models.Model):
    user = models.ForeignKey(User, unique=False)
    prod = models.ForeignKey(Product, unique=False)
    add_date = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "cart"
        ordering = ["add_date"]


# 订单模型
class Order(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    deal_date = models.DateTimeField(default=datetime.now)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = "order"
        ordering = ["deal_date"]
