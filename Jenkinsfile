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
    def remote = [:]
        remote.name = 'leo160886'
        remote.host = '35.205.178.85'
        remote.user = 'leo160886'
        remote.password = 'Bogdan2007'
        remote.allowAnyHosts = true
        stage('Remote SSH') {
          touch "123"
        }
}
