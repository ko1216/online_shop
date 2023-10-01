from django import forms

from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, forms.ModelForm):
    banned_data = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'products_image', 'category', 'price',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for banned_word in self.banned_data:
            if banned_word in cleaned_data:
                raise forms.ValidationError('Этот продукт запрещен!')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for banned_word in self.banned_data:
            if banned_word in cleaned_data:
                raise forms.ValidationError('Этот продукт запрещен!')

        return cleaned_data


#  Временно убрал Миксин на стиль для второй формы, так как этот стиль убирает возможность выбора активации версии
class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = ('name', 'version', 'is_active',)

    # def clean_version_status(self):
    #     cleaned_data = self.cleaned_data.get('is_active')
    #     is_active_filter = Version.objects.filter(is_active=True)
    #     is_active_count = []
    #     for object in is_active_filter:
    #         is_active_count.append(object)
    #     if
    #         raise forms.ValidationError('Активная версия для продукта должна быть только одна, снимите галочку на текущей версии и попробуйте заново')
    #
    #     return cleaned_data

