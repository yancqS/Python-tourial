import unittest
from get_format_name import get_format_name, AnonymousSurvey


# class NameTestCase(unittest.TestCase):
#     def test_first_last_name(self):
#         format_name = get_format_name('john', 'hans')
#         self.assertEqual(format_name, 'John Hans')
#
#     def test_store_single_response(self):
#         question = 'How old are you?'
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('20')
#         self.assertIn('20', my_survey.response)
#
#     def test_store_three_response(self):
#         question = 'what language did you first learn to sprak?'
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Spanish', 'Mandarin']
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response, my_survey.response)
#
#
# if __name__ == '__main__':
#     unittest.main()

##########################################################################

# setUp


class NameTestCase(unittest.TestCase):
    def setUp(self) -> None:
        question = 'what language did you first learn to sprak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_first_last_name(self):
        format_name = get_format_name('john', 'hans')
        self.assertEqual(format_name, 'John Hans')

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.response)

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.response)


if __name__ == '__main__':
    unittest.main()
