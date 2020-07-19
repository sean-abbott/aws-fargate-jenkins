# aws-fargate-jenkins
A jenkins docker instance intended for use on fargate. It uses CasC, has the option to install plugins, and will read secrets from the SSM parameter store and write them for use by jenkins

### Local testing
To test this locally, you can export the following environment variables:
```
JENKINS_PARAMETER_PATH=/dev/jenkins/server/secrets
SECRETS=/var/jenkins_home/secrets
CASC_JENKINS_CONFIG="https://raw.code.cargurus.com/your-github-profile/jenkins/master/casc.yaml"
```

Then you can run
```
docker run --rm -it -v $HOME/.aws:/var/jenkins_home/.aws -e AWS_PROFILE=default -e JENKINS_PARAMETER_PATH -e SECRETS -e CASC_JENKINS_CONFIG -p 8080:8080 jenkins
```

And jenkins should come up, using the jenkins configuration you specified. This is a good way to test your jenkins configs, as well.
