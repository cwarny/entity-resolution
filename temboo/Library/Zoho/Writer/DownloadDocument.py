# -*- coding: utf-8 -*-

###############################################################################
#
# DownloadDocument
# Downloads a specified document in a user's Zoho Writer Account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DownloadDocument(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DownloadDocument Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zoho/Writer/DownloadDocument')


    def new_input_set(self):
        return DownloadDocumentInputSet()

    def _make_result_set(self, result, path):
        return DownloadDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadDocumentChoreographyExecution(session, exec_id, path)

class DownloadDocumentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DownloadDocument
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Zoho)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DocumentId(self, value):
        """
        Set the value of the DocumentId input for this Choreo. ((required, integer) Specifies the unique document id to download.)
        """
        InputSet._set_input(self, 'DocumentId', value)
    def set_DownloadFormat(self, value):
        """
        Set the value of the DownloadFormat input for this Choreo. ((required, string) Specifies the file format in which the documents need to be downloaded. Possible values for documents: doc, docx, pdf, html, sxw, odt, rtf.)
        """
        InputSet._set_input(self, 'DownloadFormat', value)
    def set_LoginID(self, value):
        """
        Set the value of the LoginID input for this Choreo. ((required, string) Your Zoho username (or login id))
        """
        InputSet._set_input(self, 'LoginID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zoho password)
        """
        InputSet._set_input(self, 'Password', value)

class DownloadDocumentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DownloadDocument Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Zoho. Corresponds to the DownloadFormat input.)
        """
        return self._output.get('Response', None)

class DownloadDocumentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DownloadDocumentResultSet(response, path)
