from django import forms
from app_movies.models import Comment
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ('user', 'email', 'text', 'to_whom', 'captcha')
        # при добавлении капчи для сохранения стилей и передачи данных нужен ренденринг html
        # для этого добавляем widgets и заменяем:
        # <input type="text" class="form-control border" name="user" id="contactusername" required="">
        # на {{ form.user }}
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control border', 'id': "contactusername"}),
            'email': forms.EmailInput(attrs={'class': 'form-control border', 'id': "contactemail"}),
            'text': forms.Textarea(attrs={'class': 'form-control border', "id": "contactcomment", 'rows': '5'})
        }
