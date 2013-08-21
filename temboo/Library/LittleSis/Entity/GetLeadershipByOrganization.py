# -*- coding: utf-8 -*-

###############################################################################
#
# GetLeadershipByOrganization
# Retrieves a list of board members and executives for a given organization.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetLeadershipByOrganization(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLeadershipByOrganization Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetLeadershipByOrganization')


    def new_input_set(self):
        return GetLeadershipByOrganizationInputSet()

    def _make_result_set(self, result, path):
        return GetLeadershipByOrganizationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLeadershipByOrganizationChoreographyExecution(session, exec_id, path)

class GetLeadershipByOrganizationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLeadershipByOrganization
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Current(self, value):
        """
        Set the value of the Current input for this Choreo. ((optional, integer) Set to 1 to limit the relationships returned to only past relationships. Set to 0 to limit relationships returned to only current relationships. Defaults to all.)
        """
        InputSet._set_input(self, 'Current', value)
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((required, integer) The ID of the organization.)
        """
        InputSet._set_input(self, 'EntityID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetLeadershipByOrganizationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLeadershipByOrganization Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetLeadershipByOrganizationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLeadershipByOrganizationResultSet(response, path)
