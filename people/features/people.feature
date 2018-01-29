Feature: People

 Scenario: Add PersonRole
    Given I am logged in as ccedev
    When I visit add_person_role
    And I submit valid role information
    Then I should see the new role

  Scenario: Edit PersonRole
    Given I am logged in as ccedev
    And I have a role
    When I visit edit_person_role
    And I submit updated role information
    Then I should see the updated role

  Scenario: Delete PersonRole
    Given I am logged in as ccedev
    And I have a role
    When I visit delete_person_role
    And I delete the role
    Then I shouldnt see the role

  Scenario:  Simple Search PersonRole
    Given I am logged in as ccedev
    And I have a role
    When I visit browse_person_role
    And I use the role simple search
    Then I should see the role



