node {
 	// Clean workspace before doing anything
    deleteDir()

    try {
        stage ('Clone') {
        	checkout scm
        }
        stage ('Build Wheels') {
        	sh '''
mkdir -p wheelhouse
docker run --rm -v $(pwd):/srv/data registry.bleemeo.work/bleemeo/wheelsbuilder-22.04 pip3 wheel --wheel-dir=/srv/data/wheelhouse -r /srv/data/requirements.txt
rsync -azv wheelhouse/ wheelhouse.bleemeo.work:/srv/www/wheelhouse.bleemeo.work/htdocs/
            '''
        }
        stage ('Docker Image Build') {
            sh '''
docker pull ubuntu:22.04
docker build -t bleemeolabs/quote -f Dockerfile .
            '''
        }
      	stage ('Docker Image Publish') {
            sh '''
docker tag  bleemeolabs/quote ghcr.io/bleemeolabs/quote
docker push ghcr.io/bleemeolabs/quote
docker rmi ghcr.io/bleemeolabs/quote
docker rmi bleemeolabs/quote
            '''
      	}
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}

