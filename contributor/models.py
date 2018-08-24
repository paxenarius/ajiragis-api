from django.db import models
from django.core.validators import FileExtensionValidator
from django.forms import ValidationError
from django.conf import settings

from translation.models import Language


class Data(models.Model):
  """
  Data model responsible for receiving data input from contributor. The data can be either text file or
  """
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
  language = models.ForeignKey(Language, on_delete=models.PROTECT)
  text = models.TextField(blank=True, null=True)
  file = models.FileField(
      blank=True,
      null=True,
      validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])],
      verbose_name='File: (Only pdf, docx or doc files with a maximum size of 2MB are allowed.)',
  )
  approved = models.BooleanField(default=False)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created',)

  def save(self, **kwargs):
    self.clean()
    return super().save(**kwargs)

  def clean(self):
    if self.text and self.file:
      raise ValidationError('Provide only either text or file')
    if not self.text and not self.file:
      raise ValidationError('Enter text or select file to upload')

  def __str__(self):
    return self.language.name