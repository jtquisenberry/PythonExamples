# https://www.youtube.com/watch?v=TQgB9JFbui0&list=PLmkjlbmaJWHN6RBSk_5uW8VqozeyevVGV&index=3

# SOLID
# Single responsible. Each class and each function is responsible for one thing.
#    A function may invoke other functions, but it is not responsible for their
#    implementation.
# open to extension, closed to modification
# Liskov substitution
# interface segregation
# dependency inversion


# Single responsibility
# This function does three things, but it does not have to know
# how the other functions work.
# * Redability
# * Reusability
# * Testability
def send_email_report(email, time_period):
    report = prepare_report(time_period)
    body = format_report(report)
    send_email(email, body)


''''''''''''''''''''''''''''''''''''
# Open / Closed Principle
# Open for extension, but closed for modification.

# BAD
# The only way to extend the function is to modify code.
def send_html_email_report(email, time_period):
    report = prepare_report(time_period)
    body = format_html_report(report)
    send_email(email, body)

def send_pdf_email_report(email, time_period):
    report = prepare_report(time_period)
    body = format_pdf_report(report)
    send_email(email, body)

# Better, but requires multiple classes just to change one function.
# No longer single responsibility.
# Subclassing
class EmailReporter:

    def send_email_report(self, email, time_period):
        report = self.prepare_report(time_period)
        body = self.format_report(report)
        self.send_email(email, body)

    def prepare_report(self, time_period):
        pass

    def format_report(self, report):
        pass

    def send_email(selfself, email, body):
        pass

class EmailReporter2(EmailReporter):
    def format_report(selfself, report):
        pass
        #The new implementation.

''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Dependency Inversion
# clean interface
# input arguments separated from dependencies.
# Relies on initializer
# (Talk about dependencies with dependencies.)

class EmailReporter:

    # report_preparator, report_formatter, and email_sender are instances
    # of other classes.
    def __init__(self, report_preparator, report_formatter, email_sender):
        self._report_preparator = report_preparator
        self._report_formatter = report_formatter
        self._email_sender = email_sender

    def report(self, email, time_period):
        report = self._report_preparator.prepare(time_period)
        body = self._report_formatter.format(report)
        self._email_sender.send(email, body)

# How to call the class (wiring dependencies)
#    Commend dependencies
report_preparator = ReportPreparator()
email_sender = EmailSender()

#    One of the following, depending on what type of formatter is needed
#    Depend on abstractions, not concretions. Here report_formatter is abstract becasue
#    EmailReporter does not know what type of formatter it will receive.
email_reporter_html = EmailReporter(report_preparator = report_preparator,
                                    report_formatter = HTMLReportFormatter(), email_sender = email_sender)
email_reporter_pdf = EmailReporter(report_preparator = report_preparator,
                                    report_formatter = PDFReportFormatter(), email_sender = email_sender)

#    One of the following, depending on the previous choice.
email_reporter_html.report(email, time_period)
email_reporter_pdf.report(email, time_period)
''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Separation of concerns
# Wire dependencies at the highest level, nearest the main entry point of the application.
# implementation separated from coupling.
# Do it in main function.















'''
if __name__  == '__main__':
    print(__name__)
'''