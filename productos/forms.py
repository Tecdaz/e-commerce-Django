from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='titulo', max_length=50)
    gender = forms.CharField(label='genero', max_length=50, required=False)
    category = forms.CharField(label='categoria', max_length=50)
    subCategory = forms.CharField(
        label='subcategoria', max_length=50, required=False)
    productType = forms.CharField(
        label='tipo de producto', max_length=50, required=False)
    colour = forms.CharField(label='color', max_length=50)
    pruductUsage = forms.CharField(
        label='uso del producto', max_length=50, required=False)
    imageURL = forms.CharField(label='url de la imagen', max_length=255)

    def save(self):
        Product.objects.create(
            title=self.cleaned_data['title'],
            gender=self.cleaned_data['gender'],
            category=self.cleaned_data['category'],
            subCategory=self.cleaned_data['subCategory'],
            productType=self.cleaned_data['productType'],
            colour=self.cleaned_data['colour'],
            pruductUsage=self.cleaned_data['pruductUsage'],
            imageURL=self.cleaned_data['imageURL']
        )
