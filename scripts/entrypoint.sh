#!/usr/bin/env bash
set -euo pipefail

if  [ ! -z "$PLUGIN_LIST" ]; then
    # shellcheck disable=SC2086
    /usr/local/bin/install-plugins.sh ${PLUGIN_LIST}
fi

python3 --version
python3 /usr/local/bin/populate_parameters.py

/sbin/tini -s -- /usr/local/bin/jenkins.sh
