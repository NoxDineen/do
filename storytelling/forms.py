from django import forms

class PlayerForm(forms.ModelForm):
	class Meta:
		model = Player


class StoryForm(forms.Form):
	chapter = forms.CharField(widget=forms.Textarea)


class LetterForm(forms.ModelForm):
	class Meta:
		model = Letter