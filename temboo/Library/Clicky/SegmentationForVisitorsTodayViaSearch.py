# -*- coding: utf-8 -*-

###############################################################################
#
# SegmentationForVisitorsTodayViaSearch
# Retrieves segmentation data for visitors today who arrived via a search.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SegmentationForVisitorsTodayViaSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SegmentationForVisitorsTodayViaSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Clicky/SegmentationForVisitorsTodayViaSearch')


    def new_input_set(self):
        return SegmentationForVisitorsTodayViaSearchInputSet()

    def _make_result_set(self, result, path):
        return SegmentationForVisitorsTodayViaSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SegmentationForVisitorsTodayViaSearchChoreographyExecution(session, exec_id, path)

class SegmentationForVisitorsTodayViaSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SegmentationForVisitorsTodayViaSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of records you want to retrieve. Defaults to 30.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Output(self, value):
        """
        Set the value of the Output input for this Choreo. ((optional, string) What format you want the returned data to be in. Accepted values: xml, php, json, csv. Defaults to 'xml'.)
        """
        InputSet._set_input(self, 'Output', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((required, integer) Your request must include the site's ID that you want to access data from. Available from your site preferences page.)
        """
        InputSet._set_input(self, 'SiteID', value)
    def set_SiteKey(self, value):
        """
        Set the value of the SiteKey input for this Choreo. ((required, string) The unique key assigned to you when you first register with Clicky. Available from your site preferences page.)
        """
        InputSet._set_input(self, 'SiteKey', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of data you want to retrieve. Defaults to "segmentation".)
        """
        InputSet._set_input(self, 'Type', value)

class SegmentationForVisitorsTodayViaSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SegmentationForVisitorsTodayViaSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Clicky formatted as specified in the Output parameter. Default is XML.)
        """
        return self._output.get('Response', None)

class SegmentationForVisitorsTodayViaSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SegmentationForVisitorsTodayViaSearchResultSet(response, path)
