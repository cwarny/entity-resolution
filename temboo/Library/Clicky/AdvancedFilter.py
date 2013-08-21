# -*- coding: utf-8 -*-

###############################################################################
#
# AdvancedFilter
# Allows you to retrieve analytics, using more advanced filter options.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AdvancedFilter(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AdvancedFilter Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Clicky/AdvancedFilter')


    def new_input_set(self):
        return AdvancedFilterInputSet()

    def _make_result_set(self, result, path):
        return AdvancedFilterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AdvancedFilterChoreographyExecution(session, exec_id, path)

class AdvancedFilterInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AdvancedFilter
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) The date or date range you want to access. Use YYYY-MM-DD format for date and YYYY-MM-DD,YYYY-MM-DD for a range. See docs for more options for this input. Defaults to 'today'.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_FilterName(self, value):
        """
        Set the value of the FilterName input for this Choreo. ((required, string) The name of the data you want to filter by (i.e. ip_address). See docs for a complete list of supported filters.)
        """
        InputSet._set_input(self, 'FilterName', value)
    def set_FilterValue(self, value):
        """
        Set the value of the FilterValue input for this Choreo. ((required, string) The value of the filter you want to apply to the request. For example, if you're FilterName is "ip_address", you could use "65.0.0.0,85.0.0.0" in the FilterValue.)
        """
        InputSet._set_input(self, 'FilterValue', value)
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
        Set the value of the Type input for this Choreo. ((required, string) The type of data you want to retrieve. Note that not all types are available for this Choreo. Use types: vistors-list, segmentation, or actions-list.)
        """
        InputSet._set_input(self, 'Type', value)

class AdvancedFilterResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AdvancedFilter Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Clicky formatted as specified in the Output parameter. Default is XML.)
        """
        return self._output.get('Response', None)

class AdvancedFilterChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AdvancedFilterResultSet(response, path)
