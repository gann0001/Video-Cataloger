Feature: Video
# tag
 Scenario: Add Tag
    Given I am logged in as ccedev
    When I visit add_tag
    And I submit valid tag information
    Then I should see the new tag

  Scenario: Edit Tag
    Given I am logged in as ccedev
    And I have a tag
    When I visit edit_tag
    And I submit updated tag information
    Then I should see the updated tag

  Scenario: Delete Tag
    Given I am logged in as ccedev
    And I have a tag
    When I visit delete_tag
    And I delete the tag
    Then I shouldnt see the tag

  Scenario:  Simple Search Tag
    Given I am logged in as ccedev
    And I have a tag
    When I visit browse_tag
    And I use the tag simple search
    Then I should see the tag

#ElectionYear
 Scenario: Add ElectionYear
    Given I am logged in as ccedev
    When I visit add_election_year
    And I submit valid year information
    Then I should see the new year

  Scenario: Edit ElectionYear
    Given I am logged in as ccedev
    And I have a year
    When I visit edit_election_year
    And I submit updated year information
    Then I should see the updated year

  Scenario: Delete ElectionYear
    Given I am logged in as ccedev
    And I have a year
    When I visit delete_election_year
    And I delete the year
    Then I shouldnt see the year

  Scenario:  Simple Search ElectionYear
    Given I am logged in as ccedev
    And I have a year
    When I visit browse_election_year
    And I use the year simple search
    Then I should see the year

#VideoFormat
 Scenario: Add VideoFormat
    Given I am logged in as ccedev
    When I visit add_video_format
    And I submit valid format information
    Then I should see the new format

  Scenario: Edit VideoFormat
    Given I am logged in as ccedev
    And I have a format
    When I visit edit_video_format
    And I submit updated format information
    Then I should see the updated format

  Scenario: Delete VideoFormat
    Given I am logged in as ccedev
    And I have a format
    When I visit delete_video_format
    And I delete the format
    Then I shouldnt see the format

  Scenario:  Simple Search VideoFormat
    Given I am logged in as ccedev
    And I have a format
    When I visit browse_video_format
    And I use the format simple search
    Then I should see the format