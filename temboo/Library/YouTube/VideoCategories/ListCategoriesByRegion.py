# -*- coding: utf-8 -*-

###############################################################################
#
# ListCategoriesByRegion
# Returns a list of categories available in the specified country.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Google.Drive.GoogleFileList import GoogleFileList

import json

class ListCategoriesByRegion(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListCategoriesByRegion Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/YouTube/VideoCategories/ListCategoriesByRegion')


    def new_input_set(self):
        return ListCategoriesByRegionInputSet()

    def _make_result_set(self, result, path):
        return ListCategoriesByRegionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCategoriesByRegionChoreographyExecution(session, exec_id, path)

class ListCategoriesByRegionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListCategoriesByRegion
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Google for simple API access when you do not need to access user data.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_H1(self, value):
        """
        Set the value of the H1 input for this Choreo. ((optional, string) The hl parameter specifies the language that should be used for text values in the API response. The default value is en_US.)
        """
        InputSet._set_input(self, 'H1', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) Specifies the videoCategory resource parts that the API response will include. Valid values are: id and snippet.)
        """
        InputSet._set_input(self, 'Part', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_RegionCode(self, value):
        """
        Set the value of the RegionCode input for this Choreo. ((conditional, string) Indicates to return the list of video categories available in the specified country. The parameter value is an ISO 3166-1 alpha-2 country code.)
        """
        InputSet._set_input(self, 'RegionCode', value)

class ListCategoriesByRegionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListCategoriesByRegion Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from YouTube.)
        """
        return self._output.get('Response', None)
    def getFileList(self):
        """
        Get a list of files
        """
        return GoogleFileList(self.getJSONFromString(self._output.get('Response', [])))

class ListCategoriesByRegionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListCategoriesByRegionResultSet(response, path)
