from django import forms
from .models import VehicleInstance


class ContactForm(forms.Form):
    subject = forms.CharField()
    e_mail = forms.EmailField(required=False)
    message = forms.CharField


# class AddPostForm(forms.ModelForm):
#     class Meta:
#         model = VehicleInstance
#         fields = ['category', 'brand', 'type', 'price_usd', 'mileage', 'location', 'fuel', 'gearbox',
#                   'engine_capacity', 'description', 'numberplate']
#
# widgets = {
#     'text': forms.Textarea(attrs={'class': 'form-control'}),
#     'rating': forms.Select(attrs={'class': 'form-control'}),
#     'user': forms.Select(attrs={'class': 'form-control'}),
#     'product': forms.Select(attrs={'class': 'form-control'}),
# }


class AddPostForm(forms.ModelForm):
    class Meta:
        model = VehicleInstance
        fields = ['category', 'brand', 'type', 'price_usd', 'mileage', 'location', 'fuel', 'gearbox',
                  'engine_capacity', 'description', 'numberplate']

    def save(self, user):
        obj = super(AddPostForm, self).save(commit=False)
        obj.user = user
        obj.is_active = False

        return obj.save()
