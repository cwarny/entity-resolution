# -*- coding: utf-8 -*-

###############################################################################
#
# GraduationRates
# Returns gradutation statistics about colleges and univeristies.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GraduationRates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GraduationRates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DeptOfEducation/CollegesAndUniversities/GraduationRates')


    def new_input_set(self):
        return GraduationRatesInputSet()

    def _make_result_set(self, result, path):
        return GraduationRatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GraduationRatesChoreographyExecution(session, exec_id, path)

class GraduationRatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GraduationRates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_InstitutionID(self, value):
        """
        Set the value of the InstitutionID input for this Choreo. ((optional, string) Specify an institutionID to return data on a specific institution. These ids can be retrieved from the LookupSchool Choreo.)
        """
        InputSet._set_input(self, 'InstitutionID', value)
    def set_MaxRows(self, value):
        """
        Set the value of the MaxRows input for this Choreo. ((optional, integer) Limits the number of rows returned. Defaults to 20.)
        """
        InputSet._set_input(self, 'MaxRows', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GraduationRatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GraduationRates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Data.ed.gov.)
        """
        return self._output.get('Response', None)

class GraduationRatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GraduationRatesResultSet(response, path)
