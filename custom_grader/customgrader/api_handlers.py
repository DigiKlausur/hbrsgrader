from .base import BaseApiHandler
from tornado import web
import sys
import glob
import json

class MultipleChoiceHandler(BaseApiHandler):

    def is_multiplechoice_cell(self, cell):
        if ("extended_type" not in cell["metadata"]):
            return False
        if (cell["metadata"]["extended_type"]["type"] != "multiplechoice"):
            return False
        return True

    def get_choices(self, cell):
        return cell["metadata"]["extended_type"]["choices"]


    def grade(self, solution, student_answer):
        grade = 0
        feedback = ""
        if (self.is_multiplechoice_cell(solution) and self.is_multiplechoice_cell(student_answer)):
            if (self.get_choices(solution) == self.get_choices(student_answer)):
                grade = 1
            else:
                feedback = "Student gave wrong answer."
        else:
            feedback = "Not a multiplechoice cell!"

        return grade, feedback

    @web.authenticated
    def post(self):
        request = self.get_json_body()
        solution = request['solution']['cells'][0]
        student_answer = request['task']['cells'][0]

        grade, feedback = self.grade(solution, student_answer)

        response = {
            "grade": grade,
            "feedback": feedback
        }

        self.write(json.dumps(response))

default_handlers = [
    (r'/grader/api/multiplechoice', MultipleChoiceHandler)
]