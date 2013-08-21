# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyByCWID
# Returns basic information for a specifiied company.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetCompanyByCWID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCompanyByCWID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Company/GetCompanyByCWID')


    def new_input_set(self):
        return GetCompanyByCWIDInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyByCWIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyByCWIDChoreographyExecution(session, exec_id, path)

class GetCompanyByCWIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCompanyByCWID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CWID(self, value):
        """
        Set the value of the CWID input for this Choreo. ((required, string) CoprWatch ID for the company. Format looks like: cw_8484.)
        """
        InputSet._set_input(self, 'CWID', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((optional, integer) Specify the year for which you want company information. When none is specified, returns the most recent record available for that company.)
        """
        InputSet._set_input(self, 'Year', value)

class GetCompanyByCWIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCompanyByCWID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class GetCompanyByCWIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompanyByCWIDResultSet(response, path)
