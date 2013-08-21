# -*- coding: utf-8 -*-

###############################################################################
#
# GetBookmark
# Retrieves one or more bookmarked links posted on a single day.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetBookmark(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBookmark Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Delicious/GetBookmark')


    def new_input_set(self):
        return GetBookmarkInputSet()

    def _make_result_set(self, result, path):
        return GetBookmarkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBookmarkChoreographyExecution(session, exec_id, path)

class GetBookmarkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBookmark
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ChangeSignature(self, value):
        """
        Set the value of the ChangeSignature input for this Choreo. ((optional, string) Return only bookmarks with the URL MD5 signatures you enter, regardless of posting date. Separate multiple signatures with spaces.)
        """
        InputSet._set_input(self, 'ChangeSignature', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) Return only bookmarks posted on a date specified here. Enter in YYYY-MM-DDThh:mm:ssZ format. Defaults to the most recent date.)
        """
        InputSet._set_input(self, 'Date', value)
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
        Set the value of the Tag input for this Choreo. ((optional, string) Return only items tagged with the specified keyword. Separate multiple tags with spaces.)
        """
        InputSet._set_input(self, 'Tag', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) Return only items with the specified URL, regardless of posting date.)
        """
        InputSet._set_input(self, 'URL', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        InputSet._set_input(self, 'Username', value)

class GetBookmarkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBookmark Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class GetBookmarkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBookmarkResultSet(response, path)
