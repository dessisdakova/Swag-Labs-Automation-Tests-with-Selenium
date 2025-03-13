class Credentials:

    def __init__(self, user):
        self.username = {
            "standard": "standard_user",
            "locked-out": "locked_out_user",
            "problem": "problem_user",
            "performance": "performance_glitch_user",
            "error": "error_user",
            "visual": "visual_user"
        }[user]
        self.password = "secret_sauce"
