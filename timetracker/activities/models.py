from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Activity(models.Model):
    """
    Represent a single activity.
    """
    sheet = models.ForeignKey(
        'sheets.TimeSheet',
        models.PROTECT,
        related_name='activities',
        verbose_name=_('time sheet'))
    activity = models.CharField(max_length=255, verbose_name=_('activity'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    project = models.ForeignKey(
        'projects.Project',
        models.PROTECT,
        related_name='+',
        verbose_name=_('project'))
    start_datetime = models.DateTimeField(
        default=timezone.now, verbose_name=_('start time'))
    end_datetime = models.DateTimeField(
        blank=True, null=True, verbose_name=_('end time'))

    class Meta:
        verbose_name = _('activity')
        verbose_name_plural = _('activities')
        ordering = ['-start_datetime']

    def __str__(self):
        return _('%(activity)s@%(project)s') % {
            'activity': self.activity,
            'project': self.project,
        }

    @property
    def duration(self):
        """
        Get duration of the activity.
        """
        end_datetime = self.end_datetime or timezone.now()
        return end_datetime - self.start_datetime

    def get_duration_display(self):
        """
        Get duration formatted as a string.
        """
        duration_seconds = self.duration.total_seconds()
        hours = int(duration_seconds / 3600)
        minutes = int((duration_seconds % 3600) / 60)
        return f"{hours} h {minutes} min."

    @property
    def start_date(self):
        """
        Get a date object of a start date without time.
        """
        return self.start_datetime.date()

    def get_absolute_url(self):
        """
        Get a URL to the detail page of this particular object.
        """
        return reverse('activities:detail', args=[self.sheet_id, self.id])

    def is_active(self):
        """
        Check if active is active.
        """
        return self.end_datetime is None

    def stop(self):
        """
        Stop activity if it is active.
        """
        if not self.is_active():
            raise RuntimeError('Activity must be active in order to stop it')
        # If activity is less than a minute, delete it
        self.end_datetime = timezone.now()
        if (self.end_datetime - self.start_datetime) < timezone.timedelta(
                minutes=1):
            self.delete()
            return
        self.save(update_fields=['end_datetime'])
