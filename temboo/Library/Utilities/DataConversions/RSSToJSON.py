# -*- coding: utf-8 -*-

###############################################################################
#
# RSSToJSON
# Retrieves a specified RSS Feed, and converts it to JSON format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RSSToJSON(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RSSToJSON Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/RSSToJSON')


    def new_input_set(self):
        return RSSToJSONInputSet()

    def _make_result_set(self, result, path):
        return RSSToJSONResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RSSToJSONChoreographyExecution(session, exec_id, path)

class RSSToJSONInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RSSToJSON
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RSSFeed(self, value):
        """
        Set the value of the RSSFeed input for this Choreo. ((required, string) The URL for an RSS feed that you wish to convert to JSON.)
        """
        InputSet._set_input(self, 'RSSFeed', value)

class RSSToJSONResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RSSToJSON Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The feed data in JSON format.)
        """
        return self._output.get('Response', None)

class RSSToJSONChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RSSToJSONResultSet(response, path)
