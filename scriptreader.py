"""
This module handles the text parsing and posting
"""
import random


class Tweet:
    """
    Tweet class
    """

    def __init__(self, script_files):
        """
        Entrypoint returns the tweet
        """
        self.script_files = script_files
        self.lines = []
        self.pull_scripts()

    def pull_scripts(self):
        """
        read the script files in
        """
        for scriptfile in self.script_files:
            with open(scriptfile, "r", encoding="utf8") as script:
                for line in script.readlines():
                    self.lines.append(line)

    def generate(self):
        """
        pick a line from the script ensuring it's less than 160 characters
        """
        script_line = random.choice(self.lines)
        if len(script_line > 160):
            self.generate()
        return script_line
