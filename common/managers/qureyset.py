from django.db import models


class SoftDeleteQuerySet(models.QuerySet):
    
    def delete(self):
        for obj in self:
            obj.delete()
        return

    def hard_delete(self):
        return super().delete()

    def alive(self):
        return self.filter(is_deleted=False)

    def dead(self):
        return self.filter(is_deleted=True)