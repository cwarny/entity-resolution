# -*- coding: utf-8 -*-

###############################################################################
#
# SearchJobsByJobTitle
# Retrieve jobs matching specified job title.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchJobsByJobTitle(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchJobsByJobTitle Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Jobs/SearchJobsByJobTitle')


    def new_input_set(self):
        return SearchJobsByJobTitleInputSet()

    def _make_result_set(self, result, path):
        return SearchJobsByJobTitleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchJobsByJobTitleChoreographyExecution(session, exec_id, path)

class SearchJobsByJobTitleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchJobsByJobTitle
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specify the number of jobs to be returned.  Default is 10.  The maximum is 20.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_JobTitle(self, value):
        """
        Set the value of the JobTitle input for this Choreo. ((required, integer) Search by job title.)
        """
        InputSet._set_input(self, 'JobTitle', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'SecretKey', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Specify the ordering of results. Enter R (for relationship from job to member); DA (dated posted in ascending order); DO (job posted in descending order).)
        """
        InputSet._set_input(self, 'Sort', value)

class SearchJobsByJobTitleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchJobsByJobTitle Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from LinkedIn in XML format.)
        """
        return self._output.get('Response', None)

class SearchJobsByJobTitleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchJobsByJobTitleResultSet(response, path)
