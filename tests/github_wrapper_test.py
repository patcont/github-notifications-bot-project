import unittest
import json
import github_wrapper

class TestStringMethods(unittest.TestCase):

    def test_getNotifications(self):
        f = open('tests/fixtures/sample_notifications.json')
        notifications = json.load(f)
        f.close()
        messages = list(map(github_wrapper.generateNotificationMessage, notifications))
        self.assertCountEqual(messages, [
            'Reason: comment - Faker is unsafe to use in automated tests - real urls and email addresses are generated  - Issue',
            'Reason: subscribed - Alpha 26: Zhuangzi - Release',
            'Reason: mention - Lookbook - PullRequest',
            "Reason: mention - Can't use system openssl lib/header in openSUSE 15.4 - Issue",
            'Reason: subscribed - Add curated list of Ruby on Rails courses - PullRequest'
        ])

if __name__ == '__main__':
    unittest.main()
