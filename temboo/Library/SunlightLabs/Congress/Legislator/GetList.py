# -*- coding: utf-8 -*-

###############################################################################
#
# GetList
# Returns a list of legislators that meet a specified search criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/Legislator/GetList')


    def new_input_set(self):
        return GetListInputSet()

    def _make_result_set(self, result, path):
        return GetListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListChoreographyExecution(session, exec_id, path)

class GetListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AllLegislators(self, value):
        """
        Set the value of the AllLegislators input for this Choreo. ((optional, boolean) A boolean flag indicating to search for all legislators even when they are no longer in office.)
        """
        InputSet._set_input(self, 'AllLegislators', value)
    def set_BioguideID(self, value):
        """
        Set the value of the BioguideID input for this Choreo. ((optional, string) The bioguide_id of the legislator to return.)
        """
        InputSet._set_input(self, 'BioguideID', value)
    def set_CRPID(self, value):
        """
        Set the value of the CRPID input for this Choreo. ((optional, string) The crp_id associated with a legislator to return.)
        """
        InputSet._set_input(self, 'CRPID', value)
    def set_District(self, value):
        """
        Set the value of the District input for this Choreo. ((optional, integer) Narrows the search result by district number.)
        """
        InputSet._set_input(self, 'District', value)
    def set_FECID(self, value):
        """
        Set the value of the FECID input for this Choreo. ((optional, string) The fec_id associated with the legislator to return.)
        """
        InputSet._set_input(self, 'FECID', value)
    def set_FacebookID(self, value):
        """
        Set the value of the FacebookID input for this Choreo. ((optional, string) The facebook id of a legislator to return.)
        """
        InputSet._set_input(self, 'FacebookID', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) The first name of a legislator to return.)
        """
        InputSet._set_input(self, 'FirstName', value)
    def set_Gender(self, value):
        """
        Set the value of the Gender input for this Choreo. ((optional, string) Narrows the search result by gender.)
        """
        InputSet._set_input(self, 'Gender', value)
    def set_GovTrackID(self, value):
        """
        Set the value of the GovTrackID input for this Choreo. ((optional, string) The govetrack_id associated with a legistlator to return.)
        """
        InputSet._set_input(self, 'GovTrackID', value)
    def set_InOffice(self, value):
        """
        Set the value of the InOffice input for this Choreo. ((optional, boolean) Whether or not the individual is in office currently. Valid values are true or false.)
        """
        InputSet._set_input(self, 'InOffice', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) The last name of the legislator to return.)
        """
        InputSet._set_input(self, 'LastName', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) Narrows the search result by party (i.e. "D" or "R").)
        """
        InputSet._set_input(self, 'Party', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) A state abbreviation to narrow the search results.)
        """
        InputSet._set_input(self, 'State', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The title associated with the individual to return.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_TwitterID(self, value):
        """
        Set the value of the TwitterID input for this Choreo. ((optional, string) The twitter id of the legislator to return (note, this can be a twitter screen name).)
        """
        InputSet._set_input(self, 'TwitterID', value)
    def set_VoteSmartID(self, value):
        """
        Set the value of the VoteSmartID input for this Choreo. ((optional, integer) The votesmart_id of a legislator to return.)
        """
        InputSet._set_input(self, 'VoteSmartID', value)

class GetListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListResultSet(response, path)
