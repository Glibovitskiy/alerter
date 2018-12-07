node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("leo160886/alert")
    }
    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
    stage('Remote ssh') {
                    script {

                      def remote = [:]
                          remote.name = "instance-1"
                          remote.host = "35.205.178.85"
                          remote.allowAnyHosts = true

                          node {
                            withCredentials([sshUserPrivateKey(credentialsId: '7820d7cf-1d1d-4814-bfd5-cf19576cddb1', keyFileVariable: 'identity', passphraseVariable: '', usernameVariable: 'userName')]) {
                              remote.user = userName
                              remote.identityFile = identity
                            stage('docker') {
                                 // sshCommand remote: remote, command: "docker rm -f \$(docker ps -aq)"
                                 // sshCommand remote: remote, command: "docker pull docker.io/leo160886/alert:latest"
                                 // sshCommand remote: remote, command: "docker run -d -e TOKEN --name=alert docker.io/leo160886/alert"
                                 // sshCommand remote: remote, command: "docker logs -f alert &> docker.log &"
                                 sshCommand remote: remote, command: "docker pull docker.io/leo160886/alert:latest"
                                 sshCommand remote: remote, command: "docker stop my-application"
                                 sshCommand remote: remote, command: "docker rm my-application"
                                 sshCommand remote: remote, command: "docker rmi docker.io/leo160886/alert:current"
                                 sshCommand remote: remote, command: "docker tag docker.io/leo160886/alert:latest docker.io/leo160886/alert:current"
                                 sshCommand remote: remote, command: "docker run -d -e TOKEN --name alert docker.io/leo160886/alert:latest"
                            }
                          }
                        }
                    }
    }
}
