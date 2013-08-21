# -*- coding: utf-8 -*-

###############################################################################
#
# GetCategoryStatistics
# Obtain statistics by specified categories.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetCategoryStatistics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCategoryStatistics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Statistics/GetCategoryStatistics')


    def new_input_set(self):
        return GetCategoryStatisticsInputSet()

    def _make_result_set(self, result, path):
        return GetCategoryStatisticsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCategoryStatisticsChoreographyExecution(session, exec_id, path)

class GetCategoryStatisticsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCategoryStatistics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        InputSet._set_input(self, 'APIUser', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((required, string) The category for which statistics will be retrieved. It must be an existing category that has statistics. If the category entered does not exist, an empty result set will be returned.)
        """
        InputSet._set_input(self, 'Category', value)
    def set_Days(self, value):
        """
        Set the value of the Days input for this Choreo. ((optional, integer) The number of days (greater than 0) for which block data will be retrieved. Note that you can use either the days parameter or the start_date and end_date parameter.)
        """
        InputSet._set_input(self, 'Days', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) The end of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) The start of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format, and must be earlier than the EndDate variable value. Use this ,or Days.)
        """
        InputSet._set_input(self, 'StartDate', value)


class GetCategoryStatisticsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCategoryStatistics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class GetCategoryStatisticsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCategoryStatisticsResultSet(response, path)
