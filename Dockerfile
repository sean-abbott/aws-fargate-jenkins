FROM jenkins/jenkins:lts

USER root

ENV PLUGIN_LIST=""
ENV JENKINS_PARAMETER_PATH="/jenkins"
ENV SECRETS="${JENKINS_HOME}/secrets"
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false ${JAVA_OPTS}"


RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y \
        python3-pip

RUN pip3 install \
        awscli \
        boto3

COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
COPY scripts/populate_parameters.py /usr/local/bin/populate_parameters.py

USER jenkins

RUN /usr/local/bin/install-plugins.sh configuration-as-code


ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
