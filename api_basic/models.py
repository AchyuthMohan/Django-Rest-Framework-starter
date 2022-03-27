from tkinter.ttk import Style
from django.db import models
from pygments import highlight
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
class Snippet(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100,blank=True,default=' ')
    code=models.TextField()
    linenos=models.BooleanField(default=False)
    language=models.CharField(choices=STYLE_CHOICES,default='friendly',max_length=100)
    owner=models.ForeignKey('auth.User',related_name='snippets',on_delete=models.CASCADE)
    highlighted=models.TextField()

    def save(self,*args,**kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        super().save(*args, **kwargs)

    class  Meta:
        ordering=['created']