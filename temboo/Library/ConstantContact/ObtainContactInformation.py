# -*- coding: utf-8 -*-

###############################################################################
#
# ObtainContactInformation
# Retrieves contact information from Constant Contact by specifying the contact ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ObtainContactInformation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ObtainContactInformation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/ObtainContactInformation')


    def new_input_set(self):
        return ObtainContactInformationInputSet()

    def _make_result_set(self, result, path):
        return ObtainContactInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ObtainContactInformationChoreographyExecution(session, exec_id, path)

class ObtainContactInformationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ObtainContactInformation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Constant Contact.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ContactId(self, value):
        """
        Set the value of the ContactId input for this Choreo. ((required, integer) The ID for the contact you want to retrieve information for.)
        """
        InputSet._set_input(self, 'ContactId', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Constant Contact password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Your Constant Contact username.)
        """
        InputSet._set_input(self, 'UserName', value)

class ObtainContactInformationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ObtainContactInformation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Constant Contact.)
        """
        return self._output.get('Response', None)

class ObtainContactInformationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ObtainContactInformationResultSet(response, path)
