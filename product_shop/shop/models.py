from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    """Модель категорий продуктов."""
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.CharField(max_length=200, verbose_name='ULR')
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение')

    class Meta:
        ordering = ['name',]
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """Модель подкатегорий продуктов."""
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='URL')
    image = models.ImageField(upload_to='subcategories/')
    parent_category = models.ForeignKey(Category,
                                        related_name='subcategories',
                                        on_delete=models.CASCADE,
                                        verbose_name='Подкатегория')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель продуктов."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.CASCADE,
                                    related_name='products')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name',]
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name


class Cart(models.Model):
    """Модель корзины продуктов."""
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='shopping_carts',
                             verbose_name='Пользователь')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='shopping_cart')
    amount = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'],
                name='unique_user_product',
            )
        ]
        ordering = ['id']
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'