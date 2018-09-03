from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

#Category Model
class Memory(models.Model):

    name = models.CharField(max_length=200, help_text='Enter a Memory size (e.g. 1Tb,Gbs)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class RAM(models.Model):

    name = models.CharField(max_length=200, help_text='Enter a RAM')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Processor(models.Model):

    name = models.CharField(max_length=200, help_text='Enter a Processor type)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=200,
                            help_text="Enter a the Category(e.g. S,M,L.)")

    def __str__(self):

        return self.name


class Product(models.Model):

    title = models.CharField(max_length=200)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the Product')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    memory = models.ManyToManyField(Memory, help_text='Enter a Memory size')
    ram = models.ManyToManyField(RAM, help_text='Enter a RAM')
    processor = models.ManyToManyField(Processor, help_text='Enter a Processor type')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail',  args=[str(self.id)])#args=[str(self.id)]

    #



class ProductInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular product across whole catalog')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('d', 'Done'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='prdoduct quotation availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.product.title})'


class Brand(models.Model):
    """Model representing an author."""
    brand_name = models.CharField(max_length=100)
    company_name= models.CharField(max_length=100)
    date_of_additon = models.DateField(null=True, blank=True)


    class Meta:
        ordering = ['brand_name', 'company_name']

    def get_absolute_url(self):

        return reverse('brand-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.brand_name}, {self.company_name}'