# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllFeeds
# Returns filterable data on all feeds viewable by the authenticated account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListAllFeeds(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllFeeds Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/ReadWriteData/ListAllFeeds')


    def new_input_set(self):
        return ListAllFeedsInputSet()

    def _make_result_set(self, result, path):
        return ListAllFeedsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllFeedsChoreographyExecution(session, exec_id, path)

class ListAllFeedsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllFeeds
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Content(self, value):
        """
        Set the value of the Content input for this Choreo. ((optional, string) Describes whether to return full or summary results. Full - all datastream values are returned, summary - returns the environment metadata for each feed. Valid values: 'full' or 'summary'.)
        """
        InputSet._set_input(self, 'Content', value)
    def set_DistanceUnits(self, value):
        """
        Set the value of the DistanceUnits input for this Choreo. ((optional, string) Units of distance. Valid values: "miles" or "kms" (default).)
        """
        InputSet._set_input(self, 'DistanceUnits', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((optional, decimal) Search radius (units like miles or kilometers defined by DistanceUnits). Ex: 5.0.)
        """
        InputSet._set_input(self, 'Distance', value)
    def set_FeedType(self, value):
        """
        Set the value of the FeedType input for this Choreo. ((optional, string) The type of feed that is being returned. Valid values are "json" (the default), "xml" and "csv". No metadata is returned for the csv feed.)
        """
        InputSet._set_input(self, 'FeedType', value)
    def set_FullTextSearch(self, value):
        """
        Set the value of the FullTextSearch input for this Choreo. ((optional, string) Returns any feeds matching this string.)
        """
        InputSet._set_input(self, 'FullTextSearch', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) Used to find feeds located around this latitude. Ex. 51.5235375648154.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) Used to find feeds located around this longitude. Ex: -0.0807666778564453.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Indicates which page of results you are requesting. Starts from 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Defines how many results to return per page (1 to 1000).)
        """
        InputSet._set_input(self, 'PerPage', value)
    def set_ShowUser(self, value):
        """
        Set the value of the ShowUser input for this Choreo. ((optional, string) Include user login and user level for each feed. Valid values: true, false (default).)
        """
        InputSet._set_input(self, 'ShowUser', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Order of returned feeds. Valid values: "created_at", "retrieved_at" or "relevance".)
        """
        InputSet._set_input(self, 'SortOrder', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) Sets whether to search for only live feeds, only frozen feeds, or all feeds. Valid values: "live", "frozen", "all" (default).)
        """
        InputSet._set_input(self, 'Status', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((optional, string) Returns feeds containing datastreams tagged with the search query.)
        """
        InputSet._set_input(self, 'Tag', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) Returns feeds containing datastreams with units specified by the search query. Ex: Celsius.)
        """
        InputSet._set_input(self, 'Units', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((optional, string) Returns feeds created by the user specified.)
        """
        InputSet._set_input(self, 'User', value)

class ListAllFeedsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllFeeds Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Xively.)
        """
        return self._output.get('Response', None)

class ListAllFeedsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllFeedsResultSet(response, path)
