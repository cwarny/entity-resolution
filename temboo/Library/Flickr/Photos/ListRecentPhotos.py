# -*- coding: utf-8 -*-

###############################################################################
#
# ListRecentPhotos
# Retrieve public photos that have been recently uploaded to Flickr.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListRecentPhotos(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListRecentPhotos Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/ListRecentPhotos')


    def new_input_set(self):
        return ListRecentPhotosInputSet()

    def _make_result_set(self, result, path):
        return ListRecentPhotosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListRecentPhotosChoreographyExecution(session, exec_id, path)

class ListRecentPhotosInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListRecentPhotos
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

class ListRecentPhotosResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListRecentPhotos Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListRecentPhotosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListRecentPhotosResultSet(response, path)
