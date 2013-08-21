# coding: utf-8

class GoogleEvent:
    """
     A single event on a calendar containing information such as the title of event, start and end times, and attendees.
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAttendees(self):
        """
        The attendees of the event.
        """
        return [GoogleAttendees(le) for le in self.base.get("attendees", [])]


    def getCreated(self):
        """
        Creation time of the event (as a RFC 3339 timestamp).
        """
        return self.base.get("created", [])

    def getCreator(self):
        """
        The creator of the event.
        """
        return GoogleCreator(self.base.get("creator", []))

    def getDescription(self):
        """
        Description of the event.
        """
        return self.base.get("description", [])

    def getEnd(self):
        """
        The (exclusive) end time of the event. For a recurring event, this is the end time of the first instance.
        """
        return GoogleEnd(self.base.get("end", []))

    def getEtag(self):
        """
        ETag of the resource.
        """
        return self.base.get("etag", [])

    def getHtmlLink(self):
        """
        An absolute link to this event in the Google Calendar Web UI.
        """
        return self.base.get("htmlLink", [])

    def getICalUID(self):
        """
        Event ID in the iCalendar format.
        """
        return self.base.get("iCalUID", [])

    def getId(self):
        """
        Identifier of the event.
        """
        return self.base.get("id", [])

    def getKind(self):
        """
        Type of the resource ("calendar#event").
        """
        return self.base.get("kind", [])

    def getLocation(self):
        """
        Geographic location of the event as free-form text.
        """
        return self.base.get("location", [])

    def getOrganizer(self):
        """
        Whether the organizer corresponds to the calendar on which this copy of the event appears
        """
        return GoogleOrganizer(self.base.get("organizer", []))

    def getRecurrence(self):
        """
        List of RRULE, EXRULE, RDATE and EXDATE lines for a recurring event. This field is omitted for single events or instances of recurring events.
        """
        return [le for le in self.base.get("recurrence", [])]


    def getReminders(self):
        """
        If the event doesn't use the default reminders, this lists the reminders specific to the event, or, if not set, indicates that no reminders are set for this event.
        """
        return GoogleReminders(self.base.get("reminders", []))

    def getSequence(self):
        """
        Sequence number as per iCalendar.
        """
        return self.base.get("sequence", [])

    def getStart(self):
        """
        The (inclusive) start time of the event. For a recurring event, this is the start time of the first instance.
        """
        return GoogleStart(self.base.get("start", []))

    def getStatus(self):
        """
        Status of the event: "confirmed" - The event is confirmed. This is the default status, "tentative" - The event is tentatively confirmed, "cancelled" - The event is cancelled.
        """
        return self.base.get("status", [])

    def getSummary(self):
        """
        Title of the event.
        """
        return self.base.get("summary", [])

    def getUpdated(self):
        """
        Last modification time of the event (as a RFC 3339 timestamp).
        """
        return self.base.get("updated", [])

    def getBase(self):
        """
        Internal utility method; retrieve the base JSON object for this element of the response data.
        """
        return self.base

    def getJSONObject(self, json, key):
        """
        Internal utility method; retrieve a sub-object from a JSON object/array; returns an empty object if key is not present
        """
        toReturn = {}

        if json is not None:
            toReturn = json.get(key, {})

        return toReturn

from temboo.outputs.Google.Calendar.GoogleAttendees import GoogleAttendees
from temboo.outputs.Google.Calendar.GoogleCreator import GoogleCreator
from temboo.outputs.Google.Calendar.GoogleEnd import GoogleEnd
from temboo.outputs.Google.Calendar.GoogleOrganizer import GoogleOrganizer
from temboo.outputs.Google.Calendar.GoogleReminders import GoogleReminders
from temboo.outputs.Google.Calendar.GoogleStart import GoogleStart