Feature: User authentication

  Scenario: Logging into an account

    Given I empty my "auth.User" table
    And I create the following users:
      | id | username | email             | password |
      | 1  | Jason    | jason@example.com | password |

    When I log in as "Jason" using password "password"
    Then I get a response with the following dict:
      | username | email             |
      | Jason    | jason@example.com |

  Scenario: Logging out of an account

    Given I empty my "auth.User" table
    And I create the following users:
      | id | username | email             | password |
      | 1  | Jason    | jason@example.com | password |

    And I log in as "Jason"

    When I log out
    Then I get a response with the status code "204"

  Scenario: Signing up for an account

    Given I empty my "auth.User" table

    When I sign up using the following data:
      | username | email             | password |
      | Jason    | jason@example.com | password |
    Then I get a response with the following dict:
      | username | email             |
      | Jason    | jason@example.com |