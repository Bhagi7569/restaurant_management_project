# models.py
from django.db import models

class Feedback(models.Model):
    comment = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

            def __str__(self):
                    return f"Feedback from {self.created_at}"
                    # forms.py
                    from django import forms
                    from .models import Feedback

                    class FeedbackForm(forms.ModelForm):
                        class Meta:
                                model = Feedback
                                        fields = ['comment']
                                                widgets = {
                                                            'comment': forms.Textarea(attrs={'placeholder': 'Leave your feedback here...'}),
                                                                    }
                # views.py
                from django.shortcuts import render, redirect
                from .forms import FeedbackForm

                def leave_feedback(request):
                    if request.method == 'POST':
                            form = FeedbackForm(request.POST)
                                    if form.is_valid():
                                                form.save()
                                                            return redirect('feedback_thankyou')
                                                                else:
                                                                        form = FeedbackForm()
                                                                            return render(request, 'leave_feedback.html', {'form': form})

                                                                            def feedback_thankyou(request):
                                                                                return render(request, 'feedback_thankyou.html')