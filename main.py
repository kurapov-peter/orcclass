from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from solver import Solver
import sys
import translator
import gui.mainwindow

tr = translator.Translator()
solver = Solver(size=6)


class Questionary(QMainWindow, gui.mainwindow.Ui_MainWindow):
    current_processing_vector = []
    number_of_questions = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_processing_vector = solver.get_best_informative_vector()
        self.alternative.addItems(tr.translate(self.current_processing_vector.coordinates))
        self.goodClass.clicked.connect(self.good_class_button_clicked)
        self.badClass.clicked.connect(self.bad_class_button_clicked)
        self.progressBar.setValue(0)
        self.gridStackedWidget.setCurrentIndex(0)

    def update_app(self):
        self.update_alternative()
        self.update_progress()

    def update_alternative(self):
        if self.current_processing_vector is not None:
            self.alternative.clear()
            self.alternative.addItems(tr.translate(self.current_processing_vector.coordinates))

    def update_progress(self):
        self.progressBar.setValue(100 * solver.get_progress())
        self.number_of_questions += 1

    def good_class_button_clicked(self):
        if not solver.is_finished():
            solver.process_user_input(self.current_processing_vector.coordinates, Solver.GOOD_CLASS)
            self.current_processing_vector = solver.get_best_informative_vector()
            self.update_app()
            print(solver)
        if solver.is_finished():
            self.show_completed_form()

    def bad_class_button_clicked(self):
        if not solver.is_finished():
            solver.process_user_input(self.current_processing_vector.coordinates, Solver.BAD_CLASS)
            self.current_processing_vector = solver.get_best_informative_vector()
            self.update_app()
            print(solver)
        if solver.is_finished():
            self.show_completed_form()

    def show_completed_form(self):
        self.gridStackedWidget.setCurrentIndex(1)
        self.number_of_questions_2.setText(str(self.number_of_questions))
        upper, lower = solver.border()
        self.ineffective_text_2.setReadOnly(True)
        self.effective_text_2.setReadOnly(True)
        for vector in upper:
            for rule in tr.translate(vector.coordinates):
                self.ineffective_text_2.appendPlainText(rule + "\n")
        for vector in lower:
            for rule in tr.translate(vector.coordinates):
                self.effective_text_2.appendPlainText(rule + "\n")

        # self.ineffective_text_2.insertPlainText(tr.translate([x.coordinates for x in upper]))
        # self.effective_text_2.insertPlainText(tr.translate([x.coordinates for x in lower]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Questionary()
    form.show()

    sys.exit(app.exec_())

