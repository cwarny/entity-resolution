# -*- coding: utf-8 -*-

###############################################################################
#
# Person
# Returns members of Congress and U.S. Presidents since the founding of the nation.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Person(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Person Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/Person')


    def new_input_set(self):
        return PersonInputSet()

    def _make_result_set(self, result, path):
        return PersonResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PersonChoreographyExecution(session, exec_id, path)

class PersonInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Person
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) First name of the representative to find.)
        """
        InputSet._set_input(self, 'FirstName', value)
    def set_Gender(self, value):
        """
        Set the value of the Gender input for this Choreo. ((optional, string) The person's gender (male or female). For historical data, gender is sometimes not specified.)
        """
        InputSet._set_input(self, 'Gender', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) The representative's last name.)
        """
        InputSet._set_input(self, 'LastName', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 20 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_MetaVidID(self, value):
        """
        Set the value of the MetaVidID input for this Choreo. ((optional, string) The person's ID on metavid.org.)
        """
        InputSet._set_input(self, 'MetaVidID', value)
    def set_MiddleName(self, value):
        """
        Set the value of the MiddleName input for this Choreo. ((optional, string) The representative's middle name.)
        """
        InputSet._set_input(self, 'MiddleName', value)
    def set_NameMod(self, value):
        """
        Set the value of the NameMod input for this Choreo. ((optional, string) The suffix of the person's name, ususally one of Jr., Sr., I, II, etc.)
        """
        InputSet._set_input(self, 'NameMod', value)
    def set_OSID(self, value):
        """
        Set the value of the OSID input for this Choreo. ((optional, integer) The person's ID on opensecrets.org (The Center for Responsive Politics).)
        """
        InputSet._set_input(self, 'OSID', value)
    def set_PVSID(self, value):
        """
        Set the value of the PVSID input for this Choreo. ((optional, integer) The person's ID on vote-smart.org (Project Vote Smart).)
        """
        InputSet._set_input(self, 'PVSID', value)
    def set_PersonID(self, value):
        """
        Set the value of the PersonID input for this Choreo. ((optional, integer) Specify the ID number for a person to retrieve only that person.)
        """
        InputSet._set_input(self, 'PersonID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify the format of the response. Default is JSON, but XML is also possible.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Roles(self, value):
        """
        Set the value of the Roles input for this Choreo. ((optional, string) ID number of a term in Congress or as President that this person has been elected to.)
        """
        InputSet._set_input(self, 'Roles', value)
    def set_TwitterID(self, value):
        """
        Set the value of the TwitterID input for this Choreo. ((optional, string) Official Twitter handle of the representative.)
        """
        InputSet._set_input(self, 'TwitterID', value)
    def set_YoutubeID(self, value):
        """
        Set the value of the YoutubeID input for this Choreo. ((optional, string) The name of the person't official YouTube channel.)
        """
        InputSet._set_input(self, 'YoutubeID', value)

class PersonResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Person Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The resopnse from GovTrack.)
        """
        return self._output.get('Response', None)

class PersonChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PersonResultSet(response, path)
