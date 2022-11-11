from django.db import models
from django.urls import reverse
# Create your models here.


class MainProducts(models.Model):
     products_image = models.ImageField(upload_to='images')
     ''' product_thumbnail = ImageSpecField(source='products_image',
                            processors=[ResizeToFill(200,200)],
                                  format='PNG', 
                                  options={'quality':60} , blank=True) '''
     products_video = models.FileField(upload_to='images/%y',blank=True)
     product_title = models.CharField(max_length=200)
     product_desc = models.CharField(max_length=600)
     product_spec1 = models.CharField(max_length=600)
     product_spec2 = models.CharField(max_length=600)
     product_spec3 = models.CharField(max_length=600)
     product_price = models.DecimalField(max_digits=7, decimal_places=2)
     
     def _str_(self):
         return self.product_title
 
class Meta:
        verbose_name = ('MainProducts')
        verbose_name_plural = ('MainProducts') 
        
        
        
class FeaturedProducts(models.Model):
      main_products_image = models.ImageField(upload_to='media', blank=True)
      products_image1 = models.ImageField(upload_to='media', blank=True)
      products_image2 = models.ImageField(upload_to='media', blank=True)
      products_image3 = models.ImageField(upload_to='media', blank=True)
      ''' product_thumbnail = ImageSpecField(source='products_image',
                            processors=[ResizeToFill(200,200)],
                                  format='PNG', 
                                  options={'quality':60} , blank=True) '''
      product_title = models.CharField(max_length=200)
      product_desc = models.CharField(max_length=600)
      product_price = models.DecimalField(max_digits=5, decimal_places=2)
     
      def _str_(self):
         return self.product_title
     
      ''' def get_absolute_url(self):
        	 return reverse("home:shop", kwargs={"pk": self.pk}) '''
 
 
class Meta:
        verbose_name = ('FeaturedProducts')
        verbose_name_plural = ('FeaturedProducts') 
