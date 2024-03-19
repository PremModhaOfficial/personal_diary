from django.db import models


# Create your models here.

class Note(models.Model):
    note_name = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date added')
    note_file = models.FileField(upload_to='./uploaded_files')

    def __str__(self):
        return f'{self.note_name}: {self.pub_date}'