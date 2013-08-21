# -*- coding: utf-8 -*-

###############################################################################
#
# GetZipCodeDetails
# Returns the details for a given zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetZipCodeDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetZipCodeDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetZipCodeDetails')


    def new_input_set(self):
        return GetZipCodeDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetZipCodeDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetZipCodeDetailsChoreographyExecution(session, exec_id, path)

class GetZipCodeDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetZipCodeDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((conditional, string) The App ID provided by Genability.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        InputSet._set_input(self, 'AppKey', value)
    def set_PageCount(self, value):
        """
        Set the value of the PageCount input for this Choreo. ((optional, integer) The number of results to return. Defaults to 25.)
        """
        InputSet._set_input(self, 'PageCount', value)
    def set_PageStart(self, value):
        """
        Set the value of the PageStart input for this Choreo. ((optional, integer) The page number to begin the result set from. Defaults to 1.)
        """
        InputSet._set_input(self, 'PageStart', value)
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((optional, string) A zip code to search with.)
        """
        InputSet._set_input(self, 'ZipCode', value)

class GetZipCodeDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetZipCodeDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetZipCodeDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetZipCodeDetailsResultSet(response, path)
