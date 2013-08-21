# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllBookmarks
# Returns all links posted to a Delicious account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetAllBookmarks(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAllBookmarks Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Delicious/GetAllBookmarks')


    def new_input_set(self):
        return GetAllBookmarksInputSet()

    def _make_result_set(self, result, path):
        return GetAllBookmarksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllBookmarksChoreographyExecution(session, exec_id, path)

class GetAllBookmarksInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAllBookmarks
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of bookmarks to return. Defaults to 15.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_FromDate(self, value):
        """
        Set the value of the FromDate input for this Choreo. ((optional, date) Return only bookmarks posted on this date and later. Enter in YYYY-MM-DDThh:mm:ssZ format.)
        """
        InputSet._set_input(self, 'FromDate', value)
    def set_Meta(self, value):
        """
        Set the value of the Meta input for this Choreo. ((optional, string) Specify "1" to include a change-detection signature for each item returned. Defaults to "0", or no meta attributes retained.)
        """
        InputSet._set_input(self, 'Meta', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((optional, string) Return only bookmrks tagged with this keyword.)
        """
        InputSet._set_input(self, 'Tag', value)
    def set_ToDate(self, value):
        """
        Set the value of the ToDate input for this Choreo. ((optional, date) Return only bookmarks posted on this date and earlier. Enter in YYYY-MM-DDThh:mm:ssZ format.)
        """
        InputSet._set_input(self, 'ToDate', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        InputSet._set_input(self, 'Username', value)

class GetAllBookmarksResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAllBookmarks Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class GetAllBookmarksChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAllBookmarksResultSet(response, path)
