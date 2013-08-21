# -*- coding: utf-8 -*-

###############################################################################
#
# FilterByItems
# Retrieves the stats for just a single item for the type you are requesting.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FilterByItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FilterByItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Clicky/FilterByItems')


    def new_input_set(self):
        return FilterByItemsInputSet()

    def _make_result_set(self, result, path):
        return FilterByItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterByItemsChoreographyExecution(session, exec_id, path)

class FilterByItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FilterByItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Item(self, value):
        """
        Set the value of the Item input for this Choreo. ((required, string) Use this input to get the stats for just a single item for the type you are requesting (i.e. type=links-domains and item=google.com).)
        """
        InputSet._set_input(self, 'Item', value)
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

class FilterByItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FilterByItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Clicky formatted as specified in the Output parameter. Default is XML.)
        """
        return self._output.get('Response', None)

class FilterByItemsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FilterByItemsResultSet(response, path)
