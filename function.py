from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox, QApplication, QMainWindow, \
    QRadioButton, QTableWidget, QTableWidgetItem, QWidget, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import sys
import sqlite3
import re
from PyQt5 import QtGui


class IntroDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodeWhiz")
        self.setFixedSize(900, 600)

        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setAlignment(Qt.AlignCenter)

        # Add background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("backimg.jpg")  # Load the background image
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(900, 600)

        # Add label for welcome message
        welcome_label = QLabel("Welcome to CodeWhiz")
        welcome_label.setStyleSheet("font-size: 24px; color: white;")
        layout.addWidget(welcome_label)

        # Add PLAY button
        play_button = QPushButton("PLAY")
        play_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white; 
                border: 2px solid white; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        play_button.clicked.connect(self.open_login_dialog)  # Connect button click to open login dialog
        layout.addWidget(play_button)

        self.setLayout(layout)

    def open_login_dialog(self):
        login_dialog = LoginDialog()
        login_dialog.exec_()


class MainMenuDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setFixedSize(900, 600)
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        self.setStyleSheet("background-color: transparent;")

        # Add background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("backimg.jpg")  # Load the image
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(900, 600)  # Set the size of the background image

        # Add buttons for each option
        mcq_button = QPushButton("Multiple Choice Quiz")
        self.stylize_button(mcq_button)
        mcq_button.clicked.connect(self.open_mcq_dialog)
        layout.addWidget(mcq_button)

        fillup_button = QPushButton("Fill Up")
        self.stylize_button(fillup_button)
        fillup_button.clicked.connect(self.open_fillup_dialog)
        layout.addWidget(fillup_button)


        scoreboard_button = QPushButton("Scoreboard")
        self.stylize_button(scoreboard_button)
        scoreboard_button.clicked.connect(self.open_scoreboard_dialog)
        layout.addWidget(scoreboard_button)

        about_dev_button = QPushButton("About Developers")
        self.stylize_button(about_dev_button)
        about_dev_button.clicked.connect(self.open_about_developers_dialog)
        layout.addWidget(about_dev_button)

        logout_button = QPushButton("Log Out")
        self.stylize_button(logout_button)
        logout_button.clicked.connect(self.logout)
        layout.addWidget(logout_button)

        self.setLayout(layout)

    def stylize_button(self, button):
        button.setStyleSheet(
            """
            QPushButton {
                color: white;
                font-size: 16px;
                background-color: transparent;
                border: 2px solid white; /* Neon green border color */
                border-radius: 10px;
                padding: 15px 30px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; /* Neon pink hover effect */
            }
            """
        )

    def open_mcq_dialog(self):
        mcq_dialog = MCQDialog()
        mcq_dialog.exec_()

    def open_fillup_dialog(self):
        fillup_dialog = FillBlanksDialog()
        fillup_dialog.exec_()


    def open_scoreboard_dialog(self):
        scoreboard_dialog = ScoreboardDialog()
        scoreboard_dialog.exec_()

    def open_about_developers_dialog(self):
        about_developers_dialog = AboutDevelopersDialog()
        about_developers_dialog.exec_()

    def logout(self):
        reply = QMessageBox.question(self, 'Logout', 'Are you sure you want to logout?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit()


class SignUpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up")
        self.setFixedSize(900, 600)
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignCenter)

        self.background_label = QLabel(self)
        pixmap = QPixmap("backimg.jpg")
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(900, 600)

        heading_label = QLabel("SIGN UP")
        heading_label.setStyleSheet("font-size: 24px; color: #FFFFFF; text-transform: uppercase;")
        layout.addWidget(heading_label)

        name_label = QLabel("Name")
        name_label.setStyleSheet("font-size: 16px; color: #FFFFFF;")
        layout.addWidget(name_label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        self.name_input.setStyleSheet("color: #FFFFFF; background-color: rgba(0, 0, 0, 0.5); border: 2px solid #FFFFFF; border-radius: 5px;")
        self.name_input.setFixedWidth(600)
        self.name_input.setFixedHeight(50)
        layout.addWidget(self.name_input)

        pid_label = QLabel("PID")
        pid_label.setStyleSheet("font-size: 16px; color: #FFFFFF;")
        layout.addWidget(pid_label)

        self.pid_input = QLineEdit()
        self.pid_input.setPlaceholderText("Enter your PID")
        self.pid_input.setStyleSheet("color: #FFFFFF; background-color: rgba(0, 0, 0, 0.5); border: 2px solid #FFFFFF; border-radius: 5px;")
        self.pid_input.setFixedWidth(600)
        self.pid_input.setFixedHeight(50)
        layout.addWidget(self.pid_input)

        email_label = QLabel("Email")
        email_label.setStyleSheet("font-size: 16px; color: #FFFFFF;")
        layout.addWidget(email_label)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setStyleSheet("color: #FFFFFF; background-color: rgba(0, 0, 0, 0.5); border: 2px solid #FFFFFF; border-radius: 5px;")
        self.email_input.setFixedWidth(600)
        self.email_input.setFixedHeight(50)
        layout.addWidget(self.email_input)

        password_label = QLabel("Password")
        password_label.setStyleSheet("font-size: 16px; color: #FFFFFF;")
        layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("color: #FFFFFF; background-color: rgba(0, 0, 0, 0.5); border: 2px solid #FFFFFF; border-radius: 5px;")
        self.password_input.setFixedWidth(600)
        self.password_input.setFixedHeight(50)
        layout.addWidget(self.password_input)

        confirm_password_label = QLabel("Confirm Password")
        confirm_password_label.setStyleSheet("font-size: 16px; color: #FFFFFF;")
        layout.addWidget(confirm_password_label)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm your password")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setStyleSheet("color: #FFFFFF; background-color: rgba(0, 0, 0, 0.5); border: 2px solid #FFFFFF; border-radius: 5px;")
        self.confirm_password_input.setFixedWidth(600)
        self.confirm_password_input.setFixedHeight(50)
        layout.addWidget(self.confirm_password_input)

        self.sign_up_button = QPushButton("Sign Up")
        self.sign_up_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: #FFFFFF; 
                border: 2px solid #FFFFFF; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        self.sign_up_button.clicked.connect(self.sign_up)
        layout.addWidget(self.sign_up_button)

        self.setLayout(layout)

    def go_to_login(self):
        self.close() # close the existing gui or SignUP
        login_dialog = LoginDialog()
        login_dialog.exec_()

    def sign_up(self):
        name = self.name_input.text()
        pid = self.pid_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        email_regex = r'^[a-zA-Z0-9._%+-]+@student\.sfit\.ac\.in$'
        if not re.match(email_regex, email):
            QMessageBox.warning(self, "Error", "Invalid email format! Email must end with @student.sfit.ac.in")
            return

        if len(password) < 8:
            QMessageBox.warning(self, "Error", "Password must be at least 8 characters long!")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match!")
            return

        try:
            connection = sqlite3.connect("LOGIN.db")
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM user_details WHERE PID=?", (pid,))
            existing_pid = cursor.fetchone()
            if existing_pid:
                QMessageBox.warning(self, "Error", "PID already exists! Please choose a different PID.")
                return

            cursor.execute("SELECT * FROM user_details WHERE email=?", (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                QMessageBox.warning(self, "Error", "User with this email already exists!")
                return

            cursor.execute("INSERT INTO user_details (name, PID, email, password) VALUES (?, ?, ?, ?)",
                           (name, pid, email, password))
            connection.commit()

            QMessageBox.information(self, "Success", "Sign up successful!")
            login_button = LoginDialog()
            login_button.exec_()

        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"Database error: {str(e)}")

        finally:
            if connection:
                connection.close()


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(900, 600)
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignCenter)

        heading_label = QLabel("LOGIN")
        heading_label.setStyleSheet("font-size: 24px; color: #FFFFFF; text-transform: uppercase;")
        layout.addWidget(heading_label)

        pid_label = QLabel("PID")
        pid_label.setStyleSheet("font-size: 16px; color: #FFFFFF;")
        layout.addWidget(pid_label)

        self.background_label = QLabel(self)
        pixmap = QPixmap("backimg.jpg")
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(900, 600)

        self.pid_input = QLineEdit()
        self.pid_input.setPlaceholderText("Enter your PID")
        self.pid_input.setStyleSheet("color: #000000; border: 2px solid #FFFFFF;")
        self.pid_input.setFixedWidth(600)
        self.pid_input.setFixedHeight(40)
        layout.addWidget(self.pid_input)

        password_label = QLabel("Password")
        password_label.setStyleSheet("font-size: 16px; color: #FFFFFF;")
        layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("color:#000000; border: 2px solid #FFFFFF;")
        self.password_input.setFixedWidth(600)
        self.password_input.setFixedHeight(40)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: #FFFFFF; 
                border: 2px solid #FFFFFF; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        pid = self.pid_input.text()
        password = self.password_input.text()

        connection = sqlite3.connect("LOGIN.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user_details WHERE PID=? AND password=?", (pid, password))
        user = cursor.fetchone()

        if user:
            self.accept()
            # Open the main menu dialog
            main_menu_dialog = MainMenuDialog()
            main_menu_dialog.exec_()
        else:
            QMessageBox.warning(self, "Error", "Invalid PID or password!")

        connection.close()

    def go_to_signup(self):
        signup_dialog = SignUpDialog()
        signup_dialog.exec_()


class FillBlanksDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fill in the Blanks")
        self.setFixedSize(900, 600)
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        # Add background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("backimg.jpg")  # Load the image
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(900, 600)

        self.setStyleSheet("font-size: 16px; color: white;")

        # Add heading label
        self.heading_label = QLabel("Fill in the Blanks")
        self.heading_label.setStyleSheet("font-size: 24px; color: white; text-transform: uppercase;")
        layout.addWidget(self.heading_label)

        self.question_label = QLabel()
        self.question_label.setStyleSheet("color: white;")
        layout.addWidget(self.question_label)

        self.answer_input = QLineEdit()
        self.answer_input.setStyleSheet("color: black;")
        layout.addWidget(self.answer_input)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white;
                border: 2px solid white;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7;
            }
            """
        )
        self.submit_button.clicked.connect(self.submit_answer)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        self.questions = []
        self.current_question = 0
        self.score = 0
        self.total_questions = 10  # Total questions to ask
        self.load_questions()

    def load_questions(self):
        try:
            connection = sqlite3.connect("questions.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM fillup_question ORDER BY RANDOM() LIMIT ?", (self.total_questions,))
            self.questions = cursor.fetchall()
            self.display_question()
        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"Database error: {str(e)}")
        finally:
            if connection:
                connection.close()

    def navigate_to_main_menu(self):
        main_menu_dialog = MainMenuDialog()  # Instantiate the main menu dialog
        main_menu_dialog.exec_()  # Show the main menu dialog

    def display_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.setText(question_data[0])
        self.correct_answer = question_data[1]

    def submit_answer(self):
        user_answer = self.answer_input.text()
        if user_answer.strip().lower() == self.correct_answer.strip().lower():
            self.score += 1

        if self.current_question < self.total_questions - 1:
            self.current_question += 1
            self.display_question()
            self.answer_input.clear()
        else:
            self.store_score_in_database()
            QMessageBox.information(self, "Info",
                                    f"Quiz completed! Your score: {self.score}/{self.total_questions}")
            self.navigate_to_main_menu()  # Navigate to the main menu after completing the quiz

    def store_score_in_database(self):
        try:
            connection = sqlite3.connect("LOGIN.db")
            cursor = connection.cursor()

            # Insert command to insert PID into scores table from users table
            cursor.execute("INSERT INTO scores (PID) SELECT PID FROM user_details")

            # Then, insert the score into the fillup_score column
            cursor.execute("""
                UPDATE scores 
                SET fillup_score = ? 
                WHERE PID IN (SELECT PID FROM user_details)""", (self.score,))

            # Displaying user details and scores joined
            cursor.execute("""
                SELECT user_details.*, scores.fillup_score 
                FROM user_details 
                JOIN scores ON user_details.PID = scores.PID""")

            # Fetching and printing joined data
            joined_data = cursor.fetchall()
            print(joined_data)

            connection.commit()
            QMessageBox.information(self, "Info", "Score stored in the database successfully.")
        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"Database error: {str(e)}")
        finally:
            if connection:
                connection.close()


class AboutDevelopersDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Developers")
        self.setFixedSize(900, 600)
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)

        # Add background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("backimg.jpg")  # Load the image
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(900, 600)  # Set the size of the background image

        self.setStyleSheet("font-size: 16px; color: white;")

        heading_label = QLabel("About Developers")
        heading_label.setStyleSheet("font-size: 24px; color: white; text-transform: uppercase;")
        layout.addWidget(heading_label)

        about_label = QLabel(
            """CodeWhiz is developed by JOMIN, GIRIDHAR, ARIC, ANURAG.
            We are a group of developers, dedicated to creating
            educational tools that make learning programming fun and easy!
            """
        )
        about_label.setStyleSheet("color: white;")
        layout.addWidget(about_label)

        github_button = QPushButton("Visit our GitHub")
        github_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white;
                border: 2px solid white;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7;
            }
            """
        )
        github_button.clicked.connect(self.open_github)
        layout.addWidget(github_button)

        self.setLayout(layout)

    def open_github(self):
        import webbrowser
        webbrowser.open('https://github.com/your-team-github')


class MCQDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple Choice Quiz")
        self.setFixedSize(900, 600)

        # Load background image
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 900, 600)
        self.background_label.setPixmap(QtGui.QPixmap("backimg.jpg"))

        layout = QVBoxLayout(self.background_label)
        layout.setContentsMargins(50, 50, 50, 50)

        # Add heading label
        self.heading_label = QLabel("Multiple Choice Quiz")
        self.heading_label.setStyleSheet("font-size: 24px; color: white; text-transform: uppercase;")
        layout.addWidget(self.heading_label)

        self.question_label = QLabel()
        self.question_label.setStyleSheet("font-size: 16px; color: white;")
        layout.addWidget(self.question_label)

        # Replace push buttons with radio buttons
        self.option1_radio = QRadioButton()
        self.option1_radio.setStyleSheet("color: white;font-size: 16px;")
        self.option1_radio.setObjectName("option_radio")
        layout.addWidget(self.option1_radio)

        self.option2_radio = QRadioButton()
        self.option2_radio.setStyleSheet("color: white;font-size: 16px;")
        self.option2_radio.setObjectName("option_radio")
        layout.addWidget(self.option2_radio)

        self.option3_radio = QRadioButton()
        self.option3_radio.setStyleSheet("color: white;font-size: 16px;")
        self.option3_radio.setObjectName("option_radio")
        layout.addWidget(self.option3_radio)

        self.option4_radio = QRadioButton()
        self.option4_radio.setStyleSheet("color: white;font-size: 16px;")
        self.option4_radio.setObjectName("option_radio")
        layout.addWidget(self.option4_radio)

        self.next_button = QPushButton("Next")
        self.next_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 16px;
                border: 3px solid white;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7;
            }
            """
        )
        self.next_button.clicked.connect(self.next_question)
        layout.addWidget(self.next_button)

        self.setLayout(layout)

        self.questions = []
        self.current_question = 0
        self.score = 0
        self.total_questions = 10  # Total questions to ask
        self.load_questions()

    def load_questions(self):
        try:
            connection = sqlite3.connect("questions.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM question_answer ORDER BY RANDOM() LIMIT ?", (self.total_questions,))
            self.questions = cursor.fetchall()
            self.display_question()
        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"Database error: {str(e)}")
        finally:
            if connection:
                connection.close()

    def navigate_to_main_menu(self):
        main_menu_dialog = MainMenuDialog()  # Instantiate the main menu dialog
        main_menu_dialog.exec_()  # Show the main menu dialog
    def display_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.setText(question_data[0])
        options = question_data[1:5]
        correct_answer = question_data[5]

        # Display options
        self.option1_radio.setText(options[0])
        self.option2_radio.setText(options[1])
        self.option3_radio.setText(options[2])
        self.option4_radio.setText(options[3])

        self.correct_answer = correct_answer

    def next_question(self):
        selected_option = None
        if self.option1_radio.isChecked():
            selected_option = self.option1_radio.text()
        elif self.option2_radio.isChecked():
            selected_option = self.option2_radio.text()
        elif self.option3_radio.isChecked():
            selected_option = self.option3_radio.text()
        elif self.option4_radio.isChecked():
            selected_option = self.option4_radio.text()

        if selected_option == self.correct_answer:
            self.score += 1

        if self.current_question < self.total_questions - 1:
            self.current_question += 1
            self.display_question()
        else:
            self.store_score_in_database()
            self.transfer_score_to_login_db()
            QMessageBox.information(self, "Info", f"Quiz completed! Your score: {self.score}/{self.total_questions}")

    def store_score_in_database(self):
        try:
            connection = sqlite3.connect("LOGIN.db")
            cursor = connection.cursor()

            # Insert command to insert PID into scores table from users table
            cursor.execute("INSERT INTO scores (PID) SELECT PID FROM user_details")

            # Then, insert the score into the score_mcq column
            cursor.execute("""
                UPDATE scores 
                SET mcq_score = ? 
                WHERE PID IN (SELECT PID FROM user_details)""", (self.score,))

            # Displaying user details and scores joined
            cursor.execute("""
                SELECT user_details.*, scores.mcq_score 
                FROM user_details 
                JOIN scores ON user_details.PID = scores.PID""")

            # Fetching and printing joined data
            joined_data = cursor.fetchall()
            print(joined_data)

            connection.commit()
            QMessageBox.information(self, "Info", "Score stored in the database successfully.")
        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"Database error: {str(e)}")
        finally:
            if connection:
                connection.close()
                self.navigate_to_main_menu()


class ScoreboardDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scoreboard")
        self.setFixedSize(900, 600)
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)

        # Add background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("backimg.jpg")  # Load the image
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(900, 600)  # Set the size of the background image

        self.setStyleSheet("font-size: 16px; color: black;")

        heading_label = QLabel("Scoreboard")
        heading_label.setStyleSheet("font-size: 24px; color: black; text-transform: uppercase;")
        layout.addWidget(heading_label)

        try:
            connection = sqlite3.connect("LOGIN.db")
            cursor = connection.cursor()
            cursor.execute("""
                SELECT user_details.name, 
                scores.fillup_score AS 'Fill in the Blanks',
                scores.mcq_score AS 'Multiple Choice Quiz',
                (scores.fillup_score + scores.mcq_score) AS 'Total Score'
                FROM user_details 
                JOIN scores ON user_details.PID = scores.PID
                ORDER BY (scores.fillup_score + scores.mcq_score) DESC
            """)
            scoreboard = cursor.fetchall()
            if scoreboard:
                table = QTableWidget()
                table.setRowCount(len(scoreboard))
                table.setColumnCount(len(scoreboard[0]))
                table.setHorizontalHeaderLabels(["Name", "Fill in the Blanks", "Multiple Choice Quiz", "Total Score"])
                for i, row in enumerate(scoreboard):
                    for j, cell in enumerate(row):
                        item = QTableWidgetItem(str(cell))
                        item.setTextAlignment(Qt.AlignCenter)
                        table.setItem(i, j, item)
                layout.addWidget(table)
            else:
                no_scores_label = QLabel("No scores yet!")
                no_scores_label.setStyleSheet("color: white;")
                layout.addWidget(no_scores_label)
        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"Database error: {str(e)}")
        finally:
            if connection:
                connection.close()

        self.setLayout(layout)


class MainMenuDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setFixedSize(900, 600)
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)

        # Add background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("backimg.jpg")  # Load the image
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(900, 600)  # Set the size of the background image

        self.setStyleSheet("font-size: 16px; color: white;")

        heading_label = QLabel("Main Menu")
        heading_label.setStyleSheet("font-size: 24px; color: white; text-transform: uppercase;")
        layout.addWidget(heading_label)

        self.play_fillblanks_button = QPushButton("Fill in the Blanks")
        self.play_fillblanks_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white; 
                border: 2px solid white; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        self.play_fillblanks_button.clicked.connect(self.play_fillblanks)
        layout.addWidget(self.play_fillblanks_button)

        self.play_mcq_button = QPushButton("Multiple Choice Quiz")
        self.play_mcq_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white; 
                border: 2px solid white; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        self.play_mcq_button.clicked.connect(self.play_mcq)
        layout.addWidget(self.play_mcq_button)

        self.scoreboard_button = QPushButton("Scoreboard")
        self.scoreboard_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white; 
                border: 2px solid white; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        self.scoreboard_button.clicked.connect(self.show_scoreboard)
        layout.addWidget(self.scoreboard_button)

        self.about_button = QPushButton("About Developers")
        self.about_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white; 
                border: 2px solid white; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        self.about_button.clicked.connect(self.show_about_developers)
        layout.addWidget(self.about_button)

        self.logout_button = QPushButton("Logout")
        self.logout_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white; 
                border: 2px solid white; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def play_fillblanks(self):
        fill_blanks_dialog = FillBlanksDialog()
        fill_blanks_dialog.exec_()

    def play_mcq(self):
        mcq_dialog = MCQDialog()
        mcq_dialog.exec_()

    def show_scoreboard(self):
        scoreboard_dialog = ScoreboardDialog()
        scoreboard_dialog.exec_()

    def show_about_developers(self):
        about_dialog = AboutDevelopersDialog()
        about_dialog.exec_()

    def logout(self):
        self.close()
        login_dialog = LoginDialog()
        login_dialog.exec_()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodeWhiz")
        self.setFixedSize(900, 600)

        # Add background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("backimg.jpg")  # Load the image
        self.background_label.setPixmap(pixmap)
        self.background_label.resize(900, 600)  # Set the size of the background image

        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        heading_label = QLabel("Welcome to CodeWhiz!")
        heading_label.setStyleSheet("font-size: 24px; color: white; text-transform: uppercase;")
        layout.addWidget(heading_label)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white; 
                border: 2px solid white; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        self.login_button.clicked.connect(self.open_login_dialog)
        layout.addWidget(self.login_button)

        self.sign_up_button = QPushButton("Sign Up")
        self.sign_up_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white; 
                border: 2px solid white; 
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6EC7; 
            }
            """
        )
        self.sign_up_button.clicked.connect(self.open_signup_dialog)
        layout.addWidget(self.sign_up_button)

        widget.setLayout(layout)

    def open_login_dialog(self):
        login_dialog = LoginDialog()
        login_dialog.exec_()

    def open_signup_dialog(self):
        signup_dialog = SignUpDialog()
        signup_dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
