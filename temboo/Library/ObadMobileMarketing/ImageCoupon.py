# -*- coding: utf-8 -*-

###############################################################################
#
# ImageCoupon
# Transfer an image for updating the coupon or coupon burn.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ImageCoupon(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ImageCoupon Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/ImageCoupon')


    def new_input_set(self):
        return ImageCouponInputSet()

    def _make_result_set(self, result, path):
        return ImageCouponResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ImageCouponChoreographyExecution(session, exec_id, path)

class ImageCouponInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ImageCoupon
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
    def set_CouponID(self, value):
        """
        Set the value of the CouponID input for this Choreo. ((integer) The ID of the coupon you want to update)
        """
        InputSet._set_input(self, 'CouponID', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Specify the desired image type to update (i.e. coupon or couponburn). Defaults to coupon.)
        """
        InputSet._set_input(self, 'Type', value)
    def set_URLSource(self, value):
        """
        Set the value of the URLSource input for this Choreo. ((string) The URL where you are hosting the JPG file (i.e. http://mybucket.s3.amazonaws.com/my_image.jpg))
        """
        InputSet._set_input(self, 'URLSource', value)

class ImageCouponResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ImageCoupon Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The XML response from Obad)
        """
        return self._output.get('Response', None)

class ImageCouponChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ImageCouponResultSet(response, path)
