# -*- coding: utf-8 -*-

###############################################################################
#
# GetDistrictsByZip
# Returns all districts that overlap the area for a given zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetDistrictsByZip(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDistrictsByZip Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/District/GetDistrictsByZip')


    def new_input_set(self):
        return GetDistrictsByZipInputSet()

    def _make_result_set(self, result, path):
        return GetDistrictsByZipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDistrictsByZipChoreographyExecution(session, exec_id, path)

class GetDistrictsByZipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDistrictsByZip
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, string) The zip code for the districts to return.)
        """
        InputSet._set_input(self, 'Zip', value)

class GetDistrictsByZipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDistrictsByZip Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetDistrictsByZipChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDistrictsByZipResultSet(response, path)
