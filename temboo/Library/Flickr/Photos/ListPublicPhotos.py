# -*- coding: utf-8 -*-

###############################################################################
#
# ListPublicPhotos
# Obtain a list of public photos for a given user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListPublicPhotos(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPublicPhotos Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/ListPublicPhotos')


    def new_input_set(self):
        return ListPublicPhotosInputSet()

    def _make_result_set(self, result, path):
        return ListPublicPhotosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPublicPhotosChoreographyExecution(session, exec_id, path)

class ListPublicPhotosInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPublicPhotos
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Extras(self, value):
        """
        Set the value of the Extras input for this Choreo. ((optional, string) A comma-separated list returning additional photo information such as: license, description, date_upload, date_taken.  Additional options are listed on this method's API doc page.)
        """
        InputSet._set_input(self, 'Extras', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Specify the page of photos that is to be returned.  If unspecified, the first page is returned.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Specify how many photos to display per page. Default is set to: 100. The mamimum allowed value is: 500.)
        """
        InputSet._set_input(self, 'PerPage', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SafeSearch(self, value):
        """
        Set the value of the SafeSearch input for this Choreo. ((optional, integer) Specify a safe search setting by entering: 1 (for safe), 2 (moderate), 3 (restricted).  Default is set to: 1 (safe).)
        """
        InputSet._set_input(self, 'SafeSearch', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) Enter the NSID of the user whose public photos are being retrieved.)
        """
        InputSet._set_input(self, 'UserID', value)

class ListPublicPhotosResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPublicPhotos Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListPublicPhotosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPublicPhotosResultSet(response, path)
