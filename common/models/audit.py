from auditlog.registry import auditlog
from django.db.models.base import ModelBase


class AuditLogModelBase(ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs):
        new_class = super().__new__(cls, name, bases, attrs, **kwargs)
        if not new_class._meta.abstract:
            auditlog.register(new_class)
        return new_class