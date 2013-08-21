# -*- coding: utf-8 -*-

###############################################################################
#
# GetTimeSeriesByPeriod
# Gets time series data for a given resource based on a date range period you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTimeSeriesByPeriod(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTimeSeriesByPeriod Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/Statistics/GetTimeSeriesByPeriod')


    def new_input_set(self):
        return GetTimeSeriesByPeriodInputSet()

    def _make_result_set(self, result, path):
        return GetTimeSeriesByPeriodResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTimeSeriesByPeriodChoreographyExecution(session, exec_id, path)

class GetTimeSeriesByPeriodInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTimeSeriesByPeriod
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((required, date) The end date of the period for the data you want to retrieve (in the format yyyy-MM-dd). You can also specify the value 'today'.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Period(self, value):
        """
        Set the value of the Period input for this Choreo. ((optional, string) The date range period. Valid values are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max. Defaults to 'max'.)
        """
        InputSet._set_input(self, 'Period', value)
    def set_ResourcePath(self, value):
        """
        Set the value of the ResourcePath input for this Choreo. ((required, string) The resource path that you want to access (for example: activities/log/distance). See Choreo documentation for a full list of resource paths.)
        """
        InputSet._set_input(self, 'ResourcePath', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        InputSet._set_input(self, 'UserID', value)

class GetTimeSeriesByPeriodResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTimeSeriesByPeriod Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class GetTimeSeriesByPeriodChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTimeSeriesByPeriodResultSet(response, path)
