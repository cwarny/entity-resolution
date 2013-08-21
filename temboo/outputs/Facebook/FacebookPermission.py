# coding: utf-8

class FacebookPermission:
    """
     A permission (or scope) associated with the access token used in the request

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAdsManagement(self):
        """
        Provides the ability to manage ads and call the Facebook Ads API on behalf of a user
        """
        return self.base.get("ads_management", [])

    def getCreateEvent(self):
        """
        Enables your application to create and modify events on the user's behalf
        """
        return self.base.get("create_event", [])

    def getCreateNote(self):
        """
        Enables your application to create notes on the user's behalf
        """
        return self.base.get("create_note", [])

    def getEmail(self):
        """
        Provides access to the user's primary email address in the email property.
        """
        return self.base.get("email", [])

    def getFriendsAboutMe(self):
        """
        Provides access to the user's friend's about me info
        """
        return self.base.get("friends_about_me", [])

    def getFriendsActivities(self):
        """
        Provides access to the user's friend's activities
        """
        return self.base.get("friends_activities", [])

    def getFriendsBirthday(self):
        """
        Provides access to the user's friend's birthdays
        """
        return self.base.get("friends_birthday", [])

    def getFriendsEducationHistory(self):
        """
        Provides access to the user's friend's education history
        """
        return self.base.get("friends_education_history", [])

    def getFriendsEvents(self):
        """
        Provides access to the user's friend's events
        """
        return self.base.get("friends_events", [])

    def getFriendsGamesActivity(self):
        """
        Provides access to the user's friend's game activities
        """
        return self.base.get("friends_games_activity", [])

    def getFriendsGroups(self):
        """
        Provides access to the user's friend's groups
        """
        return self.base.get("friends_groups", [])

    def getFriendsHometown(self):
        """
        Provides access to the user's friend's hometown info
        """
        return self.base.get("friends_hometown", [])

    def getFriendsInterests(self):
        """
        Provides access to the user's friend's interests
        """
        return self.base.get("friends_interests", [])

    def getFriendsLikes(self):
        """
        Provides access to the user's friend's likes
        """
        return self.base.get("friends_likes", [])

    def getFriendsLocation(self):
        """
        Provides access to the user's friend's location info
        """
        return self.base.get("friends_location", [])

    def getFriendsNotes(self):
        """
        Provides access to the user's friend's notes
        """
        return self.base.get("friends_notes", [])

    def getFriendsOnlinePresence(self):
        """
        Provides access to the user's friend's online/offline presence
        """
        return self.base.get("friends_online_presence", [])

    def getFriendsPhotoVideoTags(self):
        """
        Provides access to the user's friend's video tags
        """
        return self.base.get("friends_photo_video_tags", [])

    def getFriendsPhotos(self):
        """
        Provides access to the user's friend's photos
        """
        return self.base.get("friends_photos", [])

    def getFriendsQuestions(self):
        """
        Provides access to the user's friend's questions
        """
        return self.base.get("friends_questions", [])

    def getFriendsRelationshipDetails(self):
        """
        Provides access to the user's friend's relationship details
        """
        return self.base.get("friends_relationship_details", [])

    def getFriendsRelationships(self):
        """
        Provides access to the user's friend's relationship
        """
        return self.base.get("friends_relationships", [])

    def getFriendsReligionPolitics(self):
        """
        Provides access to the user's friend's religion and politics affiliations
        """
        return self.base.get("friends_religion_politics", [])

    def getFriendsStatus(self):
        """
        Provides access to the user's friend's status
        """
        return self.base.get("friends_status", [])

    def getFriendsSubscriptions(self):
        """
        Provides access to the user's friend's subscriptions
        """
        return self.base.get("friends_subscriptions", [])

    def getFriendsVideos(self):
        """
        Provides access to the user's friend's videos
        """
        return self.base.get("friends_videos", [])

    def getFriendsWebsite(self):
        """
        Provides access to the user's friend's website
        """
        return self.base.get("friends_website", [])

    def getFriendsWorkHistory(self):
        """
        Provides access to the user's friend's work history
        """
        return self.base.get("friends_work_history", [])

    def getManageFriendlists(self):
        """
        Enables your app to create and edit the user's friend lists
        """
        return self.base.get("manage_friendlists", [])

    def getManageNotifications(self):
        """
        Enables your app to read notifications and mark them as read
        """
        return self.base.get("manage_notifications", [])

    def getManagePages(self):
        """
        Enables your application to retrieve access_tokens for Pages and Applications that the user administrates
        """
        return self.base.get("manage_pages", [])

    def getPhotoUpload(self):
        """
        Enables your application to upload photos for a user
        """
        return self.base.get("photo_upload", [])

    def getPublishActions(self):
        """
        Allows your app to publish to the Open Graph
        """
        return self.base.get("publish_actions", [])

    def getPublishCheckins(self):
        """
        Enables your app to perform checkins on behalf of the user
        """
        return self.base.get("publish_checkins", [])

    def getPublishStream(self):
        """
        Enables your app to post content, comments, and likes to a user's stream and to the streams of the user's friends
        """
        return self.base.get("publish_stream", [])

    def getReadFriendlists(self):
        """
        Provides access to any friend lists the user created
        """
        return self.base.get("read_friendlists", [])

    def getReadInsights(self):
        """
        Provides read access to the Insights data for pages, applications, and domains the user owns
        """
        return self.base.get("read_insights", [])

    def getReadMailbox(self):
        """
        Provides the ability to read from a user's Facebook Inbox
        """
        return self.base.get("read_mailbox", [])

    def getReadRequests(self):
        """
        Provides read access to the user's friend requests
        """
        return self.base.get("read_requests", [])

    def getReadStream(self):
        """
        Provides access to all the posts in the user's News Feed and enables your application to perform searches against the user's News Feed
        """
        return self.base.get("read_stream", [])

    def getRsvpEvent(self):
        """
        Enables your application to RSVP to events on the user's behalf
        """
        return self.base.get("rsvp_event", [])

    def getStatusUpdate(self):
        """
        Enables your application to update a user's status
        """
        return self.base.get("status_update", [])

    def getUserAboutMe(self):
        """
        Provides access to the "About Me" section of the profile in the about property
        """
        return self.base.get("user_about_me", [])

    def getUserActionsMusic(self):
        """
        Allows you to retrieve the actions published by all applications using the built-in music.listens action
        """
        return self.base.get("user_actions.music", [])

    def getUserActionsNews(self):
        """
        Allows you to retrieve the actions published by all applications using the built-in news.reads action
        """
        return self.base.get("user_actions.news", [])

    def getUserActionsVideo(self):
        """
        Allows you to retrieve the actions published by all applications using the built-in video.watches action
        """
        return self.base.get("user_actions.video", [])

    def getUserActivities(self):
        """
        Provides access to the user's list of activities as the activities connection
        """
        return self.base.get("user_activities", [])

    def getUserBirthday(self):
        """
        Provides access to the birthday with year as the birthday property
        """
        return self.base.get("user_birthday", [])

    def getUserCheckins(self):
        """
        Provides read access to the authorized user's check-ins or a friend's check-ins that the user can see
        """
        return self.base.get("user_checkins", [])

    def getUserEducationHistory(self):
        """
        Provides access to education history as the education property
        """
        return self.base.get("user_education_history", [])

    def getUserEvents(self):
        """
        Provides access to the list of events the user is attending as the events connection
        """
        return self.base.get("user_events", [])

    def getUserGamesActivity(self):
        """
        Allows you post and retrieve game achievement activity
        """
        return self.base.get("user_games_activity", [])

    def getUserGroups(self):
        """
        Provides access to the list of groups the user is a member of as the groups connection
        """
        return self.base.get("user_groups", [])

    def getUserHometown(self):
        """
        Provides access to the user's hometown in the hometown property
        """
        return self.base.get("user_hometown", [])

    def getUserInterests(self):
        """
        Provides access to the user's list of interests as the interests connection
        """
        return self.base.get("user_interests", [])

    def getUserLikes(self):
        """
        Provides access to the list of all of the pages the user has liked as the likes connection
        """
        return self.base.get("user_likes", [])

    def getUserLocation(self):
        """
        Provides access to the user's current city as the location property
        """
        return self.base.get("user_location", [])

    def getUserNotes(self):
        """
        Provides access to the user's notes as the notes connection
        """
        return self.base.get("user_notes", [])

    def getUserOnlinePresence(self):
        """
        Provides access to the user's online/offline presence
        """
        return self.base.get("user_online_presence", [])

    def getUserPhotoVideoTags(self):
        """
        Provides access to video tags
        """
        return self.base.get("user_photo_video_tags", [])

    def getUserPhotos(self):
        """
        Provides access to the photos the user has uploaded, and photos the user has been tagged in
        """
        return self.base.get("user_photos", [])

    def getUserQuestions(self):
        """
        Provides access to the questions the user or friend has asked
        """
        return self.base.get("user_questions", [])

    def getUserRelationshipDetails(self):
        """
        Provides access to the user's relationship preferences
        """
        return self.base.get("user_relationship_details", [])

    def getUserRelationships(self):
        """
        Provides access to the user's family and personal relationships and relationship status
        """
        return self.base.get("user_relationships", [])

    def getUserReligionPolitics(self):
        """
        Provides access to the user's religious and political affiliations
        """
        return self.base.get("user_religion_politics", [])

    def getUserStatus(self):
        """
        Provides access to the user's status messages and checkins
        """
        return self.base.get("user_status", [])

    def getUserSubscriptions(self):
        """
        Provides access to the user's subscribers and subscribees
        """
        return self.base.get("user_subscriptions", [])

    def getUserVideos(self):
        """
        Provides access to the videos the user has uploaded, and videos the user has been tagged in
        """
        return self.base.get("user_videos", [])

    def getUserWebsite(self):
        """
        Provides access to the user's web site URL
        """
        return self.base.get("user_website", [])

    def getUserWorkHistory(self):
        """
        Provides access to work history as the work property
        """
        return self.base.get("user_work_history", [])

    def getVideoUpload(self):
        """
        Provides access to upload videos
        """
        return self.base.get("video_upload", [])

    def getWhitelistedOfflineAccess(self):
        """
        """
        return self.base.get("whitelisted_offline_access", [])

    def getXmppLogin(self):
        """
        Provides applications that integrate with Facebook Chat the ability to log in users
        """
        return self.base.get("xmpp_login", [])

    def getBase(self):
        """
        Internal utility method; retrieve the base JSON object for this element of the response data.
        """
        return self.base

    def getJSONObject(self, json, key):
        """
        Internal utility method; retrieve a sub-object from a JSON object/array; returns an empty object if key is not present
        """
        toReturn = {}

        if json is not None:
            toReturn = json.get(key, {})

        return toReturn

