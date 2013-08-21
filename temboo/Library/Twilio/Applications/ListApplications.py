# -*- coding: utf-8 -*-

###############################################################################
#
# ListApplications
# Returns a list of Twilio applications associated with your account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListApplications(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListApplications Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/Applications/ListApplications')


    def new_input_set(self):
        return ListApplicationsInputSet()

    def _make_result_set(self, result, path):
        return ListApplicationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListApplicationsChoreographyExecution(session, exec_id, path)

class ListApplicationsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListApplications
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AuthToken', value)
    def set_FriendlyName(self, value):
        """
        Set the value of the FriendlyName input for this Choreo. ((optional, string) Only return applications with friendly names that exactly match this name.)
        """
        InputSet._set_input(self, 'FriendlyName', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page.)
        """
        InputSet._set_input(self, 'PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ListApplicationsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListApplications Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class ListApplicationsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListApplicationsResultSet(response, path)
