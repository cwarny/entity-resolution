# -*- coding: utf-8 -*-

###############################################################################
#
# TopicData
# Retrieves topic data for a given topic, including an abbreviated list of all its sub-topics.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TopicData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TopicData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Topics/TopicData')


    def new_input_set(self):
        return TopicDataInputSet()

    def _make_result_set(self, result, path):
        return TopicDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopicDataChoreographyExecution(session, exec_id, path)

class TopicDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TopicData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_TopicID(self, value):
        """
        Set the value of the TopicID input for this Choreo. ((required, string) The ID of the topic.)
        """
        InputSet._set_input(self, 'TopicID', value)

class TopicDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TopicData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class TopicDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopicDataResultSet(response, path)
