pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "tidal-plasma-465103-t8"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Jibin6713/Hotel_Reservation_MLOPS.git']])
                }
            }
        }


        stage('Setting up our virtual environment and installing dependancies'){
            steps{
                script{
                    echo 'Setting up our virtual environment and installing dependancies'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate

                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Building and Pushin Docker image to GCR'){
            steps{
                    withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                        script{
                            echo 'Building and Pushin Docker image to GCR...'
                            sh '''
                            export PATH=$PATH:${GCLOUD_PATH}

                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                            gcloud config set project ${GCP_PROJECT}

                            gcloud auth configure-docker --quiet

                            docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                            docker push gcr.io/${GCP_PROJECT}/ml-project:latest

                            '''
                        }
                    }
                }
            }

         stage('Deploy to Google Cloud Run'){
            steps{
                    withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                        script{
                            echo 'Deploy to Google Cloud Run...'
                            sh '''
                            export PATH=$PATH:${GCLOUD_PATH}

                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                            gcloud config set project ${GCP_PROJECT}

                            gcloud run deploy ml-project \
                                --image=gcr.io/${GCP_PROJECT}/ml-project:latest \
                                --platform=managed \
                                --region=us-central1 \
                                --allow-unauthenticated

                            '''
                        }
                    }
                }
            }





        }

    }
