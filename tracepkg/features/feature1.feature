Feature: Minimum viable bdd
  A set of files illustrating the plumbing of a bdd project.

  Scenario: Verify all bdd project components
    Given I'm a project admin
    When I read the project's package directory
    Then I should see a features directory
    And I should see a test directory
    And I should see a test/bdd directory