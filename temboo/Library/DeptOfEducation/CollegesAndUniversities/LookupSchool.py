# -*- coding: utf-8 -*-

###############################################################################
#
# LookupSchool
# Allows you to search the U.S. Department of Education college and univeristy listings.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class LookupSchool(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LookupSchool Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DeptOfEducation/CollegesAndUniversities/LookupSchool')


    def new_input_set(self):
        return LookupSchoolInputSet()

    def _make_result_set(self, result, path):
        return LookupSchoolResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LookupSchoolChoreographyExecution(session, exec_id, path)

class LookupSchoolInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LookupSchool
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Keyword(self, value):
        """
        Set the value of the Keyword input for this Choreo. ((required, string) Used to perform a full text search on the data set. For example, you can search for an institution's name or an institution's ID.)
        """
        InputSet._set_input(self, 'Keyword', value)
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

class LookupSchoolResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LookupSchool Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Data.ed.gov.)
        """
        return self._output.get('Response', None)

class LookupSchoolChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LookupSchoolResultSet(response, path)
