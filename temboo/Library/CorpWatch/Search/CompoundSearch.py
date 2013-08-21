# -*- coding: utf-8 -*-

###############################################################################
#
# CompoundSearch
# Returns a list of companies according to several search parameters such as industry, location, date range, company name, etc.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CompoundSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompoundSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Search/CompoundSearch')


    def new_input_set(self):
        return CompoundSearchInputSet()

    def _make_result_set(self, result, path):
        return CompoundSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompoundSearchChoreographyExecution(session, exec_id, path)

class CompoundSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompoundSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((conditional, string) Specific fragment of an address to be searched, such as "empire" or "Main Street.")
        """
        InputSet._set_input(self, 'Address', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((optional, string) Two-letter country code (e.g. VI for Virgin Islands).)
        """
        InputSet._set_input(self, 'CountryCode', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        InputSet._set_input(self, 'Index', value)
    def set_IndustryCode(self, value):
        """
        Set the value of the IndustryCode input for this Choreo. ((conditional, integer) Standard Industrial Classification (SIC) code.)
        """
        InputSet._set_input(self, 'IndustryCode', value)
    def set_IndustrySector(self, value):
        """
        Set the value of the IndustrySector input for this Choreo. ((conditional, integer) Standard Industrial Classification (SIC) sector code.)
        """
        InputSet._set_input(self, 'IndustrySector', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Match(self, value):
        """
        Set the value of the Match input for this Choreo. ((optional, integer) By default search terms match against complete words. Use 1 to return cases where the search string matches anywhere in the Name or Address field. Performance is significantly affected when enabled.)
        """
        InputSet._set_input(self, 'Match', value)
    def set_MaxYear(self, value):
        """
        Set the value of the MaxYear input for this Choreo. ((optional, integer) Indicate desired year of the most recent appearance in SEC filing data (e.g. indicating 2007 will search for companies that ceased filing in 2007).)
        """
        InputSet._set_input(self, 'MaxYear', value)
    def set_MinYear(self, value):
        """
        Set the value of the MinYear input for this Choreo. ((optional, integer) Indicate desired year of the most recent appearance in SEC filing data (e.g. indicating 2007 will search for companies that ceased filing in 2007).)
        """
        InputSet._set_input(self, 'MinYear', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((conditional, string) Company name to search. Words in the search query must match to full words in the name. See documentation for more details.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_NumChildren(self, value):
        """
        Set the value of the NumChildren input for this Choreo. ((optional, integer) Limit results to those with a specified number of listed subsidiaries, or "children." (Only immediate relationships are counted.)
        """
        InputSet._set_input(self, 'NumChildren', value)
    def set_NumParents(self, value):
        """
        Set the value of the NumParents input for this Choreo. ((optional, integer) Limit results to those with a specified number of listed parent companies (only immediate relationships are counted).)
        """
        InputSet._set_input(self, 'NumParents', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_SourceType(self, value):
        """
        Set the value of the SourceType input for this Choreo. ((optional, string) Indicate "filers" to restrict results to those of companies that appeared as a filer on SEC documents, or "relationships" for companies that only appear as subsidiaries on filings.)
        """
        InputSet._set_input(self, 'SourceType', value)
    def set_SubdivisionCode(self, value):
        """
        Set the value of the SubdivisionCode input for this Choreo. ((optional, string) Two-letter abbreviation for the subdivision of the area to be searched (e.g. "OR" for Oregon when CountryCode is set to "US").)
        """
        InputSet._set_input(self, 'SubdivisionCode', value)
    def set_TopParent(self, value):
        """
        Set the value of the TopParent input for this Choreo. ((optional, integer) Limit results by he CWID of the highest-level owning parent of a family of corprorations (or Top Parent). Most company records contain a field for top_parent_id.)
        """
        InputSet._set_input(self, 'TopParent', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((optional, integer) If a year is specified, only records for that year will be returned and the data in the company objects returned will be set appropriately for the request year. Defaults to most recent.)
        """
        InputSet._set_input(self, 'Year', value)

class CompoundSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompoundSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class CompoundSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompoundSearchResultSet(response, path)
