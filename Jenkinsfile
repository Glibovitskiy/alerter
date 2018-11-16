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
                steps {
                    script {

                        def remote = [:]
                            remote.name = 'test'
                            remote.host = "${TESTHOST}"
                            remote.user = "${TESTUSER}"
                            // remote.password = "${TESTPASSWORD}"
                            remote.allowAnyHosts = true

                            stage('docker') {
                                 sshCommand remote: remote, command: "docker rm -f alert"
                                 sshCommand remote: remote, command: "docker pull docker.io/leo160886/alert"
                                 sshCommand remote: remote, command: "docker run -d -e TOKEN --name=alert docker.io/leo160886/alert"
                            }
}
}                    
}
