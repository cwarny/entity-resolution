# -*- coding: utf-8 -*-

###############################################################################
#
# ListPublicFavorites
# Returns a list of favorite public photos for the given user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListPublicFavorites(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPublicFavorites Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Favorites/ListPublicFavorites')


    def new_input_set(self):
        return ListPublicFavoritesInputSet()

    def _make_result_set(self, result, path):
        return ListPublicFavoritesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPublicFavoritesChoreographyExecution(session, exec_id, path)

class ListPublicFavoritesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPublicFavorites
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Extras(self, value):
        """
        Set the value of the Extras input for this Choreo. ((optional, string) A comma-delimited list of extra information to fetch for each returned record. See Choreo documentation for accepted values.)
        """
        InputSet._set_input(self, 'Extras', value)
    def set_MaxFaveDate(self, value):
        """
        Set the value of the MaxFaveDate input for this Choreo. ((optional, date) Maximum date that a photo was favorited on. The date should be in the form of a unix timestamp.)
        """
        InputSet._set_input(self, 'MaxFaveDate', value)
    def set_MinFaveDate(self, value):
        """
        Set the value of the MinFaveDate input for this Choreo. ((optional, date) Minimum date that a photo was favorited on. The date should be in the form of a unix timestamp.)
        """
        InputSet._set_input(self, 'MinFaveDate', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to return. Used for paging through many results.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of photos to return per page. Defaults to 100.)
        """
        InputSet._set_input(self, 'PerPage', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The user to fetch the favorites list for.)
        """
        InputSet._set_input(self, 'UserID', value)

class ListPublicFavoritesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPublicFavorites Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListPublicFavoritesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPublicFavoritesResultSet(response, path)
