# -*- coding: utf-8 -*-

###############################################################################
#
# CouponGroupData
# Allows you to add or remove a coupon from a coupon group.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CouponGroupData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CouponGroupData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/CouponGroupData')


    def new_input_set(self):
        return CouponGroupDataInputSet()

    def _make_result_set(self, result, path):
        return CouponGroupDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CouponGroupDataChoreographyExecution(session, exec_id, path)

class CouponGroupDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CouponGroupData
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
    def set_CouponGroupID(self, value):
        """
        Set the value of the CouponGroupID input for this Choreo. ((integer) The ID of the coupongroup you need to update)
        """
        InputSet._set_input(self, 'CouponGroupID', value)
    def set_CouponID(self, value):
        """
        Set the value of the CouponID input for this Choreo. ((integer) The ID of the coupon you need to update)
        """
        InputSet._set_input(self, 'CouponID', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_Mode(self, value):
        """
        Set the value of the Mode input for this Choreo. ((optional, boolean) Specify 0 for removing or 1 for adding. Defaults to 1.)
        """
        InputSet._set_input(self, 'Mode', value)


class CouponGroupDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CouponGroupData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Obad)
        """
        return self._output.get('Response', None)

class CouponGroupDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CouponGroupDataResultSet(response, path)
