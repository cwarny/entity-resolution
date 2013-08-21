# -*- coding: utf-8 -*-

###############################################################################
#
# DownloadBase64EncodedDocument
# Downloads a document with the title you specify, and returns the content as Base64 encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DownloadBase64EncodedDocument(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DownloadBase64EncodedDocument Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/DownloadBase64EncodedDocument')


    def new_input_set(self):
        return DownloadBase64EncodedDocumentInputSet()

    def _make_result_set(self, result, path):
        return DownloadBase64EncodedDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadBase64EncodedDocumentChoreographyExecution(session, exec_id, path)

class DownloadBase64EncodedDocumentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DownloadBase64EncodedDocument
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) The format you want to export the document to, such as "doc", "txt", "pdf", etc. The default download format is HTML.)
        """
        InputSet._set_input(self, 'Format', value)
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((conditional, string) Enter the source links for the document to be retrieved. Required unless specifying the Title.)
        """
        InputSet._set_input(self, 'Link', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((conditional, string) The title of the document to download. Required unless specifying the download Link.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google account username.)
        """
        InputSet._set_input(self, 'Username', value)

class DownloadBase64EncodedDocumentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DownloadBase64EncodedDocument Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_FileContents(self):
        """
        Retrieve the value for the "FileContents" output from this Choreo execution. ((string) The Base64 encoded file content of the downloaded file.)
        """
        return self._output.get('FileContents', None)

class DownloadBase64EncodedDocumentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DownloadBase64EncodedDocumentResultSet(response, path)
