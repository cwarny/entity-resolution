# -*- coding: utf-8 -*-

###############################################################################
#
# FindByAddress
# Retrieves complete geocoding information for a location by specifying an address or partial address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FindByAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindByAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/PlaceFinder/FindByAddress')


    def new_input_set(self):
        return FindByAddressInputSet()

    def _make_result_set(self, result, path):
        return FindByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByAddressChoreographyExecution(session, exec_id, path)

class FindByAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindByAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) The address to be searched.)
        """
        InputSet._set_input(self, 'Address', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) The App ID provided by Yahoo!)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_GeocodeFlags(self, value):
        """
        Set the value of the GeocodeFlags input for this Choreo. ((optional, string) Affects how geocoding is performed for the request. Valid value are: A, C, L, Q, or R. See documentation for more details on this parameter.)
        """
        InputSet._set_input(self, 'GeocodeFlags', value)
    def set_ResponseFlags(self, value):
        """
        Set the value of the ResponseFlags input for this Choreo. ((optional, string) Determines which data elements are returned in the response. Valid values are: B, C, D, E, G, I, J, Q, R, T, U, W, X. See documentation for details on this parameter.)
        """
        InputSet._set_input(self, 'ResponseFlags', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) You can specify json to get this output format in JSON. Otherwise, the default output will be in XML.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class FindByAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindByAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yahoo! PlaceFinder.)
        """
        return self._output.get('Response', None)

class FindByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindByAddressResultSet(response, path)
