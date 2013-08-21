# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyProfiles
# Retrieve multiple company profiles using a given list of company IDs or names.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetCompanyProfiles(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCompanyProfiles Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Companies/GetCompanyProfiles')


    def new_input_set(self):
        return GetCompanyProfilesInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyProfilesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyProfilesChoreographyExecution(session, exec_id, path)

class GetCompanyProfilesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCompanyProfiles
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Companies(self, value):
        """
        Set the value of the Companies input for this Choreo. ((required, string) A comma separated list of company IDs or universal-name key/value pairs. IDs and names can be mixed also. For example: 812686,universal-name=linkedin,universal-name=apple.)
        """
        InputSet._set_input(self, 'Companies', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'SecretKey', value)

class GetCompanyProfilesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCompanyProfiles Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from LinkedIn in XML format.)
        """
        return self._output.get('Response', None)

class GetCompanyProfilesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompanyProfilesResultSet(response, path)
