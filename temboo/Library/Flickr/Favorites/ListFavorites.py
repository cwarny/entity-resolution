# -*- coding: utf-8 -*-

###############################################################################
#
# ListFavorites
# Returns a list of the user's favorite photos.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListFavorites(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListFavorites Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Favorites/ListFavorites')


    def new_input_set(self):
        return ListFavoritesInputSet()

    def _make_result_set(self, result, path):
        return ListFavoritesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListFavoritesChoreographyExecution(session, exec_id, path)

class ListFavoritesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListFavorites
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'APISecret', value)
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
        Set the value of the UserID input for this Choreo. ((required, string) The NSID of the user to fetch the favorites list for. If this argument is omitted, the favorites list for the calling user is returned.)
        """
        InputSet._set_input(self, 'UserID', value)

class ListFavoritesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListFavorites Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListFavoritesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListFavoritesResultSet(response, path)
