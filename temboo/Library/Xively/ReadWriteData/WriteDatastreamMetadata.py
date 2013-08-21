# -*- coding: utf-8 -*-

###############################################################################
#
# WriteDatastreamMetadata
# Allows you to easily update the metadata of your datastream.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class WriteDatastreamMetadata(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WriteDatastreamMetadata Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/ReadWriteData/WriteDatastreamMetadata')


    def new_input_set(self):
        return WriteDatastreamMetadataInputSet()

    def _make_result_set(self, result, path):
        return WriteDatastreamMetadataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WriteDatastreamMetadataChoreographyExecution(session, exec_id, path)

class WriteDatastreamMetadataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WriteDatastreamMetadata
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CustomDatastreamData(self, value):
        """
        Set the value of the CustomDatastreamData input for this Choreo. ((optional, json) Custom data body for the updated datastream in JSON. See documentation for how to construct your own datastream feed. If custom DatastreamData is used, all other optional inputs are ignored.)
        """
        InputSet._set_input(self, 'CustomDatastreamData', value)
    def set_DatastreamID(self, value):
        """
        Set the value of the DatastreamID input for this Choreo. ((required, string) The ID of the Datastream you would like to add metadata to. Required unless you are using CustomDatastreamData.)
        """
        InputSet._set_input(self, 'DatastreamID', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, integer) The ID for the feed that you would like to update.)
        """
        InputSet._set_input(self, 'FeedID', value)
    def set_MaxValue(self, value):
        """
        Set the value of the MaxValue input for this Choreo. ((optional, string) The maximum value since the last reset. Leave empty to keep existing MaxValue. Type "BLANK" to clear existing value.)
        """
        InputSet._set_input(self, 'MaxValue', value)
    def set_MinValue(self, value):
        """
        Set the value of the MinValue input for this Choreo. ((optional, string) The minimum value since the last reset. Leave empty to keep existing MinValue. Type "BLANK" to clear existing value.)
        """
        InputSet._set_input(self, 'MinValue', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Comma-separated list of searchable tags (the characters ', ", and commas are not allowed). Tags input overwrites previous tags, enter "BLANK" to clear all tags. Ex: "power,energy".)
        """
        InputSet._set_input(self, 'Tags', value)
    def set_UnitSymbol(self, value):
        """
        Set the value of the UnitSymbol input for this Choreo. ((optional, string) The symbol of the Unit. Leave empty to keep existing UnitSymbol. Type "BLANK" to clear existing value. Ex: "C".)
        """
        InputSet._set_input(self, 'UnitSymbol', value)
    def set_UnitType(self, value):
        """
        Set the value of the UnitType input for this Choreo. ((optional, string) The type of Unit. Leave empty to keep existing UnitType. Type "BLANK" to clear existing value. Ex: "basicSI".)
        """
        InputSet._set_input(self, 'UnitType', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) The units of the datastream. Leave empty to keep existing Units. Type "BLANK" to clear existing Units. Ex: "Celsius".)
        """
        InputSet._set_input(self, 'Units', value)

class WriteDatastreamMetadataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WriteDatastreamMetadata Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful datastream update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class WriteDatastreamMetadataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WriteDatastreamMetadataResultSet(response, path)
