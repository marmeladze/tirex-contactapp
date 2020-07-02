class FindUserStory:

    def __init__(self, phone_book):
        self.phone_book = phone_book

    def run(self, keyword):
        validated = self.validate_input(keyword)
        if validated:
            results = self.phone_book.find_by(keyword)
        else:
            results = self.validation_error_message(validated)
        return results

    def validate_input(self, keyword):
        return False if "%" in keyword else True

    def validation_error_message(validated):
        return {"message": "Keyword can not contain %"}


