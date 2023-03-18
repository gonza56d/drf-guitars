from django.db import models


class AuditedModel(models.Model):
    """Inherit auditory fields."""

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


class NamedModel(AuditedModel):
    """Inherit unique name field and auditory fields."""

    name = models.CharField(
        max_length=300,
        unique=True,
        error_messages={'unique': 'Nombre duplicado.'}
    )
    hidden = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        try:
            self.name = self.name.upper()
        except AttributeError:
            pass
        return super().save(*args, **kwargs)

    class Meta(AuditedModel.Meta):
        abstract = True
        ordering = ['name', '-created', '-modified']
