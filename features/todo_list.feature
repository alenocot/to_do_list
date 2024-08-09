Feature: To-Do List Management

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with description "Buy milk" due on "2024-08-10" and priority "High"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task           |
      | Buy groceries  |
      | Pay bills      |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task           | Status    |
      | Buy groceries  | Pending   |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task           |
      | Buy groceries  |
      | Pay bills      |
    When the user clears the to-do list
    Then the to-do list should be empty

    Feature: To-Do List Management

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with description "Buy milk" due on "2024-08-10" and priority "High"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task           |
      | Buy groceries  |
      | Pay bills      |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task           | Status    |
      | Buy groceries  | Pending   |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task           |
      | Buy groceries  |
      | Pay bills      |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Add a duplicate task
    Given the to-do list contains tasks:
      | Task           |
      | Buy groceries  |
    When the user adds a task "Buy groceries" with description "Buy milk again" due on "2024-08-11" and priority "Medium"
    Then the to-do list should contain 2 tasks with the title "Buy groceries"

  Scenario: List completed tasks only
    Given the to-do list contains tasks:
      | Task           | Status    |
      | Buy groceries  | Completed |
      | Pay bills      | Pending   |
    When the user lists only completed tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      """
    And the output should not contain:
      """
      - Pay bills
      """
