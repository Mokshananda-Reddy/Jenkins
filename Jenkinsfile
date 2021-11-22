pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Mokshananda-Reddy/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x length.py"
                sh "./length.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}