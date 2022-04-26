from django import forms
from .models import SingleSeat

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = SingleSeat
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm,self).__init__(*args,**kwargs)
        self.fields['train_number'].disabled= True
        self.fields['train_car_number'].disabled= True
        self.fields['trip_number'].disabled= True
        self.fields['NumberSeat'].disabled= True
        self.fields['price'].disabled= True
        self.fields['SS_date'].disabled= True
        self.fields['SS_time'].disabled= True
        self.fields['SS_source'].disabled= True
        self.fields['SS_destination'].disabled= True
