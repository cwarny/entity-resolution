# -*- coding: utf-8 -*-

###############################################################################
#
# SearchForBugs
# Search for bugs listed by Mozilla product name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchForBugs(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchForBugs Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Bugzilla/SearchForBugs')


    def new_input_set(self):
        return SearchForBugsInputSet()

    def _make_result_set(self, result, path):
        return SearchForBugsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForBugsChoreographyExecution(session, exec_id, path)

class SearchForBugsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchForBugs
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BugChangeDate(self, value):
        """
        Set the value of the BugChangeDate input for this Choreo. ((optional, string) Retrieve bugs that were changed within a certain date range. For example: 25d will return all bugs changed from 25 days ago untill today.  Or: 3h, to return all bugs entered with 3 hours.)
        """
        InputSet._set_input(self, 'BugChangeDate', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Your Bugzilla password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Priority(self, value):
        """
        Set the value of the Priority input for this Choreo. ((optional, integer) Filter results by priority: For example: enter P1, to get Priority 1 bugs assoicated with a Product.)
        """
        InputSet._set_input(self, 'Priority', value)
    def set_Product(self, value):
        """
        Set the value of the Product input for this Choreo. ((required, string) Enter the Mozilla product for which bugs will be retrieved. For example: Bugzilla)
        """
        InputSet._set_input(self, 'Product', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        InputSet._set_input(self, 'Server', value)
    def set_Severity(self, value):
        """
        Set the value of the Severity input for this Choreo. ((optional, string) Filter results by severity. For example: blocker)
        """
        InputSet._set_input(self, 'Severity', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Bugzilla username.)
        """
        InputSet._set_input(self, 'Username', value)

class SearchForBugsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchForBugs Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class SearchForBugsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchForBugsResultSet(response, path)
