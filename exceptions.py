class LowLimitOfLengthsMessage(Exception):
    def __init__(
        self,
        message=("The splitting limit is too small; "
                "try increasing the limit or reformat the message."),
    ):
        self.message = message
        super().__init__(self.message)
