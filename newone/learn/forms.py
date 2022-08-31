from django import forms


class Answer(forms.Form):
    aswer = forms.CharField(label="answer", max_length=200, required=True, initial="Write Answer Here")

# class Form(forms.ModelForm):
#     class Media:
#         js = 