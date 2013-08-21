# coding: utf-8

class FacebookSummary:
    """
     A summary object containing information about the inbox

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getUnreadCount(self):
        """
        The total number of unread items in the inbox
        """
        return self.base.get("unread_count", [])

    def getUnseenCount(self):
        """
        The total number of unseen items in the inbox
        """
        return self.base.get("unseen_count", [])

    def getUpdatedTime(self):
        """
        The last updated time of the inbox
        """
        return self.base.get("updated_time", [])

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

