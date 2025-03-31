"""
S part of the SOLID Principle means it promotes the idea that each class should have one job or responsibility, and that job should be encapsulated within that class.
"""


class Report:

    def __init__(self, content: str):
        self.report = content

    def generate(self):
        print(f"report generated {self.report}")


# this separates the problem to save the data.
class ReportSaver:

    def __init__(self, report: Report):
        self.report = report
    
    def save_to_file(self, filename: str):
        with open(filename, "w") as file:
            file.write(self.report.report)

if __name__ == "__main__":

    report = Report("This is the content")

    report.generate()

    rs = ReportSaver(report)
    rs.save_to_file("test")