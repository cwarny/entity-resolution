# -*- coding: utf-8 -*-

###############################################################################
#
# CreateEvent
# Creates a new event.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateEvent(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateEvent Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/OneLogin/Events/CreateEvent')


    def new_input_set(self):
        return CreateEventInputSet()

    def _make_result_set(self, result, path):
        return CreateEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEventChoreographyExecution(session, exec_id, path)

class CreateEventInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateEvent
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by OneLogin.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_EventTypeID(self, value):
        """
        Set the value of the EventTypeID input for this Choreo. ((required, integer) The id for the type of event you want to create. Note that depending on the event type id specified, you may need to provide the ObjectName and ObjectID that is being affected.)
        """
        InputSet._set_input(self, 'EventTypeID', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((conditional, integer) The object id that is being affected. Required for certain event types. When specified, ObjectName must also be provided.)
        """
        InputSet._set_input(self, 'ObjectID', value)
    def set_ObjectName(self, value):
        """
        Set the value of the ObjectName input for this Choreo. ((conditional, string) The object name that is being affected (i.e. user-id). Required for certain event types. When specified, ObjectID must also be provided.)
        """
        InputSet._set_input(self, 'ObjectName', value)

class CreateEventResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateEvent Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from OneLogin.)
        """
        return self._output.get('Response', None)

class CreateEventChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateEventResultSet(response, path)
