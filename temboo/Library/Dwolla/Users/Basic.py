# -*- coding: utf-8 -*-

###############################################################################
#
# Basic
# Retrieves the Dwolla account information for the user associated with the specified consumer credentials and Dwolla account identifier.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Basic(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Basic Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Users/Basic')


    def new_input_set(self):
        return BasicInputSet()

    def _make_result_set(self, result, path):
        return BasicResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BasicChoreographyExecution(session, exec_id, path)

class BasicInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Basic
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountIdentifier(self, value):
        """
        Set the value of the AccountIdentifier input for this Choreo. ((required, string) Dwolla account identifier or email address of the Dwolla account.)
        """
        InputSet._set_input(self, 'AccountIdentifier', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID provided by Dwolla (AKA the Consumer Key).)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The Client Secret provided by Dwolla (AKA the Consumer Secret).)
        """
        InputSet._set_input(self, 'ClientSecret', value)

class BasicResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Basic Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class BasicChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BasicResultSet(response, path)
