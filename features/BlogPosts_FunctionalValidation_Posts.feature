Feature: Operations related to Blog posts

  Scenario: Verifying the list of blogs when the Blog posts End point is triggered
    Given I want to retrieve list of posts when blog posts end point is triggered
    When I submit Get request with query parameters
    Then the response is success and validating the get posts response schema
    And validating the items field for the post

