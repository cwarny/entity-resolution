# -*- coding: utf-8 -*-

###############################################################################
#
# GetEntityByOutsideID
# Retrieves the record for an Entity in LittleSis using the ID of a number of third-party organizations such as the SEC or GovTrack.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetEntityByOutsideID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetEntityByOutsideID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetEntityByOutsideID')


    def new_input_set(self):
        return GetEntityByOutsideIDInputSet()

    def _make_result_set(self, result, path):
        return GetEntityByOutsideIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEntityByOutsideIDChoreographyExecution(session, exec_id, path)

class GetEntityByOutsideIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetEntityByOutsideID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_IDType(self, value):
        """
        Set the value of the IDType input for this Choreo. ((required, string) You can search for a record by the IDs of other third-party services. Acceptable inputs: ticker, sec_cik, fec_id, bioguide_id, govtrack_id, crp_id, watchdog_id. See documentation for more information.)
        """
        InputSet._set_input(self, 'IDType', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The ID of the record to be returned.)
        """
        InputSet._set_input(self, 'ID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetEntityByOutsideIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetEntityByOutsideID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetEntityByOutsideIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEntityByOutsideIDResultSet(response, path)
