# -*- coding: utf-8 -*-

###############################################################################
#
# PhotoTags
# Retrieves a list of photos associated with a specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Facebook.FacebookPhotoTag import FacebookPhotoTag

import json

class PhotoTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PhotoTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Reading/PhotoTags')


    def new_input_set(self):
        return PhotoTagsInputSet()

    def _make_result_set(self, result, path):
        return PhotoTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PhotoTagsChoreographyExecution(session, exec_id, path)

class PhotoTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PhotoTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return (i.e. id,name).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Used to page through results. Limits the number of records returned in the response.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results. Returns results starting from the specified number.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to retrieve photo tags for. Defaults to "me" indicating the authenticated user.)
        """
        InputSet._set_input(self, 'ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((optional, date) Used for time-based pagination. Values can be a unix timestamp or any date accepted by strtotime.)
        """
        InputSet._set_input(self, 'Since', value)
    def set_Until(self, value):
        """
        Set the value of the Until input for this Choreo. ((optional, date) Used for time-based pagination. Values can be a unix timestamp or any date accepted by strtotime.)
        """
        InputSet._set_input(self, 'Until', value)

class PhotoTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PhotoTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_HasNext(self):
        """
        Retrieve the value for the "HasNext" output from this Choreo execution. ((boolean) A boolean flag indicating that a next page exists.)
        """
        return self._output.get('HasNext', None)
    def get_HasPrevious(self):
        """
        Retrieve the value for the "HasPrevious" output from this Choreo execution. ((boolean) A boolean flag indicating that a previous page exists.)
        """
        return self._output.get('HasPrevious', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getPhotoTags(self):
        """
        Get the user's photo
        """
        return [FacebookPhotoTag(le) for le in self.getJSONFromString(self._output.get('Response', [])).get("data", [])]


class PhotoTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PhotoTagsResultSet(response, path)
