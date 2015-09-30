from django.db                  import models
from uuslug                     import uuslug
from taggit.managers            import TaggableManager
from django.contrib.auth.models import User
from django_countries.fields    import CountryField
from django.utils.translation   import ugettext_lazy as _

class Product (models.Model):
    sku           = models.SlugField('SKU', unique=True, max_length=50, editable=False)
    name          = models.CharField('Name',default='', max_length=140)
    description   = models.TextField('Description', default='')
    image         = models.ImageField('Main image', blank=True, null=True)
    price         = models.FloatField('Price', default=0.0)
    discount      = models.FloatField('Discount', default=0.0)
    inventory     = models.IntegerField('Inventory', default=0)
    tags          = TaggableManager(blank=True)
    statusChoices = (('IN','In stock'),('OUT','Out of stock'))
    status        = models.CharField('Status', choices=statusChoices, max_length=3, default='OUT')
    date          = models.DateField('Date added', auto_now_add=True)
    updated       = models.DateField('Date updated', auto_now=True)
    order         = models.IntegerField('Order', default=0)
    class Meta:
        ordering  = ['order', 'date', 'sku']
        verbose_name = 'product'
        verbose_name_plural = 'products'
    def __unicode__(self):
        return u'%s' % (self.sku)
    def __str__(self):
        return u'%s' % (self.sku)
    def save(self, *args, **kwargs):
        self.sku = uuslug(self.name, instance=self, slug_field='sku')
        super(Product, self).save(**kwargs)

class ProductImages:
    product      = models.ForeignKey('Product')
    name         = models.CharField('Name',default='', max_length=140)
    image        = models.ImageField('Image')
    order        = models.IntegerField('Order', default=0)
    date         = models.DateField('Date added', auto_now_add=True)
    updated      = models.DateField('Date updated', auto_now=True)
    class Meta:
        ordering = ['order', 'date']
        verbose_name = 'image'
        verbose_name_plural = 'images'
    def __unicode__(self):
        return u'%s' % (self.image.url)
    def __str__(self):
        return u'%s' % (self.image.url)

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    class Meta:
        ordering = ['user']
        verbose_name = 'client'
        verbose_name_plural = 'clients'
    def __unicode__(self):
        return u'%s' % (self.user.username)
    def __str__(self):
        return u'%s' % (self.user.username)

class ShoppingCartProduct(models.Model):
    user     = models.ForeignKey('Client')
    product  = models.ForeignKey('Product')
    cuantity = models.IntegerField()
    class Meta:
        ordering  = ['cuantity',]
        verbose_name = 'shopping cart product'
        verbose_name_plural = 'shopping cart products'
    def __unicode__(self):
        return u'%s' % (self.product.name)
    def __str__(self):
        return u'%s' % (self.product.name)

class Order(models.Model):
    sku               = models.SlugField('SKU', unique=True, max_length=50)
    user              = models.ForeignKey('Client')
    shippingAdress    = models.ForeignKey('Adress',limit_choices_to={'type': 'SHI'}, related_name='shippingAdress')
    billingAdress     = models.ForeignKey('Adress',limit_choices_to={'type': 'BIL'}, related_name='billingAdress')
    items_subTotal    = models.FloatField(_('Items subtotal'))
    shipping_cost     = models.FloatField(_('Shipping cost'))
    taxes_cost        = models.FloatField(_('Taxes costs'))
    total             = models.FloatField(_('Total'))
    shipping_carrier  = models.CharField(_('Shipping carrier'), max_length=50)
    shipping_tracking = models.CharField(_('Shipping tracking numer'), max_length=50)
    date              = models.DateField('Date placed', auto_now_add=True)
    updated           = models.DateField('Date updated', auto_now=True)
    statusChoices     = (('PRO','processing'),('SHI','shipped'),('COM','complete'))
    status            = models.CharField(_('status'), choices=statusChoices, max_length=3, default='PRO')
    class Meta:
        ordering  = ['date', 'sku']
        verbose_name = 'order'
        verbose_name_plural = 'orders'
    def __unicode__(self):
        return u'%s' % (self.sku)
    def __str__(self):
        return u'%s' % (self.sku)

class OrderProduct(models.Model):
    order    = models.ForeignKey('Order')
    product  = models.ForeignKey('Product')
    cuantity = models.IntegerField()
    class Meta:
        ordering  = ['cuantity',]
        verbose_name = 'order product'
        verbose_name_plural = 'order products'
    def __unicode__(self):
        return u'%s' % (self.product.name)
    def __str__(self):
        return u'%s' % (self.product.name)

class Adress(models.Model):
    user           = models.ForeignKey('Client')
    name           = models.CharField('Name',default='', max_length=140)
    typeChoices    = (('BIL','Billing'),('SHI', 'Shipping'))
    type           = models.CharField('Type', choices=typeChoices, max_length=3, default='BIL')
    default        = models.BooleanField()
    firstname      = models.CharField(_('Firstname'), max_length=50)
    lastname       = models.CharField(_('Lastname'), max_length=50)
    adress_line1   = models.CharField(_('Address 1'), max_length=140)
    adress_line2   = models.CharField(_('Address 2'), max_length=140, blank=True)
    city           = models.CharField(_('City'), max_length=50)
    state_province = models.CharField(_('State/Providence'), max_length=50)
    country        = CountryField()
    zipcode        = models.CharField(_('ZIP code'), max_length=32)
    phone_number   = models.CharField(_('Phone number'), max_length=40)
    date           = models.DateField('Date added', auto_now_add=True)
    class Meta:
        ordering = ['default', 'date', 'name']
        verbose_name = 'adress'
        verbose_name_plural = 'adresses'
    def __unicode__(self):
        return u'%s' % (self.name)
    def __str__(self):
        return u'%s' % (self.name)
    def save(self, *args, **kwargs):
        if self.default:
            Adress.objects.filter(default=True,type=self.type,user=self.user).update(default=False)
        super(Adress, self).save(*args, **kwargs)

class Transaction(models.Model):
    order       = models.ForeignKey('Order')
    card        = models.CharField(_('Token'), max_length=50)
