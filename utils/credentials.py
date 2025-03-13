class Credentials:
    """
    A class to manage user credentials based on a given user.

    Attributes:
        username (str): The username for the specified user.
        password (str): The password, which is common across all users.
    """

    def __init__(self, user: str):
        self.username = {
            "standard": "standard_user",
            "locked-out": "locked_out_user",
            "problem": "problem_user",
            "performance": "performance_glitch_user",
            "error": "error_user",
            "visual": "visual_user"
        }[user]
        self.password = "secret_sauce"
