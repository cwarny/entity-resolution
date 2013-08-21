# -*- coding: utf-8 -*-

###############################################################################
#
# GetListByID
# Retrieves a list of NPR categories from a specified list type ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetListByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetListByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/GetListByID')


    def new_input_set(self):
        return GetListByIDInputSet()

    def _make_result_set(self, result, path):
        return GetListByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListByIDChoreographyExecution(session, exec_id, path)

class GetListByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetListByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ChildrenOf(self, value):
        """
        Set the value of the ChildrenOf input for this Choreo. ((optional, integer) Returns only items which are assigned to the given topic ID. For example, if Id=3006 and ChildrenOf=1008 only recent series which are assigned to "Arts & Life" are returned.)
        """
        InputSet._set_input(self, 'ChildrenOf', value)
    def set_HideChildren(self, value):
        """
        Set the value of the HideChildren input for this Choreo. ((optional, boolean) If set to "1", returns only topics which are not subtopics of another topic.)
        """
        InputSet._set_input(self, 'HideChildren', value)
    def set_Id(self, value):
        """
        Set the value of the Id input for this Choreo. ((required, integer) The id of the list type you want to retrieve. For example, the list type id for Music Genres is 3218).)
        """
        InputSet._set_input(self, 'Id', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Set to json or xml (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_StoryCountAll(self, value):
        """
        Set the value of the StoryCountAll input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories.)
        """
        InputSet._set_input(self, 'StoryCountAll', value)
    def set_StoryCountMonth(self, value):
        """
        Set the value of the StoryCountMonth input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published in the last month.)
        """
        InputSet._set_input(self, 'StoryCountMonth', value)
    def set_StoryCountToday(self, value):
        """
        Set the value of the StoryCountToday input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published today.)
        """
        InputSet._set_input(self, 'StoryCountToday', value)

class GetListByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetListByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from NPR.)
        """
        return self._output.get('Response', None)

class GetListByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListByIDResultSet(response, path)
