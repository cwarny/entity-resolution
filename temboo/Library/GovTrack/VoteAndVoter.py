# -*- coding: utf-8 -*-

###############################################################################
#
# VoteAndVoter
# Retrieves how people voted on roll call votes in the U.S. Congress since 1789. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class VoteAndVoter(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VoteAndVoter Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/VoteAndVoter')


    def new_input_set(self):
        return VoteAndVoterInputSet()

    def _make_result_set(self, result, path):
        return VoteAndVoterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VoteAndVoterChoreographyExecution(session, exec_id, path)

class VoteAndVoterInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VoteAndVoter
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Created(self, value):
        """
        Set the value of the Created input for this Choreo. ((optional, string) The date (and in recent history also the time) on which the vote was held (in YYYY-MM-DD format).)
        """
        InputSet._set_input(self, 'Created', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 20 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((optional, integer) Specify the ID of a vote object to retrieve just that object's record.)
        """
        InputSet._set_input(self, 'ObjectID', value)
    def set_Option(self, value):
        """
        Set the value of the Option input for this Choreo. ((optional, string) The way a particular person voted. The value corresponds to the key of an option returned on the Vote Choreo. See documentation for details.)
        """
        InputSet._set_input(self, 'Option', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) You can order the results by date using fieldname (ascending) or -fieldname (descending), where "fieldname" is either startdate or enddate.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_Person(self, value):
        """
        Set the value of the Person input for this Choreo. ((optional, integer) The person making this vote. This is an ID number.)
        """
        InputSet._set_input(self, 'Person', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify the format of the response. Default is JSON, but XML is also possible.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Vote(self, value):
        """
        Set the value of the Vote input for this Choreo. ((optional, string) The ID number of the vote that this was part of. This is in the form of an ID number.)
        """
        InputSet._set_input(self, 'Vote', value)

class VoteAndVoterResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VoteAndVoter Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The resopnse from GovTrack.)
        """
        return self._output.get('Response', None)

class VoteAndVoterChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VoteAndVoterResultSet(response, path)
