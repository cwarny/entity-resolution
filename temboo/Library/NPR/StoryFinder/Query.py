# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Queries the Story API for stories across all NPR media, including audio, text, images, and web-only content.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Query(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Query Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/Query')


    def new_input_set(self):
        return QueryInputSet()

    def _make_result_set(self, result, path):
        return QueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryChoreographyExecution(session, exec_id, path)

class QueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Query
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, multiline) The API Key provided by NPR.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DateType(self, value):
        """
        Set the value of the DateType input for this Choreo. ((optional, string) Controls the meaning of StartDate and EndDate. Values can be story or correction.)
        """
        InputSet._set_input(self, 'DateType', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) The exact date for which stories will be returned. Format: YYYY-MM-DD The special value current is also allowed. Cannot be used with StartDate or EndDate.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) The end date for which stories will be returned. Format: YYYY-MM-DD Can be used with StartDate to search a range. Cannot be used with Date. The meaning of this parameter can be modified with DateType.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Comma-delimited list of fields to be returned in the output for the results. List of fields can be made up of selectable fields or compilation fields. Defaults to all available fields.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_IDBoolean(self, value):
        """
        Set the value of the IDBoolean input for this Choreo. ((optional, string) Describes how IDs are searched. Allowed values: and, or, union.)
        """
        InputSet._set_input(self, 'IDBoolean', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((optional, string) Comma-delimited list of ID numbers corresponding to topics, music genres, programs, blogs, bios, music artists, and series.)
        """
        InputSet._set_input(self, 'ID', value)
    def set_NumResults(self, value):
        """
        Set the value of the NumResults input for this Choreo. ((optional, integer) The number of stories to be returned up to 20 maximum.)
        """
        InputSet._set_input(self, 'NumResults', value)
    def set_OrgID(self, value):
        """
        Set the value of the OrgID input for this Choreo. ((optional, string) Comma-delimited list of ID numbers of local stations.)
        """
        InputSet._set_input(self, 'OrgID', value)
    def set_RequiredAssets(self, value):
        """
        Set the value of the RequiredAssets input for this Choreo. ((optional, string) Comma-delimited list that limits the resulting set to contain only stories with a particular type of asset. Allowed values: audio, image, text, and correction.)
        """
        InputSet._set_input(self, 'RequiredAssets', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Enter output format. Values accepted: NPRML, RSS, MediaRSS, Podcast, ATOM, JSON, HTML WIdget, Javascript Widget. Default is JSON.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SearchTerm(self, value):
        """
        Set the value of the SearchTerm input for this Choreo. ((optional, string) Term to search in NPR's search engine. Can be used with SearchType to specify which fields should be searched.)
        """
        InputSet._set_input(self, 'SearchTerm', value)
    def set_SearchType(self, value):
        """
        Set the value of the SearchType input for this Choreo. ((optional, string) Used with SearchTerm to specify which fields should be searched. Default searches all fields. Allowed values: main and full.)
        """
        InputSet._set_input(self, 'SearchType', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Determines the order in which the stories will be returned. Default is date descending. Other allowed values: date ascending, editor assigned, and featured.)
        """
        InputSet._set_input(self, 'Sort', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) The start date for which stories will be returned. Format: YYYY-MM-DD Can be used with EndDate to search a range. Cannot be used with Date. The meaning of this parameter can be modified with DateType.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_StartNum(self, value):
        """
        Set the value of the StartNum input for this Choreo. ((optional, integer) Determines where in the result set to start returning stories.)
        """
        InputSet._set_input(self, 'StartNum', value)

class QueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Query Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from NPR.)
        """
        return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
