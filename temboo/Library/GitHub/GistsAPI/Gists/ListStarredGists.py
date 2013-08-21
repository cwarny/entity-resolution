# -*- coding: utf-8 -*-

###############################################################################
#
# ListStarredGists
# Returns a list of starred gists for the authenticated user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListStarredGists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListStarredGists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/GistsAPI/Gists/ListStarredGists')


    def new_input_set(self):
        return ListStarredGistsInputSet()

    def _make_result_set(self, result, path):
        return ListStarredGistsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListStarredGistsChoreographyExecution(session, exec_id, path)

class ListStarredGistsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListStarredGists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Indicates the page index that you want to retrieve. This is used to page through many results. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)

class ListStarredGistsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListStarredGists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_LastPage(self):
        """
        Retrieve the value for the "LastPage" output from this Choreo execution. ((integer) If multiple pages are available for the response, this contains the last available page.)
        """
        return self._output.get('LastPage', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_NextPage(self):
        """
        Retrieve the value for the "NextPage" output from this Choreo execution. ((integer) If multiple pages are available for the response, this contains the next page that you should retrieve.)
        """
        return self._output.get('NextPage', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)

class ListStarredGistsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListStarredGistsResultSet(response, path)
