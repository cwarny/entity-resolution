# coding: utf-8

class StripeDeleteResults:
    """
      An object with the deleted object's ID and a deleted flag upon success. An error is returned otherwise, such as if the object has already been deleted.

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDeleted(self):
        """
        A delete flag showing true on success.
        """
        return self.base.get("deleted", [])

    def getId(self):
        """
        ID of the deleted object
        """
        return self.base.get("id", [])

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

