from django.db import models
from toolkit.models import CCEAuditModel


class ElectionYear(CCEAuditModel):
    year = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return self.year
        #return u'%s' % self.year

    def can_update(self, user_obj):
        return True

    def can_delete(self, user_obj):
        return user_obj.is_staff or self.created_by == user_obj

    def can_create(self, user_obj):
        return True

    def can_view_list(self, user_obj):
        return True

    def can_view(self, user_obj):
        return True


class Tag(CCEAuditModel):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    def can_update(self, user_obj):
        return True

    def can_delete(self, user_obj):
        return user_obj.is_staff or self.created_by == user_obj

    def can_create(self, user_obj):
        return True

    def can_view_list(self, user_obj):
        return True

    def can_view(self, user_obj):
        return True


class VideoFormat(CCEAuditModel):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    def can_update(self, user_obj):
        return True

    def can_delete(self, user_obj):
        return user_obj.is_staff or self.created_by == user_obj

    def can_create(self, user_obj):
        return True

    def can_view_list(self, user_obj):
        return True

    def can_view(self, user_obj):
        return True

