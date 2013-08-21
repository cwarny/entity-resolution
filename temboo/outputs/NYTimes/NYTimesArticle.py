# coding: utf-8

class NYTimesArticle:
    """
     Represents a NYTimes article

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getBody(self):
        """
        The body of the article
        """
        return self.base.get("body", [])

    def getByLine(self):
        """
        The 'by line' field containing the author's name
        """
        return self.base.get("byline", [])

    def getDate(self):
        """
        The publication date in YYYYMMDD format
        """
        return self.base.get("date", [])

    def getTitle(self):
        """
        The title of the article
        """
        return self.base.get("title", [])

    def getUrl(self):
        """
        The url for the article
        """
        return self.base.get("url", [])

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

