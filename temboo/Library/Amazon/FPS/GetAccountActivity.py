# -*- coding: utf-8 -*-

###############################################################################
#
# GetAccountActivity
# Returns account transactions from a specified start date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetAccountActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAccountActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/FPS/GetAccountActivity')


    def new_input_set(self):
        return GetAccountActivityInputSet()

    def _make_result_set(self, result, path):
        return GetAccountActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccountActivityChoreographyExecution(session, exec_id, path)

class GetAccountActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAccountActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) The endpoint should be fps.sandbox.amazonaws.com when accessing the sandbox. Defaults to production setting:  fps.amazonaws.com.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((required, date) The first date of transactions to return (epoch timestamp in milliseconds or formatted like 2009-10-07Z).)
        """
        InputSet._set_input(self, 'StartDate', value)

class GetAccountActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAccountActivity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetAccountActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAccountActivityResultSet(response, path)
