# -*- coding: utf-8 -*-

###############################################################################
#
# ListPhotosWithoutGeoTags
# Returns a list of your photos which haven't been geo-tagged.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListPhotosWithoutGeoTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPhotosWithoutGeoTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/ListPhotosWithoutGeoTags')


    def new_input_set(self):
        return ListPhotosWithoutGeoTagsInputSet()

    def _make_result_set(self, result, path):
        return ListPhotosWithoutGeoTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPhotosWithoutGeoTagsChoreographyExecution(session, exec_id, path)

class ListPhotosWithoutGeoTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPhotosWithoutGeoTags
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
        Set the value of the Extras input for this Choreo. ((optional, string) A comma-delimited list of extra information to retrieve for each returned record. See Choreo documentation for accepted values.)
        """
        InputSet._set_input(self, 'Extras', value)
    def set_MaxTakenDate(self, value):
        """
        Set the value of the MaxTakenDate input for this Choreo. ((optional, date) Photos with an taken date less than or equal to this value will be returned. The date should be in the form of a mysql datetime.)
        """
        InputSet._set_input(self, 'MaxTakenDate', value)
    def set_MaxUploadDate(self, value):
        """
        Set the value of the MaxUploadDate input for this Choreo. ((optional, date) Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.)
        """
        InputSet._set_input(self, 'MaxUploadDate', value)
    def set_Media(self, value):
        """
        Set the value of the Media input for this Choreo. ((optional, string) Filter results by media type. Possible values are all (default), photos or videos.)
        """
        InputSet._set_input(self, 'Media', value)
    def set_MinTakenDate(self, value):
        """
        Set the value of the MinTakenDate input for this Choreo. ((optional, date) Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime.)
        """
        InputSet._set_input(self, 'MinTakenDate', value)
    def set_MinUploadDate(self, value):
        """
        Set the value of the MinUploadDate input for this Choreo. ((optional, date) Photos with an upload date greater than or equal to this value will be returned. The date should be in the form of a unix timestamp.)
        """
        InputSet._set_input(self, 'MinUploadDate', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to return. Used for paging through many results. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.)
        """
        InputSet._set_input(self, 'PerPage', value)
    def set_PrivacyFilter(self, value):
        """
        Set the value of the PrivacyFilter input for this Choreo. ((optional, integer) Valid values are: 1 (public photos), 2 (private photos visible to friends), 3 (private photos visible to family), 4 (private photos visible to friends and family), 5 (completely private photos).)
        """
        InputSet._set_input(self, 'PrivacyFilter', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) )
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) The sort order. Accepted values are: date-posted-asc, date-posted-desc, date-taken-asc, date-taken-desc, interestingness-desc, and interestingness-asc.)
        """
        InputSet._set_input(self, 'Sort', value)

class ListPhotosWithoutGeoTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPhotosWithoutGeoTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListPhotosWithoutGeoTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPhotosWithoutGeoTagsResultSet(response, path)
