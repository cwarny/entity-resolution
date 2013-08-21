# coding: utf-8

class FacebookFormat:
    """
     An object containing format parameters for the video

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEmbedHtml(self):
        """
        The html element that may be embedded in an Web page to play the video
        """
        return self.base.get("embed_html", [])

    def getFilter(self):
        """
        The video filter parameter
        """
        return self.base.get("filter", [])

    def getHeight(self):
        """
        The video height
        """
        return self.base.get("height", [])

    def getPicture(self):
        """
        The URL for the thumbnail picture for the video
        """
        return self.base.get("picture", [])

    def getWidth(self):
        """
        The video width
        """
        return self.base.get("width", [])

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

