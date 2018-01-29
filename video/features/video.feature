Feature: Video

  Scenario: Add Video
    Given I am logged in as ccedev
    And I have a organization, party, office, tag, electionyear, videoformat and personrole
    When I visit add_video
    And I submit valid video information
    Then I should see the new video

  Scenario: Edit Video
    Given I am logged in as ccedev
    And I have a video
    When I visit edit_video
    And I submit updated video information
    Then I should see the updated video

  Scenario: Delete Video
    Given I am logged in as ccedev
    And I have a video
    When I visit delete_video
    And I delete the video
    Then I shouldnt see the video

  Scenario:  Simple Search Videos
    Given I am logged in as ccedev
    And I have a video
    When I visit browse_videos
    And I use the video simple search
    Then I should see the video

  Scenario: Advanced Search Videos
    Given I am logged in as ccedev
    And I have a video
    When I visit browse_videos
    And I use the video advanced search
    Then I should see the video

