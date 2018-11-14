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
    stage('deploy alerter') {
    // some block
    sh '''ssh leo160886@35.205.178.85
          docker pull docker.io/leo160886/alert:latest
          docker stop my-application
          docker rm my-application
          docker rmi docker.io/leo160886/alert:latest:current
          docker tag docker.io/leo160886/alert:latest docker.example.com/my-application:current
          docker run -d --name my-application docker.io/leo160886/alert:latest
          '''
}
}
