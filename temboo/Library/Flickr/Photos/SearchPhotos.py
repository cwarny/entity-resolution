# -*- coding: utf-8 -*-

###############################################################################
#
# SearchPhotos
# Returns a list of photos matching a search criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchPhotos(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchPhotos Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/SearchPhotos')


    def new_input_set(self):
        return SearchPhotosInputSet()

    def _make_result_set(self, result, path):
        return SearchPhotosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchPhotosChoreographyExecution(session, exec_id, path)

class SearchPhotosInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchPhotos
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((optional, integer) The accuracy level of the location information. Current range is 1-16. World level is 1, Country is ~3, Region is ~6, City is ~11, Street is ~16.)
        """
        InputSet._set_input(self, 'Accuracy', value)
    def set_BoundingBox(self, value):
        """
        Set the value of the BoundingBox input for this Choreo. ((optional, string) A comma-delimited list of 4 values defining the Bounding Box of the area that will be searched. These values represent the coordinates of the bottom-left corner and top-right corner of the box.)
        """
        InputSet._set_input(self, 'BoundingBox', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, integer) The content type setting. 1 = photos only, 2 = screenshots only, 3 = other, 4 = photos and screenshots, 5 = screenshots and other, 6 = photos and other, 7 = all.)
        """
        InputSet._set_input(self, 'ContentType', value)
    def set_Extras(self, value):
        """
        Set the value of the Extras input for this Choreo. ((optional, string) A comma-delimited list of extra information to fetch for each returned record. See documentation for more details on supported fields.)
        """
        InputSet._set_input(self, 'Extras', value)
    def set_GeoContext(self, value):
        """
        Set the value of the GeoContext input for this Choreo. ((optional, integer) A numeric value representing the photo's location info beyond latitude and longitude. 0 = not defined, 1 = indoors, 2 = outdoors.)
        """
        InputSet._set_input(self, 'GeoContext', value)
    def set_GroupID(self, value):
        """
        Set the value of the GroupID input for this Choreo. ((optional, string) The id of a group who's pool to search. If specified, only matching photos posted to the group's pool will be returned.)
        """
        InputSet._set_input(self, 'GroupID', value)
    def set_InGallery(self, value):
        """
        Set the value of the InGallery input for this Choreo. ((optional, boolean) Limits the search to only photos that are in a gallery. Default is false.)
        """
        InputSet._set_input(self, 'InGallery', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((conditional, decimal) A valid latitude, in decimal format, for performing geo queries (not required if providing another limiting search parameter).)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) A valid longitude, in decimal format, for performing geo queries (not required if providing another limiting search parameter).)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_MaxTakenDate(self, value):
        """
        Set the value of the MaxTakenDate input for this Choreo. ((optional, date) The maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.)
        """
        InputSet._set_input(self, 'MaxTakenDate', value)
    def set_MaxUploadDate(self, value):
        """
        Set the value of the MaxUploadDate input for this Choreo. ((optional, date) The maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.)
        """
        InputSet._set_input(self, 'MaxUploadDate', value)
    def set_Media(self, value):
        """
        Set the value of the Media input for this Choreo. ((optional, string) Filter results by media type. Valid values are all (default), photos or videos.)
        """
        InputSet._set_input(self, 'Media', value)
    def set_MinTakenDate(self, value):
        """
        Set the value of the MinTakenDate input for this Choreo. ((optional, date) The minimum taken date. Photos with a taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.)
        """
        InputSet._set_input(self, 'MinTakenDate', value)
    def set_MinUploadDate(self, value):
        """
        Set the value of the MinUploadDate input for this Choreo. ((optional, date) The minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.)
        """
        InputSet._set_input(self, 'MinUploadDate', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to return. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of photos to return per page. Defaults to 100.)
        """
        InputSet._set_input(self, 'PerPage', value)
    def set_PlaceID(self, value):
        """
        Set the value of the PlaceID input for this Choreo. ((optional, string) A Flickr place id.)
        """
        InputSet._set_input(self, 'PlaceID', value)
    def set_RadiusUnits(self, value):
        """
        Set the value of the RadiusUnits input for this Choreo. ((optional, string) The unit of measure when doing radial geo queries. Valid values are: "mi" (miles) and "km" (kilometers). The default is "km".)
        """
        InputSet._set_input(self, 'RadiusUnits', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((optional, integer) A valid radius used for geo queries, greater than zero and less than 20 miles (or 32 kilometers). Defaults to 5 (km).)
        """
        InputSet._set_input(self, 'Radius', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Defaults to date-posted-desc unless performing a geo query. Valid values are: date-posted-asc, date-posted-desc, date-taken-asc, date-taken-desc, interestingness-desc, interestingness-asc, relevance.)
        """
        InputSet._set_input(self, 'Sort', value)
    def set_TagMode(self, value):
        """
        Set the value of the TagMode input for this Choreo. ((optional, string) Use the mode 'any' to search using an OR combination of tags. Use 'all' for an AND combnation. Defaults to 'any'.)
        """
        InputSet._set_input(self, 'TagMode', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma-delimited list of tags. Photos with one or more of the tags listed will be returned. You can exclude results that match a term by prepending it with a hyphen.)
        """
        InputSet._set_input(self, 'Tags', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((conditional, string) A keyword search against photo titles, descriptions, or tags. Prepend search term with a hyphen to exclude. Not required if providing another limiting search parameter.)
        """
        InputSet._set_input(self, 'Text', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the user who's photo to search. If this parameter isn't passed, all public photos will be searched. A value of "me" will search against the authenticated user's photos.)
        """
        InputSet._set_input(self, 'UserID', value)
    def set_WOEID(self, value):
        """
        Set the value of the WOEID input for this Choreo. ((optional, string) The unique 'Where on Earth ID' that uniquely represents spatial entities.)
        """
        InputSet._set_input(self, 'WOEID', value)

class SearchPhotosResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchPhotos Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class SearchPhotosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchPhotosResultSet(response, path)
