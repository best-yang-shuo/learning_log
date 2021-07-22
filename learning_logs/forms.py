from django import forms
from .models import Topic,Entry
'''创建类别表单'''
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['text']
        labels={'text':''}

'''创建条目'''
class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=["text"]
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}
