from django.db import models

venderFlag_sizes = ((0, 'customer'), (1, 'vendor'))
status_sizes = (('p', 'pending'), ('h', 'hold'), ('s', 'shipped'), ('c', 'cancelled'))
cancelledPerson_sizes = (('c', 'customer'), ('v', 'vendor'))

# Create your models here.
class product(models.Model):
    pid = models.CharField(max_length=10, primary_key=True)
    pname = models.CharField(max_length=15)
    brand = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail_image = models.BinaryField()
    class Meta:
        db_table = 'product_info'


class properties(models.Model):
    pid = models.OneToOneField(product, on_delete=models.CASCADE, primary_key=True)
    author = models.CharField(max_length=15)
    numPage = models.IntegerField()
    publisher = models.CharField(max_length=15)

    class Meta:
        db_table = 'properties_info'

class account(models.Model):
    aid = models.CharField(max_length=10, primary_key=True)
    aname = models.CharField(max_length=15)
    eaddress = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    saddress = models.CharField(max_length=50)
    venderFlag = models.IntegerField(choices=venderFlag_sizes)

    class Meta:
        db_table = 'account_info'


class shopcartRecord(models.Model):
    pid = models.ForeignKey(product, on_delete=models.CASCADE)
    aid = models.ForeignKey(account, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'shopcartRecord_info'
        unique_together = ('pid', 'aid')


class purchOrder(models.Model):
    po = models.CharField(max_length=10, primary_key=True)
    aid = models.ForeignKey(account, on_delete=models.CASCADE)
    pDate = models.DateTimeField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=1, choices=status_sizes)
    specDate = models.DateTimeField()
    cancelledPerson = models.CharField(max_length=1, choices=cancelledPerson_sizes)

    class Meta:
        db_table = 'purchOrder_info'


class dorder(models.Model):
    po = models.ForeignKey(purchOrder, on_delete=models.CASCADE)
    pid = models.ForeignKey(product, on_delete=models.DO_NOTHING)
    rName = models.CharField(max_length=15)
    rAddress = models.CharField(max_length=50)
    rQuentity = models.IntegerField()
    rPrice = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'dorder_info'
        unique_together = ('po', 'pid')

