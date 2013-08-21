# coding: utf-8

class GoogleExportLinks:
    """
     Links for exporting Google Docs to specific formats

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getPdfLink(self):
        """
        A link to the file in pdf format
        """
        return self.base.get("application/pdf", [])

    def getRtfLink(self):
        """
        A link to the file in rtf format
        """
        return self.base.get("application/rtf", [])

    def getOdtLink(self):
        """
        A link to the file in odt format
        """
        return self.base.get("application/vnd.oasis.opendocument.text", [])

    def getXlsxLink(self):
        """
        A link to the file in xlsx format
        """
        return self.base.get("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", [])

    def getDocxLink(self):
        """
        A link to the file in docx format
        """
        return self.base.get("application/vnd.openxmlformats-officedocument.wordprocessingml.document", [])

    def getOdsLink(self):
        """
        A link to the file in ods format
        """
        return self.base.get("application/x-vnd.oasis.opendocument.spreadsheet", [])

    def getHtmlLink(self):
        """
        A link to the file in html format
        """
        return self.base.get("text/html", [])

    def getTxtLink(self):
        """
        A link to the file in txt format
        """
        return self.base.get("text/plain", [])

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

