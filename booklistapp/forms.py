from django import forms

class FeedbackForm(forms.Form):
    text = forms.CharField()

class PictureForm(forms.Form):
	picture = forms.ImageField(
		label='Select a file',
		help_text='max. 2 megabytes'
)