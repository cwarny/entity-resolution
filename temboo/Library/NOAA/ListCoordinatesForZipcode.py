# -*- coding: utf-8 -*-

###############################################################################
#
# ListCoordinatesForZipcode
# Retrieve latitude and longitude data for a specified zipcode (in 50 U.S. States and Puerto Rico).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListCoordinatesForZipcode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListCoordinatesForZipcode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NOAA/ListCoordinatesForZipcode')


    def new_input_set(self):
        return ListCoordinatesForZipcodeInputSet()

    def _make_result_set(self, result, path):
        return ListCoordinatesForZipcodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCoordinatesForZipcodeChoreographyExecution(session, exec_id, path)

class ListCoordinatesForZipcodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListCoordinatesForZipcode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ListZipCodeList(self, value):
        """
        Set the value of the ListZipCodeList input for this Choreo. ((integer) Enter the zipcode for which latitude and longitude coordinates will be retrieved.)
        """
        InputSet._set_input(self, 'ListZipCodeList', value)

class ListCoordinatesForZipcodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListCoordinatesForZipcode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) Response from NDFD servers.)
        """
        return self._output.get('Response', None)

class ListCoordinatesForZipcodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListCoordinatesForZipcodeResultSet(response, path)
