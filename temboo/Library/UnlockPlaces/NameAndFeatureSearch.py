# -*- coding: utf-8 -*-

###############################################################################
#
# NameAndFeatureSearch
# Searches for names of places with a specified feature type.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class NameAndFeatureSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the NameAndFeatureSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/UnlockPlaces/NameAndFeatureSearch')


    def new_input_set(self):
        return NameAndFeatureSearchInputSet()

    def _make_result_set(self, result, path):
        return NameAndFeatureSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NameAndFeatureSearchChoreographyExecution(session, exec_id, path)

class NameAndFeatureSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the NameAndFeatureSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FeatureType(self, value):
        """
        Set the value of the FeatureType input for this Choreo. ((required, string) The feature type that the place is (i.e. "Cities"). See http://unlock.edina.ac.uk/ws/supportedFeatureTypes?format=txt for a complete list of supported Feature Types.)
        """
        InputSet._set_input(self, 'FeatureType', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) The format of the place search results. One of xml, kml, json, georss or txt. Defaults to "xml".)
        """
        InputSet._set_input(self, 'Format', value)
    def set_Gazetteer(self, value):
        """
        Set the value of the Gazetteer input for this Choreo. ((optional, string) The place-name source to take locations from. The options are geonames, os, naturalearth or unlock which combines all the previous. Defaults to "unlock".)
        """
        InputSet._set_input(self, 'Gazetteer', value)
    def set_MaxRows(self, value):
        """
        Set the value of the MaxRows input for this Choreo. ((optional, integer) The maximum number of results to return. Defaults to 20. Cannot exceed 1000.)
        """
        InputSet._set_input(self, 'MaxRows', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) One or more names of places to search for (separated by commas).)
        """
        InputSet._set_input(self, 'Name', value)
    def set_StartRow(self, value):
        """
        Set the value of the StartRow input for this Choreo. ((optional, integer) The row to start results display from. Defaults to 1.)
        """
        InputSet._set_input(self, 'StartRow', value)

class NameAndFeatureSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the NameAndFeatureSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Unlock. Defaults to XML based on the format input parameter.)
        """
        return self._output.get('Response', None)

class NameAndFeatureSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return NameAndFeatureSearchResultSet(response, path)
