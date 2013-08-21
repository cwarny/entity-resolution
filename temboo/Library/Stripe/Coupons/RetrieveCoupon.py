# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCoupon
# Retrieves a coupon with specified coupon id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeCoupon import StripeCoupon

import json

class RetrieveCoupon(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCoupon Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Coupons/RetrieveCoupon')


    def new_input_set(self):
        return RetrieveCouponInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCouponResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCouponChoreographyExecution(session, exec_id, path)

class RetrieveCouponInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCoupon
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CouponID(self, value):
        """
        Set the value of the CouponID input for this Choreo. ((required, string) The unique identifier of the coupon you want to retrieve)
        """
        InputSet._set_input(self, 'CouponID', value)

class RetrieveCouponResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCoupon Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getCoupon(self):
        """
        A coupon contains information about a percent-off discount you might want to apply to a customer. Coupons only apply to invoices created for recurring subscriptions and invoice items; they do not apply to one-off charges.
        """
        return StripeCoupon(self.getJSONFromString(self._output.get('Response', [])))

class RetrieveCouponChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveCouponResultSet(response, path)
