Feature: Video

  Scenario: Add Party
    Given I am logged in as ccedev
    When I visit add_party
    And I submit valid party information
    Then I should see the new party

  Scenario: Edit Party
    Given I am logged in as ccedev
    And I have a party
    When I visit edit_party
    And I submit updated party information
    Then I should see the updated party

  Scenario: Delete Party
    Given I am logged in as ccedev
    And I have a party
    When I visit delete_party
    And I delete the party
    Then I shouldnt see the party

  Scenario:  Simple Search Party
    Given I am logged in as ccedev
    And I have a party
    When I visit browse_party
    And I use the party simple search
    Then I should see the party

    # Organization
  Scenario: Add Organization
    Given I am logged in as ccedev
    When I visit add_organization
    And I submit valid organization information
    Then I should see the new organization

  Scenario: Edit Organization
    Given I am logged in as ccedev
    And I have a organization
    When I visit edit_organization
    And I submit updated organization information
    Then I should see the updated organization

  Scenario: Delete Organization
    Given I am logged in as ccedev
    And I have a organization
    When I visit delete_organization
    And I delete the organization
    Then I shouldnt see the organization

  Scenario:  Simple Search Organization
    Given I am logged in as ccedev
    And I have a organization
    When I visit browse_organization
    And I use the organization simple search
    Then I should see the organization

    #OFFICE
    Scenario: Add Office
    Given I am logged in as ccedev
    When I visit add_office
    And I submit valid office information
    Then I should see the new office

  Scenario: Edit Office
    Given I am logged in as ccedev
    And I have a office
    When I visit edit_office
    And I submit updated office information
    Then I should see the updated office

  Scenario: Delete Office
    Given I am logged in as ccedev
    And I have a office
    When I visit delete_office
    And I delete the office
    Then I shouldnt see the office

  Scenario:  Simple Search Office
    Given I am logged in as ccedev
    And I have a office
    When I visit browse_office
    And I use the office simple search
    Then I should see the office