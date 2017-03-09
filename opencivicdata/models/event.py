from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.encoding import python_2_unicode_compatible
from .base import OCDBase, LinkBase, OCDIDField, RelatedBase, MimetypeLinkBase, RelatedEntityBase
from .jurisdiction import Jurisdiction
from .bill import Bill
from .vote import VoteEvent


EVENT_STATUS_CHOICES = (
    ('cancelled', 'Cancelled'),
    ('tentative', 'Tentative'),
    ('confirmed', 'Confirmed'),
    ('passed', 'Passed'),
)


class EventMediaBase(RelatedBase):
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=10, blank=True)    # YYYY[-MM[-DD]]
    offset = models.PositiveIntegerField(null=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class EventLocation(RelatedBase):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, max_length=2000)
    coordinates = models.PointField(null=True)
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='event_locations')

    objects = models.GeoManager()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Event(OCDBase):
    id = OCDIDField(ocd_type='event')
    name = models.CharField(max_length=300)
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='events')
    description = models.TextField()
    classification = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    timezone = models.CharField(max_length=300)
    end_time = models.DateTimeField(null=True)
    all_day = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES)
    location = models.ForeignKey(EventLocation, null=True)

    def __str__(self):
        return self.name

    class Meta:
        index_together = [
            ['jurisdiction', 'start_time', 'name']
        ]


@python_2_unicode_compatible
class EventMedia(EventMediaBase):
    event = models.ForeignKey(Event, related_name='media')

    def __str__(self):
        return '%s for %s' % (self.note, self.event)


@python_2_unicode_compatible
class EventMediaLink(MimetypeLinkBase):
    media = models.ForeignKey(EventMedia, related_name='links')

    def __str__(self):
        return '{0} for {1}'.format(self.url, self.media.event)


@python_2_unicode_compatible
class EventDocument(MimetypeLinkBase):
    event = models.ForeignKey(Event, related_name='documents')
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=10)

    def __str__(self):
        tmpl = '{doc.note} for event {doc.event}'
        return tmpl.format(doc=self)


@python_2_unicode_compatible
class EventDocumentLink(MimetypeLinkBase):
    document = models.ForeignKey(EventDocument, related_name='links')

    def __str__(self):
        return '{0} for {1}'.format(self.url, self.document.bill)


class EventLink(LinkBase):
    event = models.ForeignKey(Event, related_name='links')


class EventSource(LinkBase):
    event = models.ForeignKey(Event, related_name='sources')


@python_2_unicode_compatible
class EventParticipant(RelatedEntityBase):
    event = models.ForeignKey(Event, related_name='participants')
    note = models.TextField()

    def __str__(self):
        tmpl = '%s at %s'
        return tmpl % (self.name, self.event)


@python_2_unicode_compatible
class EventAgendaItem(RelatedBase):
    description = models.TextField()
    classification = ArrayField(base_field=models.TextField(), blank=True, default=list)
    order = models.CharField(max_length=100, blank=True)
    subjects = ArrayField(base_field=models.TextField(), blank=True, default=list)
    notes = ArrayField(base_field=models.TextField(), blank=True, default=list)
    event = models.ForeignKey(Event, related_name='agenda')

    def __str__(self):
        return '{0} for {1}'.format(self.description, self.event)


@python_2_unicode_compatible
class EventRelatedEntity(RelatedEntityBase):
    agenda_item = models.ForeignKey(EventAgendaItem, related_name='related_entities')
    bill = models.ForeignKey(Bill, null=True)
    vote_event = models.ForeignKey(VoteEvent, null=True)
    note = models.TextField()

    def __str__(self):
        return '{0} of {1}'.format(self.entity_name, self.agenda_item)

    @property
    def entity_name(self):
        if self.entity_type == 'vote' and self.vote_event_id:
            return self.vote_event.identifier
        elif self.entity_type == 'bill' and self.bill_id:
            return self.bill.identifier
        else:
            return super(EventRelatedEntity, self).entity_name

    @property
    def entity_id(self):
        if self.entity_type == 'vote':
            return self.vote_event_id
        if self.entity_type == 'bill':
            return self.bill_id
        return super(EventRelatedEntity, self).entity_id


@python_2_unicode_compatible
class EventAgendaMedia(EventMediaBase):
    agenda_item = models.ForeignKey(EventAgendaItem, related_name='media')

    def __str__(self):
        return '{0} for {1}'.format(self.note, self.agenda_item)


@python_2_unicode_compatible
class EventAgendaMediaLink(MimetypeLinkBase):
    media = models.ForeignKey(EventAgendaMedia, related_name='links')

    def __str__(self):
        return '{0} for {1}'.format(self.url, self.media)
