# -*- coding: utf-8 -*-

###############################################################################
#
# ImageCampaign
# Transfer an image for updating the email body image or the wap banner of a campaign.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ImageCampaign(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ImageCampaign Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/ImageCampaign')


    def new_input_set(self):
        return ImageCampaignInputSet()

    def _make_result_set(self, result, path):
        return ImageCampaignResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ImageCampaignChoreographyExecution(session, exec_id, path)

class ImageCampaignInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ImageCampaign
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CampaignID(self, value):
        """
        Set the value of the CampaignID input for this Choreo. ((integer) The ID of the campaign you want to update)
        """
        InputSet._set_input(self, 'CampaignID', value)
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
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Specify the desired image type to modify (i.e. mailimage or wapban). Defaults to mailimage.)
        """
        InputSet._set_input(self, 'Type', value)
    def set_URLSource(self, value):
        """
        Set the value of the URLSource input for this Choreo. ((string) The URL where you are hosting the JPG file (i.e. http://mybucket.s3.amazonaws.com/my_image.jpg))
        """
        InputSet._set_input(self, 'URLSource', value)

class ImageCampaignResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ImageCampaign Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Obad)
        """
        return self._output.get('Response', None)

class ImageCampaignChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ImageCampaignResultSet(response, path)
