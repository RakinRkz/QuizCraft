# QuizCraft
![Tools](https://skillicons.dev/icons?i=python,django,firebase)


Welcome to QuizCraft, a cutting-edge platform designed to revolutionize the way users engage with educational content. Inspired by the popular game-based learning platform Kahoot, QuizCraft takes interactive quizzes to the next level, offering a seamless blend of fun, competition, and effective learning tools. Whether you're a student looking to test your knowledge in a playful environment or a teacher seeking an engaging way to assess your students, QuizCraft has something for everyone.

## Features

- **Interactive Quizzes**: Dive into a variety of quizzes tailored to different subjects and skill levels. From general knowledge to specialized topics, there's always something new to learn and discover.
- **Customizable Quizzes**: Create your own quizzes or modify existing ones to fit your teaching style or learning preferences. Customize questions, categories, and even add images or videos to enhance understanding.
- **Real-Time Results**: See how you stack up against others in real-time leaderboards. Compete with friends, classmates, or challenge yourself to beat your previous scores.
- **User Accounts**: Sign up for a free account to save your progress, track your performance over time, and access personalized recommendations based on your interests and achievements.
- **Integration with Educational Platforms**: Seamlessly integrate QuizCraft with other educational platforms to extend the reach of your quizzes and assessments.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- Firebase Admin SDK

### Installation

1. Clone the repository:
   ```bash
   git clone https://your-repository-url.git
   cd QuizCraft
   ```

2. Set up a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure Firebase by following the instructions provided in the Firebase section of this README.

5. Apply migrations and create a superuser for the admin panel:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000` in your browser to get started.
