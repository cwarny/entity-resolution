# -*- coding: utf-8 -*-

###############################################################################
#
# FilterByKeyword
# Retrieves analytics, filtering down to only the results you specify in a keyword filter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FilterByKeyword(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FilterByKeyword Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Clicky/FilterByKeyword')


    def new_input_set(self):
        return FilterByKeywordInputSet()

    def _make_result_set(self, result, path):
        return FilterByKeywordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterByKeywordChoreographyExecution(session, exec_id, path)

class FilterByKeywordInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FilterByKeyword
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((required, string) You can use this parameter to filter down to only the results you want.)
        """
        InputSet._set_input(self, 'Filter', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The maximum number of results that will be returned. Defaults to 10.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Output(self, value):
        """
        Set the value of the Output input for this Choreo. ((optional, string) What format you want the returned data to be in. Accepted values: xml, php, json, csv. Defaults to 'xml'.)
        """
        InputSet._set_input(self, 'Output', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((required, integer) Your request must include the site's ID that you want to access data from. Available from your site preferences page.)
        """
        InputSet._set_input(self, 'SiteID', value)
    def set_SiteKey(self, value):
        """
        Set the value of the SiteKey input for this Choreo. ((required, string) The unique key assigned to you when you first register with Clicky. Available from your site preferences page.)
        """
        InputSet._set_input(self, 'SiteKey', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((required, string) The type of data you want to retrieve. Can be a comma-separated list of types (i.e. visitors,countries,searches).)
        """
        InputSet._set_input(self, 'Type', value)

class FilterByKeywordResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FilterByKeyword Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Clicky formatted as specified in the Output parameter. Default is XML.)
        """
        return self._output.get('Response', None)

class FilterByKeywordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FilterByKeywordResultSet(response, path)
