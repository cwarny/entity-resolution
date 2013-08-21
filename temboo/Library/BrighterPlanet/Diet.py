# -*- coding: utf-8 -*-

###############################################################################
#
# Diet
# Returns information about the carbon footprint of an individual's yearly food consumption.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Diet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Diet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Diet')


    def new_input_set(self):
        return DietInputSet()

    def _make_result_set(self, result, path):
        return DietResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DietChoreographyExecution(session, exec_id, path)

class DietInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Diet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DietClass(self, value):
        """
        Set the value of the DietClass input for this Choreo. ((optional, string) Enter the type of diet. Acceptable inputs: standard, vegetarian, vegan.)
        """
        InputSet._set_input(self, 'DietClass', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) End date od diet in YYYY-MM-DD format. Defaults to 2013-01-01 when none specified.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Size(self, value):
        """
        Set the value of the Size input for this Choreo. ((required, integer) Enter the number of calories consumed per day. See documentation below for a set of national averages for reference.)
        """
        InputSet._set_input(self, 'Size', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) Start date of diet in YYYY-MM-DD format. Defaults to 2012-01-01 when none specified.)
        """
        InputSet._set_input(self, 'StartDate', value)

class DietResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Diet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class DietChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DietResultSet(response, path)
