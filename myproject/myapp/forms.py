from django import forms
from .models import Review, Teacher, Subjects, Klass

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Напишите ваш отзыв...',
                'class': 'form-control'
            }),
            'rating': forms.HiddenInput(),  
        }

class TeacherForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Предметы"
    )
    klass = forms.ModelMultipleChoiceField(
        queryset=Klass.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Классы"
    )
    
    class Meta:
        model = Teacher
        fields = ('fio', 'photo', 'description', 'price', 'phone', 'subjects', 'klass')  # ← ДОБАВЛЕНЫ subjects и klass
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }