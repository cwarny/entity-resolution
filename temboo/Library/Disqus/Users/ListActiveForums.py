# -*- coding: utf-8 -*-

###############################################################################
#
# ListActiveForums
# Retrieve a list of forums a user has been active on.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListActiveForums(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListActiveForums Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Users/ListActiveForums')


    def new_input_set(self):
        return ListActiveForumsInputSet()

    def _make_result_set(self, result, path):
        return ListActiveForumsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListActiveForumsChoreographyExecution(session, exec_id, path)

class ListActiveForumsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListActiveForums
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) Default is set to null.)
        """
        InputSet._set_input(self, 'Cursor', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of records to return. Defaults to 25.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) The sort order for the results. Valid values are: asc or desc. Default is set to: asc.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SinceID(self, value):
        """
        Set the value of the SinceID input for this Choreo. ((optional, integer) A Unix timestamp (or ISO datetime standard) to obtain results from. Default is set to null.)
        """
        InputSet._set_input(self, 'SinceID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) the Disqus User ID, for which active forum information will be retrieved.  If UserID is set, then Username must be null.)
        """
        InputSet._set_input(self, 'UserID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) A Disqus username.  If Username is being set, then UserID must be null.)
        """
        InputSet._set_input(self, 'Username', value)

class ListActiveForumsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListActiveForums Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class ListActiveForumsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListActiveForumsResultSet(response, path)
