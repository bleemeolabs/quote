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
docker run --rm -v $(pwd):/srv/data bleemeo/wheelsbuilder-18.04 pip3 wheel --wheel-dir=/srv/data/wheelhouse -r /srv/data/requirements.txt
rsync -av ./wheelhouse/* /srv/www/wheelhouse.bleemeo.work/htdocs/
            '''
        }
        stage ('Docker Image Build') {
            sh '''
docker pull ubuntu:18.04
docker build -t bleemeo/quote.bleemeo.com-uwsgi -f Dockerfile .
            '''
        }
      	stage ('Docker Image Publish') {
            sh '''
docker tag bleemeo/quote.bleemeo.com-uwsgi:latest registry.bleemeo.work/bleemeo/quote.bleemeo.com-uwsgi:latest
docker push registry.bleemeo.work/bleemeo/quote.bleemeo.com-uwsgi:latest
            '''
      	}
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}

