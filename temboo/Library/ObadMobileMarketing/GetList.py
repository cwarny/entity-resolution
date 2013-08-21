# -*- coding: utf-8 -*-

###############################################################################
#
# GetList
# Returns the list and parameters of a specified list type (i.e. campaigns, coupons, user groups, shop groups, or coupons groups).
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
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/GetList')


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
        Set the value of the APIKey input for this Choreo. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((integer) Private Key for 1 unique customer to connect with - provided by Obad Mobile Marketing)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((optional, integer) Unique ID for an item.  Defaults to 0 which returns ALL.)
        """
        InputSet._set_input(self, 'ID', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Specify the desired item list (i.e. camp, coupon, usergroup, shopgroup, or coupongroup). Defaults to coupon.)
        """
        InputSet._set_input(self, 'Type', value)

class GetListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Obad)
        """
        return self._output.get('Response', None)

class GetListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListResultSet(response, path)
