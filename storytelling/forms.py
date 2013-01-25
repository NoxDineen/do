from django import forms

class PlayerForm(forms.ModelForm):
	class Meta:
		model = Player


class StoryForm(forms.Form)