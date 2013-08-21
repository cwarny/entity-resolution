# -*- coding: utf-8 -*-

###############################################################################
#
# ListGalleries
# Get a gallery list for a specfied user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListGalleries(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListGalleries Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Galleries/ListGalleries')


    def new_input_set(self):
        return ListGalleriesInputSet()

    def _make_result_set(self, result, path):
        return ListGalleriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListGalleriesChoreographyExecution(session, exec_id, path)

class ListGalleriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListGalleries
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Enter the number of results pages to be returned.  Default is: 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Specify the number of galleries that are to be returned per page.  If null, defaults to 100 galleries returned.  Maximum is 500.)
        """
        InputSet._set_input(self, 'PerPage', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) Provide the NSID for the user whose gallery list(s) are to be retreived.)
        """
        InputSet._set_input(self, 'UserID', value)

class ListGalleriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListGalleries Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListGalleriesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListGalleriesResultSet(response, path)
