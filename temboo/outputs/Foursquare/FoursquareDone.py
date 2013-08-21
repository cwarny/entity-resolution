# coding: utf-8

class FoursquareDone:
    """
     Contains a count of tips that are done

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCount(self):
        """
        The number of tips that are done
        """
        return self.base.get("count", [])

    def getPeopleGroup(self):
        """
        Get groups of people that have marked this tip done
        """
        return [FoursquarePeopleGroup(le) for le in self.base.get("groups", [])]


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

from temboo.outputs.Foursquare.FoursquarePeopleGroup import FoursquarePeopleGroup