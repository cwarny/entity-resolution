# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveFriends
# Returns the friends in a user's network.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveFriends(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveFriends Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Friends/RetrieveFriends')


    def new_input_set(self):
        return RetrieveFriendsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveFriendsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveFriendsChoreographyExecution(session, exec_id, path)

class RetrieveFriendsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveFriends
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number entries to return per page. Defaults to 25.)
        """
        InputSet._set_input(self, 'PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of entries to return. This parameter is used in combination with the PageSize input to page through results. Defaults to 0 (the first page).)
        """
        InputSet._set_input(self, 'Page', value)

class RetrieveFriendsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveFriends Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Next(self):
        """
        Retrieve the value for the "Next" output from this Choreo execution. ((integer) The next page of entries that is available. This value can be passed into the Page input while paging through entries.)
        """
        return self._output.get('Next', None)
    def get_Previous(self):
        """
        Retrieve the value for the "Previous" output from this Choreo execution. ((integer) The previous page of entries that is available. This value can be passed into the Page input while paging through entries.)
        """
        return self._output.get('Previous', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class RetrieveFriendsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveFriendsResultSet(response, path)
