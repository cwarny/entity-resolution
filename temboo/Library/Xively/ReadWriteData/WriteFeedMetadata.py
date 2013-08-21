# -*- coding: utf-8 -*-

###############################################################################
#
# WriteFeedMetadata
# Allows you to easily update the metadata of your feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class WriteFeedMetadata(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WriteFeedMetadata Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/ReadWriteData/WriteFeedMetadata')


    def new_input_set(self):
        return WriteFeedMetadataInputSet()

    def _make_result_set(self, result, path):
        return WriteFeedMetadataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WriteFeedMetadataChoreographyExecution(session, exec_id, path)

class WriteFeedMetadataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WriteFeedMetadata
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FeedData(self, value):
        """
        Set the value of the FeedData input for this Choreo. ((optional, any) Custom data body for the new feed in JSON or XML format (set by FeedType). See documentation for how to write your own feed. If custom FeedData is used, all other optional inputs are ignored.)
        """
        InputSet._set_input(self, 'FeedData', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description of the feed. Leave empty to keep existing Description. Type "BLANK" to clear existing Description.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) Contact Email. Leave empty to keep existing Email. Type "BLANK" to clear existing Email.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, integer) The ID for the feed that you would like to update.)
        """
        InputSet._set_input(self, 'FeedID', value)
    def set_FeedType(self, value):
        """
        Set the value of the FeedType input for this Choreo. ((optional, string) The type of feed that is being provided for custom FeedData. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'FeedType', value)
    def set_Icon(self, value):
        """
        Set the value of the Icon input for this Choreo. ((optional, string) The URL of an icon which is relevant to this feed. Leave empty to keep existing Icon. Type "BLANK" to clear existing Icon.)
        """
        InputSet._set_input(self, 'Icon', value)
    def set_Private(self, value):
        """
        Set the value of the Private input for this Choreo. ((optional, boolean) Specifies whether or not the feed is private to the creator of the feed. If 'true' the feed is private, if 'false' the feed is public. Leave empty to keep existing settings.)
        """
        InputSet._set_input(self, 'Private', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Comma-separated list of searchable tags (the characters ', ", and commas are not allowed). Tags input overwrites previous tags, enter "BLANK" to clear all tags. Ex: "power,energy".)
        """
        InputSet._set_input(self, 'Tags', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) A descriptive name for the feed. Leave empty to keep existing Title. Type "BLANK" to clear existing Title.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Website(self, value):
        """
        Set the value of the Website input for this Choreo. ((optional, string) The URL of a website which is relevant to this feed. Leave empty to keep existing Website. Type "BLANK" to clear existing Website. Ex.: http://www.homepage.com.)
        """
        InputSet._set_input(self, 'Website', value)

class WriteFeedMetadataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WriteFeedMetadata Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful feed update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class WriteFeedMetadataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WriteFeedMetadataResultSet(response, path)
