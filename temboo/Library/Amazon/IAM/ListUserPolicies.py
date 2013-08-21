# -*- coding: utf-8 -*-

###############################################################################
#
# ListUserPolicies
# Lists the names of the policies associated with the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListUserPolicies(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListUserPolicies Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/ListUserPolicies')


    def new_input_set(self):
        return ListUserPoliciesInputSet()

    def _make_result_set(self, result, path):
        return ListUserPoliciesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUserPoliciesChoreographyExecution(session, exec_id, path)

class ListUserPoliciesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListUserPolicies
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
    def set_Marker(self, value):
        """
        Set the value of the Marker input for this Choreo. ((optional, string) Used for pagination to indicate the starting point of the results to return.)
        """
        InputSet._set_input(self, 'Marker', value)
    def set_MaxItems(self, value):
        """
        Set the value of the MaxItems input for this Choreo. ((optional, integer) Used for pagination to limit the number of results returned. Defaults to 100.)
        """
        InputSet._set_input(self, 'MaxItems', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) The name of the user to list policies for.)
        """
        InputSet._set_input(self, 'UserName', value)

class ListUserPoliciesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListUserPolicies Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class ListUserPoliciesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListUserPoliciesResultSet(response, path)
