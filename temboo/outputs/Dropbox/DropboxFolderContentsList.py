# coding: utf-8

class DropboxFolderContentsList:
    """
     A list of metdata for the folder's contents

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getBytes(self):
        """
        A human-readable description of the file size (translated by locale).
        """
        return self.base.get("bytes", [])

    def getItemMetadata(self):
        """
        a list of metadata for the folder's contents
        """
        return [DropboxItemMetadata(le) for le in self.base.get("contents", [])]


    def getHash(self):
        """
        A folder's hash is useful for indicating changes to the folder's contents in later calls to /metadata. This is roughly the folder equivalent to a file's rev.
        """
        return self.base.get("hash", [])

    def getIcon(self):
        """
        The name of the icon used to illustrate the file type in Dropbox's icon library.
        """
        return self.base.get("icon", [])

    def getIsDir(self):
        """
        Whether the given entry is a folder or not.
        """
        return self.base.get("is_dir", [])

    def getPath(self):
        """
        Returns the canonical path to the file or directory.
        """
        return self.base.get("path", [])

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

from temboo.outputs.Dropbox.DropboxItemMetadata import DropboxItemMetadata