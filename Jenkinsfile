// Testing Jenkins automatic trigger

pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest --html=report.html --self-contained-html'
            }
        }
    }
}