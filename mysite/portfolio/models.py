from django.db import models


class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('Web design', 'Web design'),
        ('Other', 'Other'),
    ]
    title = models.CharField(max_length=25)
    img = models.ImageField(upload_to='pics')
    support_img_1 = models.ImageField(upload_to='pics/support-1')
    support_img_2 = models.ImageField(upload_to='pics/support-2')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Web design')
    client = models.CharField(max_length=100, default='After Nepal')
    project_date = models.DateField()
    project_url = models.URLField(default="")
    description = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.client} - {self.project_date}"

class Blog_Category(models.Model):
    category = models.CharField(max_length=20)
    img = models.ImageField(upload_to='blogs-category')

    def __str__(self):
        return self.category


class Blog(models.Model):
    blog = models.ForeignKey(Blog_Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.TextField()
    imp_description = models.TextField()
    img = models.ImageField(upload_to='my-blog')


    def __str__(self):
        return self.title


class Web_Services(models.Model):
    icon = models.CharField(max_length=220)
    web_service_heading = models.CharField(max_length=50)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    description4 = models.TextField()

    def __str__(self):
        return self.web_service_heading


class Mobile_Services(models.Model):
    icon = models.CharField(max_length=220)
    mobile_service_heading = models.CharField(max_length=50)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    description4 = models.TextField()

    def __str__(self):
        return self.mobile_service_heading

class Desktop_Services(models.Model):
    icon = models.CharField(max_length=220)
    desktop_service_heading = models.CharField(max_length=50)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    description4 = models.TextField()

    def __str__(self):
        return self.desktop_service_heading

class Feedback(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(null=False)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} -- {self.subject}'