from django import forms
from .models import Question,Choice,Post,GModel
#from formValidationApp.models import *
from django.forms import ModelForm

#from django.db import models

class quesForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = "__all__"
		
class choiceForm(forms.ModelForm):
	class Meta:
		model = Choice
		fields = "__all__"


# define the class of a form 
class PostForm(forms.ModelForm): 
    class Meta: 
        # write the name of models for which the form is made 
        model = Post         
  
        # Custom fields 
        fields =["username", "position", "gender", "text"] 
  
    #this function will be used for the validation 
    def clean(self): 
  
        # data from the form is fetched using super function 
        super(PostForm, self).clean() 
          
        # extract the username and text field from the data 
        username = self.cleaned_data.get('username') 
        text = self.cleaned_data.get('text') 
  
        # conditions to be met for the username length 
        if len(username) < 5: 
            self._errors['username'] = self.error_class([ 
                'Minimum 5 characters required']) 
        if len(text) <10: 
            self._errors['text'] = self.error_class([ 
                'Text Should Contain a minimum of 10 characters']) 
  
        # return any errors if found 
        return self.cleaned_data 




# def validate_G_mail(value): 
#     if "@gmail.com" in value: 
#         return value 
#     else: 
#         raise ValidationError("This field accepts mail id of google only") 

class GForm(forms.ModelForm):
    class Meta:
        model = GModel
        fields = "__all__"

    
       
      
#https://www.geeksforgeeks.org/python-form-validation-using-django/

