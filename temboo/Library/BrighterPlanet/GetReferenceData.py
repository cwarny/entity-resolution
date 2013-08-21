# -*- coding: utf-8 -*-

###############################################################################
#
# GetReferenceData
# Retrieves a wide variety of reference data sets provided by Brighter Planet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetReferenceData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReferenceData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/GetReferenceData')


    def new_input_set(self):
        return GetReferenceDataInputSet()

    def _make_result_set(self, result, path):
        return GetReferenceDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReferenceDataChoreographyExecution(session, exec_id, path)

class GetReferenceDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReferenceData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Resource(self, value):
        """
        Set the value of the Resource input for this Choreo. ((required, string) The name of the reference data resource you want to retrieve (i.e. airports, airlines, etc). Resource names are formatted using plural, lowercase, and underscores (i.e. automobile_makes).)
        """
        InputSet._set_input(self, 'Resource', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The desired response format. Accepted formats are: csv, xml, and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetReferenceDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReferenceData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class GetReferenceDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReferenceDataResultSet(response, path)
