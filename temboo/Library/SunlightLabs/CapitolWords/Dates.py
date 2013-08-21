# -*- coding: utf-8 -*-

###############################################################################
#
# Dates
# Returns the popularity of a given phrase in the Congressional Record over time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Dates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Dates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/CapitolWords/Dates')


    def new_input_set(self):
        return DatesInputSet()

    def _make_result_set(self, result, path):
        return DatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DatesChoreographyExecution(session, exec_id, path)

class DatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Dates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_BioguideID(self, value):
        """
        Set the value of the BioguideID input for this Choreo. ((optional, string) Limit results to the member of Congress with the given Bioguide ID. The Bioguide ID of any current or past congressional member can be found at bioguide.congress.gov.)
        """
        InputSet._set_input(self, 'BioguideID', value)
    def set_Chamber(self, value):
        """
        Set the value of the Chamber input for this Choreo. ((optional, string) Limit results to a particular chamber. Valid values: house, senate, extensions.)
        """
        InputSet._set_input(self, 'Chamber', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) Show results for only the given date. Format: YYYY-MM-DD)
        """
        InputSet._set_input(self, 'Date', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) Limit results to those on or before the given date. Format: YYYY-MM-DD.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Granularity(self, value):
        """
        Set the value of the Granularity input for this Choreo. ((optional, string) The length of time covered by each result. Valid values: year, month, day. Defaults to day.)
        """
        InputSet._set_input(self, 'Granularity', value)
    def set_MinCount(self, value):
        """
        Set the value of the MinCount input for this Choreo. ((optional, boolean) Only returns results where mentions are at or above the supplied threshold.)
        """
        InputSet._set_input(self, 'MinCount', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) Limit results to members of congress from a given party. Valid values: R, D, I.)
        """
        InputSet._set_input(self, 'Party', value)
    def set_Percentages(self, value):
        """
        Set the value of the Percentages input for this Choreo. ((optional, string) Include the percentage of mentions versus total words in the result objects. Valid values: true, false. Defaults to false.)
        """
        InputSet._set_input(self, 'Percentages', value)
    def set_Phrase(self, value):
        """
        Set the value of the Phrase input for this Choreo. ((required, string) The phrase to search for.)
        """
        InputSet._set_input(self, 'Phrase', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Output formats inlcude json and xml. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) Limit results to those on or after the given date. Format: YYYY-MM-DD)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Limit results to members from a particular state. Format: 2-letter state abbreviation (e.g. MD, RI, NY))
        """
        InputSet._set_input(self, 'State', value)

class DatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Dates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CapitolWords.)
        """
        return self._output.get('Response', None)

class DatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DatesResultSet(response, path)
