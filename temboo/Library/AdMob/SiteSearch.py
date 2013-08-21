# -*- coding: utf-8 -*-

###############################################################################
#
# SiteSearch
# Search for sites by specifying their ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SiteSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SiteSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/AdMob/SiteSearch')


    def new_input_set(self):
        return SiteSearchInputSet()

    def _make_result_set(self, result, path):
        return SiteSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SiteSearchChoreographyExecution(session, exec_id, path)

class SiteSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SiteSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientKey(self, value):
        """
        Set the value of the ClientKey input for this Choreo. ((required, string) The Client Key provided by AdMob.)
        """
        InputSet._set_input(self, 'ClientKey', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((conditional, string) Your AdMob username. Required unless providing a valid Token input.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_IncludeDeleted(self, value):
        """
        Set the value of the IncludeDeleted input for this Choreo. ((optional, boolean) If set to 1, ad groups that have been deleted will be included in the search result.)
        """
        InputSet._set_input(self, 'IncludeDeleted', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your Admob password. Required unless providing a valid Token input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that your want the response to be in. Accepted values are: xml (the default) and json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) Search for a site matching this ID.)
        """
        InputSet._set_input(self, 'SiteID', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when Email and Password are supplied.)
        """
        InputSet._set_input(self, 'Token', value)

class SiteSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SiteSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from AdMob. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when Email and Password are supplied.)
        """
        return self._output.get('Token', None)

class SiteSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SiteSearchResultSet(response, path)
