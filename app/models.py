from django.db import models
import os
import datetime
from ckeditor.fields import RichTextField

# Create your models here.


def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)


class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-Show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    sub_category_of = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-Show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_of = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    front_image = models.ImageField(
        upload_to=getFileName, null=True, blank=True)
    left_image = models.ImageField(
        upload_to=getFileName, null=True, blank=True)
    right_image = models.ImageField(
        upload_to=getFileName, null=True, blank=True)
    back_image = models.ImageField(
        upload_to=getFileName, null=True, blank=True)
    price = models.CharField(max_length=6, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    specification = RichTextField(blank=True, null=True)
    additionalinfo = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-Show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Awards(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name


class Messages(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=10)
    message = models.TextField(max_length=500)


class Testimonial(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    person_image = models.ImageField(
        upload_to=getFileName, null=True, blank=True)
    person_name = models.CharField(max_length=50, null=False, blank=False)
    person_review = models.TextField(max_length=500)
    person_role_company = models.CharField(
        max_length=50, null=False, blank=False)
