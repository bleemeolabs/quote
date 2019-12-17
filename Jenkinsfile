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
docker run --rm -v $(pwd):/srv/data registry.bleemeo.work/bleemeo/wheelsbuilder-18.04 pip3 wheel --wheel-dir=/srv/data/wheelhouse -r /srv/data/requirements.txt
rsync -azv wheelhouse/ wheelhouse.bleemeo.work:/srv/www/wheelhouse.bleemeo.work/htdocs/
            '''
        }
        stage ('Docker Image Build') {
            sh '''
docker pull ubuntu:18.04
docker build -t bleemeo/bleemeo-quote-uwsgi -f Dockerfile .
            '''
        }
      	stage ('Docker Image Publish') {
            sh '''
docker tag bleemeo/bleemeo-quote-uwsgi:latest registry.bleemeo.work/bleemeo/bleemeo-quote-uwsgi:latest
docker push registry.bleemeo.work/bleemeo/bleemeo-quote-uwsgi:latest
docker rmi registry.bleemeo.work/bleemeo/bleemeo-quote-uwsgi:latest
docker rmi bleemeo/bleemeo-quote-uwsgi:latest
            '''
      	}
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}

