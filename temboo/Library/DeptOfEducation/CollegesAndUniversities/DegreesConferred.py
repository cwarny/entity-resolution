# -*- coding: utf-8 -*-

###############################################################################
#
# DegreesConferred
# Returns a list of all degrees conferred by a given institution, along with detailed demographic data for each degree awarded.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DegreesConferred(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DegreesConferred Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DeptOfEducation/CollegesAndUniversities/DegreesConferred')


    def new_input_set(self):
        return DegreesConferredInputSet()

    def _make_result_set(self, result, path):
        return DegreesConferredResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DegreesConferredChoreographyExecution(session, exec_id, path)

class DegreesConferredInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DegreesConferred
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

class DegreesConferredResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DegreesConferred Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Data.ed.gov.)
        """
        return self._output.get('Response', None)

class DegreesConferredChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DegreesConferredResultSet(response, path)
