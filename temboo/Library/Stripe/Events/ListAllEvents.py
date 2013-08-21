# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllEvents
# Returns a list of events that have happened in your account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListAllEvents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllEvents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Events/ListAllEvents')


    def new_input_set(self):
        return ListAllEventsInputSet()

    def _make_result_set(self, result, path):
        return ListAllEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllEventsChoreographyExecution(session, exec_id, path)

class ListAllEventsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllEvents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) A limit on the number of events to be returned. Count can range between 1 and 100 items.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_Created(self, value):
        """
        Set the value of the Created input for this Choreo. ((optional, date) Filters the result based on the event created date (a UTC timestamp).)
        """
        InputSet._set_input(self, 'Created', value)
    def set_GreaterThanEqualTo(self, value):
        """
        Set the value of the GreaterThanEqualTo input for this Choreo. ((optional, date) Returns events that have been created after or equal to this UTC timestamp.)
        """
        InputSet._set_input(self, 'GreaterThanEqualTo', value)
    def set_GreaterThan(self, value):
        """
        Set the value of the GreaterThan input for this Choreo. ((optional, date) Returns events that have been created after this UTC timestamp.)
        """
        InputSet._set_input(self, 'GreaterThan', value)
    def set_LessThanEqualTo(self, value):
        """
        Set the value of the LessThanEqualTo input for this Choreo. ((optional, date) Return events that were created before or equal to this UTC timestamp.)
        """
        InputSet._set_input(self, 'LessThanEqualTo', value)
    def set_LessThan(self, value):
        """
        Set the value of the LessThan input for this Choreo. ((optional, date) Return events that were created before this UTC timestamp.)
        """
        InputSet._set_input(self, 'LessThan', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) An offset into your events array. The API will return the requested number of events starting at that offset.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) A string containing a specific event name, or group of events using * as a wildcard. This will return a filtered result including only events with a matching event property.)
        """
        InputSet._set_input(self, 'Type', value)

class ListAllEventsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllEvents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class ListAllEventsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllEventsResultSet(response, path)
