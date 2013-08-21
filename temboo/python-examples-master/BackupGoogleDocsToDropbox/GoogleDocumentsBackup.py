"""
Copyright 2012, Temboo Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


This is a simple Python application that demonstrates how to use the Temboo
SDK to backup a set of Google Documents files to Dropbox. To run the demo,
you'll need a Temboo account, and of course Dropbox and Google Docs accounts.
The demo uses Temboo SDK functions to create a new folder to hold your backups
of Dropbox, then retrieves a list of Google Documents files for the specified
account, downloads each file and then uploads it to the Dropbox folder.

@author Joaquin Maguire
"""

import sys
from xml.etree import ElementTree

from temboo.core.session import TembooSession
from temboo.Library import Dropbox
from temboo.Library.Google import Documents
from temboo.Library.Google import Spreadsheets

"""
UPDATE THE VALUES OF THESE CONSTANTS WITH YOUR OWN CREDENTIALS
"""

# These constants define the oAuth credentials with which you access your
# Dropbox account.
DROPBOX_OAUTH_CONSUMER_KEY = "YOUR KEY"
DROPBOX_OAUTH_CONSUMER_SECRET = "YOUR SECRET"
DROPBOX_OAUTH_TOKEN = "YOUR TOKEN"
DROPBOX_OAUTH_TOKEN_SECRET = "YOUR TOKEN SECRET"

# Use this constant to define the name of the folder that will be created
# on Dropbox, and that will hold the set of uploaded documents. Note that
# another folder with the same name can't already exist on Dropbox.
DROPBOX_BACKUP_FOLDERNAME = "GoogleDocBackups"

# Use these constants to define the set of credentials that will be used 
# to access Google Documents.
GOOGLEDOCS_USERNAME = "YOUR USERNAME"
GOOGLEDOCS_PASSWORD = "YOUR PASSWORD"

# Use these constants to define the set of credentials that will be used 
# to connect with Temboo.
TEMBOO_ACCOUNT_NAME = "YOUR ACCOUNT NAME"
TEMBOO_APPLICATIONKEY_NAME = "YOUR APPKEY NAME"
TEMBOO_APPLICATIONKEY = "YOUR APPKEY"

"""
END CONSTANTS; NOTHING BELOW THIS POINT SHOULD NEED TO BE CHANGED
"""


class GoogleDocumentsBackup:

    def __init__(self):
        """
        Set up Temboo session. Create a target folder in Dropbox.
        """
        self.session = TembooSession(TEMBOO_ACCOUNT_NAME, TEMBOO_APPLICATIONKEY_NAME, 
                                TEMBOO_APPLICATIONKEY)

    def create_new_folder(self):
        """
        Add a folder in your dropbox account in to which you will place your
        backed up Google documents.
        """
        # Use the Dropbox.CreateFolder choreo to  create a new folder.
        create_folder = Dropbox.CreateFolder(self.session)
        # Inputs for the folder-creation choreo.
        inputs = Dropbox.CreateFolderInputSet() 
        
        # Set input values. The Dropbox.CreateFolder choreo requires the name of the
        # folder to create, and the Dropbox credentials, as inputs
        inputs.set_NewFolderName(DROPBOX_BACKUP_FOLDERNAME)
        inputs.set_OauthConsumerKey(DROPBOX_OAUTH_CONSUMER_KEY)
        inputs.set_OauthConsumerSecret(DROPBOX_OAUTH_CONSUMER_SECRET)
        inputs.set_OauthToken(DROPBOX_OAUTH_TOKEN)
        inputs.set_OauthTokenSecret(DROPBOX_OAUTH_TOKEN_SECRET)

        # Create the folder by running the choreo.
        folder_result = create_folder.execute_with_results(inputs)
        if folder_result.status:
            return True
        else:
            return False


    def get_file_list(self):
        """
        Get the list of files to be backed up from Google Docs.
        """
        file_dict = {}

        # Choreo to retrieve document list.
        get_doc_list = Documents.GetAllDocuments(self.session)
        # Inputs for the list-fetching choreo.
        inputs = Documents.GetAllDocumentsInputSet()
        # Configure inputs
        inputs.set_Username(GOOGLEDOCS_USERNAME)
        inputs.set_Password(GOOGLEDOCS_PASSWORD)
        inputs.set_Deleted("false")

        # Get Temboo result object.
        results = get_doc_list.execute_with_results(inputs)
        # Convert the XML response to an ElementTree object.
        result_tree = ElementTree.fromstring(results.get_Response())
        # Get the list of entries (each entry represents a file.)
        entry_list = result_tree.findall("{http://www.w3.org/2005/Atom}entry")

        # Get the information that we will need to download the document.
        for entry in entry_list:
            title = entry.find("{http://www.w3.org/2005/Atom}title").text
            content = entry.find("{http://www.w3.org/2005/Atom}content")
            src = content.attrib["src"]
            file_dict[title] = src

        return file_dict


    def download_from_google_docs(self, location):
        # If it's a spreadsheet, download the document with the
        # DownloadBase64EncodedSpreadsheet choreo.
        if location.find("spreadsheet") >= 0:
            choreo = \
                Spreadsheets.DownloadBase64EncodedSpreadsheet(self.session)
            inputs = Spreadsheets.DownloadBase64EncodedSpreadsheetInputSet()
        # Otherwise use DownloadBase64EncodedDocument.
        else:
            choreo = Documents.DownloadBase64EncodedDocument(self.session)
            inputs = Documents.DownloadBase64EncodedDocumentInputSet()
            # Make sure we're expecting the right type of document.
            if location.find("pdf") >= 0:
                inputs.set_Format("pdf")
            else:
                inputs.set_Format("doc")
        
        # The other properties are the same for both sheets and docs.
        inputs.set_Link(location)
        inputs.set_Username(GOOGLEDOCS_USERNAME)
        inputs.set_Password(GOOGLEDOCS_PASSWORD)
        inputs.set_Title("")

        # Run the choreo and return its results.
        results = choreo.execute_with_results(inputs)
        return results.get_FileContents()


    def upload_to_dropbox(self, name, contents):
        choreo = Dropbox.UploadFile(self.session)

        # Create input and set salient values.
        inputs = Dropbox.UploadFileInputSet()
        inputs.set_Folder(DROPBOX_BACKUP_FOLDERNAME)
        inputs.set_OauthConsumerKey(DROPBOX_OAUTH_CONSUMER_KEY)
        inputs.set_OauthConsumerSecret(DROPBOX_OAUTH_CONSUMER_SECRET)
        inputs.set_OauthToken(DROPBOX_OAUTH_TOKEN)
        inputs.set_OauthTokenSecret(DROPBOX_OAUTH_TOKEN_SECRET)
        inputs.set_FileContents(contents)
        inputs.set_FileName(name)

        # Upload the file to Dropbox.
        try:
            choreo.execute_with_results(inputs)
            print "Uploaded", name
        except Exception, e:
            print "An error occurred attempting to upload", name
            raise e

    def main(self):
        """
        Wraps things all up. Get the list of documents and upload each to
        Dropbox.
        """
        self.create_new_folder()
        file_list = self.get_file_list()
        for file_name in file_list.keys():
            contents = self.download_from_google_docs(file_list[file_name])
            self.upload_to_dropbox(file_name, contents)


if __name__ == "__main__":
    instance = GoogleDocumentsBackup()
    instance.main()



