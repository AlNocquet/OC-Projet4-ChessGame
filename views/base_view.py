class BaseView:
    def is_string_valid(self, value, string_len):
        if len(value) < string_len:
            return False

        else:
            return True