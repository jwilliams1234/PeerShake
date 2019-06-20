from django.db import models
import datetime 

class SearchQuery(models.Model):
    paperTitle = models.CharField(max_length=5000)
    paperAuthors = models.CharField(max_length=5000)
    paperDOI = models.IntegerField()
    paperSubject = models.CharField(max_length=5000)
    def split2(self):
        blank=[]
        pA = str(self.paperAuthors)
        t = 0
        for i in range(len(self.paperAuthors)):
            if pA[i]==';':
                blank.append(pA[t:i])
                t = t+1
        s = pA[t:] if t!=(len(pA)-1) else ''
        blank.append(s)
        return s
    def __str__(self):
        return self.paperTitle

class ChromeExtension(models.Model):
    email = models.EmailField('Email', max_length=100)
    paperTitleCE = models.TextField('Paper Title', default="")
    genComment = models.TextField('General Comments')
    specComment = models.TextField('Specific Comments')
    name = models.CharField('Name', max_length=100, null=True, blank=True)
    url = models.CharField('Url', max_length = 300)
    doi = models.CharField(verbose_name="DOI", max_length=100)
    date = models.DateField(auto_now_add=True, blank = True)

    def __str__(self):
        return 'Title: '+self.paperTitleCE+';'+'Email: '+self.email

