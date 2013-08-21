# -*- coding: utf-8 -*-

###############################################################################
#
# GetListingsPercentiles
# Retrieves percentiles of real estate listings from New York Times Web Service.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetListingsPercentiles(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetListingsPercentiles Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/RealEstate/GetListingsPercentiles')


    def new_input_set(self):
        return GetListingsPercentilesInputSet()

    def _make_result_set(self, result, path):
        return GetListingsPercentilesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListingsPercentilesChoreographyExecution(session, exec_id, path)

class GetListingsPercentilesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetListingsPercentiles
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Bedrooms(self, value):
        """
        Set the value of the Bedrooms input for this Choreo. ((optional, integer) Limits the results by number of bedrooms to search for. Defaults to 1.)
        """
        InputSet._set_input(self, 'Bedrooms', value)
    def set_DateRange(self, value):
        """
        Set the value of the DateRange input for this Choreo. ((required, string) Sets the quarter, month, week or day for the results (i.e. 2008-Q1, 2008-W52, 2007-07, 2010-10-01, etc).)
        """
        InputSet._set_input(self, 'DateRange', value)
    def set_GeoExtentLevel(self, value):
        """
        Set the value of the GeoExtentLevel input for this Choreo. ((required, string) The geographical unit for the results (i.e. borough, neighborhood, or zip).)
        """
        InputSet._set_input(self, 'GeoExtentLevel', value)
    def set_GeoExtentValue(self, value):
        """
        Set the value of the GeoExtentValue input for this Choreo. ((required, string) Limits the search to a specific area.  For example, if GeoExtentLevel is borough, the value for GeoExtentValue could be Brooklyn.)
        """
        InputSet._set_input(self, 'GeoExtentValue', value)
    def set_GeoSummaryLevel(self, value):
        """
        Set the value of the GeoSummaryLevel input for this Choreo. ((required, string) The geographic unit for grouping the results (borough, neighborhood, or zip).)
        """
        InputSet._set_input(self, 'GeoSummaryLevel', value)
    def set_Percentile(self, value):
        """
        Set the value of the Percentile input for this Choreo. ((required, integer) Specify a percentile for the listing prices you want to retrieve (i.e 50).)
        """
        InputSet._set_input(self, 'Percentile', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetListingsPercentilesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetListingsPercentiles Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class GetListingsPercentilesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListingsPercentilesResultSet(response, path)
