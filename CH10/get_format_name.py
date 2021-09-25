def get_format_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()


class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.response = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.response.append(new_response)

    def show_result(self):
        print("Survey result:")
        for response in self.response:
            print(f"- {response}")
