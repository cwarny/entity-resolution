# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllTimeCategoryTotals
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

class GetAllTimeCategoryTotals(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAllTimeCategoryTotals Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Statistics/GetAllTimeCategoryTotals')


    def new_input_set(self):
        return GetAllTimeCategoryTotalsInputSet()

    def _make_result_set(self, result, path):
        return GetAllTimeCategoryTotalsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllTimeCategoryTotalsChoreographyExecution(session, exec_id, path)

class GetAllTimeCategoryTotalsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAllTimeCategoryTotals
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
    def set_Aggregate(self, value):
        """
        Set the value of the Aggregate input for this Choreo. ((required, integer) Retrieve category statistics.  Default is set to 1.)
        """
        InputSet._set_input(self, 'Aggregate', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((required, string) Enter a category for which statistics will be retrieved. It must be an existing category that has statistics. If the category entered does not exist, an empty result set will be returned.)
        """
        InputSet._set_input(self, 'Category', value)
    def set_Days(self, value):
        """
        Set the value of the Days input for this Choreo. ((optional, integer) The number of days (greater than 0) for which block data will be retrieved. Note that you can use either the days parameter or the start_date and end_date parameter.)
        """
        InputSet._set_input(self, 'Days', value)
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


class GetAllTimeCategoryTotalsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAllTimeCategoryTotals Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class GetAllTimeCategoryTotalsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAllTimeCategoryTotalsResultSet(response, path)
