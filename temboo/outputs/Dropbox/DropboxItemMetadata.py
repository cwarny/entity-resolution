# coding: utf-8

class DropboxItemMetadata:
    """
     The metadata for the file or folder at the given <path>. If <path> represents a folder and the list parameter is true, the metadata will also include a listing of metadata for the folder's contents.

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getBytes(self):
        """
        The file size in bytes.
        """
        return self.base.get("bytes", [])

    def getClientMtime(self):
        """
        For files, this is the modification time set by the desktop client when the file was added to Dropbox, in the standard date format. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not.
        """
        return self.base.get("client_mtime", [])

    def getIcon(self):
        """
        The name of the icon used to illustrate the file type in Dropbox's icon library.
        """
        return self.base.get("icon", [])

    def getIsDeleted(self):
        """
        Whether the given entry is deleted (only included if deleted files are being returned).
        """
        return self.base.get("is_deleted", [])

    def getIsDir(self):
        """
        Whether the given entry is a folder or not.
        """
        return self.base.get("is_dir", [])

    def getMimeType(self):
        """
        The mime type of the file.
        """
        return self.base.get("mime_type", [])

    def getModified(self):
        """
        The last time the file was modified on Dropbox, in the standard date format (not included for the root folder).
        """
        return self.base.get("modified", [])

    def getPath(self):
        """
        Returns the canonical path to the file or directory.
        """
        return self.base.get("path", [])

    def getRev(self):
        """
        A unique identifier for the current revision of a file. This field is the same rev as elsewhere in the API and can be used to detect changes and avoid conflicts.
        """
        return self.base.get("rev", [])

    def getRevision(self):
        """
        A deprecated field that semi-uniquely identifies a file. Use rev instead.
        """
        return self.base.get("revision", [])

    def getRoot(self):
        """
        The root or top-level folder depending on your access level. All paths returned are relative to this root level. Permitted values are either dropbox or app_folder.
        """
        return self.base.get("root", [])

    def getSize(self):
        """
        A human-readable description of the file size (translated by locale).
        """
        return self.base.get("size", [])

    def getThumbExists(self):
        """
        True if the file is an image can be converted to a thumbnail via the /thumbnails call.
        """
        return self.base.get("thumb_exists", [])

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

