# coding: utf-8

class DropboxAccountInfo:
    """
     Information about the user's account.

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCountry(self):
        """
        The user's two-letter country code, if available.
        """
        return self.base.get("country", [])

    def getDisplayName(self):
        """
        The user's display name.
        """
        return self.base.get("display_name", [])

    def getEmail(self):
        """
        The user's e-mail address.
        """
        return self.base.get("email", [])

    def getQuotaInfo(self):
        """
        User's quota info for shared/unshared folders
        """
        return DropboxQuotaInfo(self.base.get("quota_info", []))

    def getReferralLink(self):
        """
        The user's referral link.
        """
        return self.base.get("referral_link", [])

    def getUid(self):
        """
        The user's unique Dropbox ID.
        """
        return self.base.get("uid", [])

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

from temboo.outputs.Dropbox.DropboxQuotaInfo import DropboxQuotaInfo