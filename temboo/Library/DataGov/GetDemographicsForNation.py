# -*- coding: utf-8 -*-

###############################################################################
#
# GetDemographicsForNation
# Retrieve demographic information for the entire nation.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetDemographicsForNation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDemographicsForNation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetDemographicsForNation')


    def new_input_set(self):
        return GetDemographicsForNationInputSet()

    def _make_result_set(self, result, path):
        return GetDemographicsForNationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDemographicsForNationChoreographyExecution(session, exec_id, path)

class GetDemographicsForNationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDemographicsForNation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DataVersion(self, value):
        """
        Set the value of the DataVersion input for this Choreo. ((optional, string) Specify the census data version to search, such as "jun2011" (the default).)
        """
        InputSet._set_input(self, 'DataVersion', value)

class GetDemographicsForNationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDemographicsForNation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from the API.)
        """
        return self._output.get('Response', None)

class GetDemographicsForNationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDemographicsForNationResultSet(response, path)
