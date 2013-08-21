# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveFolderItems
# Retrieves only the files and/or folders contained within the specified folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveFolderItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveFolderItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Folders/RetrieveFolderItems')


    def new_input_set(self):
        return RetrieveFolderItemsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveFolderItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveFolderItemsChoreographyExecution(session, exec_id, path)

class RetrieveFolderItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveFolderItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((conditional, string) The id of the folder that you want to retrieve items for. Defaults to 0 indicating the "root" folder.)
        """
        InputSet._set_input(self, 'FolderID', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of items to return.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The item at which to begin the response.)
        """
        InputSet._set_input(self, 'Offset', value)


class RetrieveFolderItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveFolderItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class RetrieveFolderItemsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveFolderItemsResultSet(response, path)
