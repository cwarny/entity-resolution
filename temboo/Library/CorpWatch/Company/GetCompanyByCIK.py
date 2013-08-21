# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyByCIK
# Returns a company record for a given SEC CIK identification number.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetCompanyByCIK(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCompanyByCIK Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Company/GetCompanyByCIK')


    def new_input_set(self):
        return GetCompanyByCIKInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyByCIKResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyByCIKChoreographyExecution(session, exec_id, path)

class GetCompanyByCIKInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCompanyByCIK
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CIK(self, value):
        """
        Set the value of the CIK input for this Choreo. ((required, string) The SEC's CIK identification number.)
        """
        InputSet._set_input(self, 'CIK', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        InputSet._set_input(self, 'Index', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((optional, integer) If a year is specified, only records for that year will be returned and the data in the company objects returned will be set appropriately for the request year. Defaults to most recent.)
        """
        InputSet._set_input(self, 'Year', value)

class GetCompanyByCIKResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCompanyByCIK Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class GetCompanyByCIKChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompanyByCIKResultSet(response, path)
