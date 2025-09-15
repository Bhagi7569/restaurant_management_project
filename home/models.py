from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    email = forms.EmailField(
            max_length=100,
                    validators=[EmailValidator()],
                            widget=forms.EmailInput(attrs={'placeholder': 'Your email'})
                                )
                                    message = forms.CharField(
                                            widget=forms.Textarea(attrs={'placeholder': 'Your message'}),
                                                    min_length=10
                                                        )

                                                            def clean_message(self):
                                                                    message = self.cleaned_data['message']
                                                                            if len(message) < 10:
                                                                                        raise forms.ValidationError('Message must be at least 10 characters long.')
                                                                                                return message