from django.db import models
from common.managers.qureyset import SoftDeleteQuerySet


class SoftDeleteManager(models.Manager):
    
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop("alive_only", None)
        super().__init__(*args, **kwargs)

    def get_queryset(self) -> SoftDeleteQuerySet:
        if self.alive_only is True:
            return SoftDeleteQuerySet(self.model).filter(is_deleted=False)
        elif self.alive_only is False:
            return SoftDeleteQuerySet(self.model).filter(is_deleted=True)
        return SoftDeleteQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()