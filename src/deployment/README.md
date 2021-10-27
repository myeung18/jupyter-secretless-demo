[knowledge sharing]
https://jupyter.readthedocs.io/en/latest/projects/architecture/content-architecture.html

https://console-openshift-console.apps.odh-cl1.apps.os-climate.org/k8s/ns/odh-jupyterhub/pods

1. Spin up a dev quicklab cluster
https://github.com/operate-first/apps/blob/master/docs/ocp_dev_environments/setup_quicklab.md

2. Set up your pvcs by following this doc: 
https://github.com/operate-first/apps/tree/master/scripts/setup_pvs (use the runbook + env file in that folder, update the env file with your quicklab  host)
    - steps to setup PV/PVC

3. Got operator hub, find Opendatahub, install it

4. create a new project for jupyterhub, deploy this kfdef: 
    https://github.com/operate-first/apps/blob/master/kfdefs/overlays/osc/osc-cl1/jupyterhub/kfdef.yaml
    oc apply -f kfdefs/overlays/osc/osc-cl1/jupyterhub/kfdef.yaml

    [jupyterhub]
    quay.io/odh-jupyterhub/jupyterhub-img:v0.3.0'

    [jupyterHub in OpenShift deployment]
    #fix nodeaffinity
    oc label node ip-10-0-152-85.us-east-2.compute.internal node-role.kubernetes.io/odh-notebook=anytext
    #Service account info
    https://www.cyberark.com/resources/threat-research-blog/securing-kubernetes-clusters-by-eliminating-risky-permissions
    https://www.cyberark.com/resources/threat-research-blog/securing-identity-and-access-management-solutions
    -IDP
    https://computingforgeeks.com/restrict-kubernetes-service-account-users-to-a-namespace-with-rbac/

    #POC setup
    oc create sa data-team3 -n jupyterhub -o yaml --dry-run

    c.KubeSpawner.extra_containers = [{
      "name": "secretless-broker",
      "image": "quay.io/myeung/secretless-broker:local",
      "imagePullPolicy":"Always"
    }];
    c.KubeSpawner.extra_containers = [{
                "name": "secretless-broker",
                "image": "quay.io/myeung/secretless-broker:local",
                "args": ["-f", "/etc/secretless/secretless.yaml", "-debug"]
            }]    
    c.KubeSpawner.volumes = [{
                          "name": "config",
                          "configMap": {
                            "name": "secretless-config"}
                          }]

Note: we put all osc manifests here: https://github.com/operate-first/apps
    - https://github.com/OSC/bc_osc_jupyter

[kubeflow on OpenShift]
    https://www.kubeflow.org/docs/distributions/openshift/install-kubeflow/
    kubeflow + istio-system 

[Knowledge sharing - odh (Vaclav)]

Václav (Vašek) Pavlín11:10 AM
https://jupyterhub-kubespawner.readthedocs.io/en/latest/spawner.html
extra_containers
https://github.com/opendatahub-io/jupyterhub-odh
    https://github.com/jupyter-on-openshift/jupyter-notebooks
    https://github.com/jupyter-on-openshift/jupyterhub-quickstart

https://github.com/opendatahub-io/jupyterhub-odh/blob/master/.jupyter/jupyterhub_config.py
https://github.com/red-hat-data-services/odh-manifests/blob/master/jupyterhub/jupyterhub/base/jupyterhub-configmap.yaml#L8
Václav (Vašek) Pavlín11:16 AM
https://github.com/red-hat-data-services/odh-manifests/tree/master/jupyterhub
Václav (Vašek) Pavlín11:27 AM
https://github.com/opendatahub-io/odh-manifests/tree/master/jupyterhub


https://github.com/opendatahub-io/odh-manifests/blob/master/kfdef/kfctl_openshift.yaml
How to install: 
    http://opendatahub.io/docs/getting-started/quick-installation.html

    Customizing the Installation
    https://opendatahub.io/docs/administration/installation-customization/customization.html
Kubespawner docs: 
    https://jupyterhub-kubespawner.readthedocs.io/en/latest/spawner.html
    https://github.com/jupyterhub/kubespawner
look for extra_containers
Jupyterhub custom namespace: 
    https://github.com/opendatahub-io/odh-manifests/tree/master/jupyterhub#deploying-jupyterhub-notebooks-to-custom-namespaces
KFDEF CR:   
    https://github.com/opendatahub-io/odh-manifests/blob/master/kfdef/kfctl_openshift.yaml#L106
Customizing deployment manifests: 
    http://opendatahub.io/docs/administration/installation-customization/customization.html
jupyterhub_config.py configmap: 
    https://github.com/opendatahub-io/odh-manifests/blob/master/jupyterhub/jupyterhub/base/jupyterhub-configmap.yaml#L8
        jupyterhub_config:""



https://github.com/opendatahub-io/jupyterhub-singleuser-profiles
vpavlin
vpavlin@redhat.com
https://github.com/opendatahub-io/manifests
KFDef
https://github.com/opendatahub-io/manifests/pull/75/files#diff-7fc0c157337e327a063a2ea590d2bd249881437d45ae2ecee09b19b0e3a94317            

[research - build and deploy jupyterhub in k8s]
Jupyter on OpenShift Part 3: Creating a S2I Builder Image
  -  https://cloud.redhat.com/blog/jupyter-on-openshift-part-3-creating-a-s2i-builder-image
     https://cloud.redhat.com/blog/jupyter-on-openshift-part-4-adding-a-persistent-workspace
     https://cloud.redhat.com/blog/jupyter-on-openshift-part-5-ad-hoc-package-installation
     https://cloud.redhat.com/blog/jupyter-on-openshift-part-6-running-as-an-assigned-user-id
     https://cloud.redhat.com/blog/jupyter-on-openshift-part-7-adding-the-image-to-the-catalog
        -repo: https://github.com/GrahamDumpleton-abandoned/s2i-minimal-notebook
     https://cloud.redhat.com/blog/jupyter-openshift-part-2-using-jupyter-project-images?extIdCarryOver=true&sc_cid=7013a000002pop9AAA

    []  
     https://github.com/jupyter-on-openshift/poc-hub-openshift-auth # build and deploy jupyterhub
        oc new-app https://raw.githubusercontent.com/jupyter-on-openshift/poc-hub-openshift-auth/master/templates/jupyterhub.json

        -> https://github.com/opendatahub-io/jupyterhub-odh  (fork)

    https://github.com/jupyter-on-openshift/poc-hub-keycloak-auth.git


     https://github.com/GrahamDumpleton-abandoned/jupyter-notebooks
        oc import-image getwarped/s2i-notebook-python35 --confirm
        oc create -f https://raw.githubusercontent.com/getwarped/jupyter-notebooks/master/openshift/templates.json

https://kienmn97.medium.com/manually-deploy-jupyterhub-on-kubernetes-for-a-single-machine-dbcd9c9e50a4    

    


[Other good examples]
    - https://github.com/jupyter-on-openshift/poc-hub-keycloak-auth
    - https://github.com/jupyter-on-openshift/poc-hub-openshift-auth


****************************************************************
https://www.katacoda.com/openshift/courses/ai-machine-learning/jupyterhub-service

oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/templates/jupyterhub-builder.json
oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/templates/jupyterhub-deployer.json
oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/templates/jupyterhub-quickstart.json
oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/templates/jupyterhub-workspace.json

oc new-app --template jupyterhub-workspace --param CLUSTER_SUBDOMAIN=A.B.C.D.nip.io \
           --SPAWNER_NAMESPACE=`oc project --short` --param VOLUME_SIZE=1Gi --param IDLE_TIMEOUT=3600

#image stream to OCP
oc create -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyter-notebooks/master/image-streams/s2i-minimal-notebook.json
oc create -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyter-notebooks/master/build-configs/s2i-minimal-notebook.json

oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/image-streams/jupyterhub.json
oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/build-configs/jupyterhub.json

oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/templates/jupyterhub-builder.json
oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/templates/jupyterhub-deployer.json
oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/templates/jupyterhub-quickstart.json
curl -L -O https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/templates/jupyterhub-quickstart.json
    image: centos/postgresql-10-centos7
    image: registry.redhat.io/rhel8/postgresql-96

oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyter-notebooks/master/image-streams/s2i-minimal-notebook.json
oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/image-streams/jupyterhub.json
oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/build-configs/jupyterhub.json

oc apply -f https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/templates/jupyterhub-workspace.json

# use a template
oc new-app --template jupyterhub-deployer

oc new-app --template jupyterhub-quickstart \
  --param APPLICATION_NAME=jakevdp \
  --param GIT_REPOSITORY_URL=https://github.com/jakevdp/PythonDataScienceHandbook \
  --param BUILDER_IMAGE=s2i-minimal-notebook:3.5
  ERROR >>> No package 'hdf5' found

oc delete all,configmap,pvc,dc,serviceaccount,rolebinding --selector app=jupyterhub -n jupyterhub

[JupyterHub (OpenShift Authenticator)] https://github.com/opendatahub-io/jupyterhub-odh 

oc create -f https://raw.githubusercontent.com/aicoe/jupyterhub-ocp-oauth/master/templates.json

oc new-app --template jupyterhub-ocp-oauth \
  --param STORAGE_CLASS=gp2

rm -rf downloads/ upload/ &&  s2i build --with-builder podman  .  quay.io/odh-jupyterhub/jupyterhub:v3.5.4 quay.io/${USER}/jupyterhub-img:url && podman push quay.io/${USER}/jupyterhub-img:url

rm -rf downloads/ upload/ &&  
s2i build --with-builder docker  .  quay.io/odh-jupyterhub/jupyterhub:v3.5.4 quay.io/myeung/jupyterhub-img:latest
 && dman push quay.io/${USER}/jupyterhub-img:url

export USER=myeung
 s2i build --with-builder podman  .  quay.io/odh-jupyterhub/jupyterhub:v3.5.4 quay.io/${USER}/jupyterhub-img:url

`s2i build https://github.com/opendatahub-io/jupyterhub-odh.git quay.io/myeung/jupyterhub:v3.5.3 quay.io/odh-jupyterhub/jupyterhub-img:latest` from this config file: https://github.com/opendatahub-io/jupyterhub-odh/blob/master/.aicoe-ci.yaml

1. Fork https://github.com/opendatahub-io/jupyterhub-singleuser-profiles
2. Update dependency reference in Pipfile (ref is commit id or potentially a branch, git is your fork)
3. Run pipenv lock to update Pipfile.lock
    4a. If you use Docker, you can run s2i directly
    s2i build . quay.io/odh-jupyterhub/jupyterhub:v3.5.1  quay.io/$USER/jupyterhub-img:some-fix
    4b. Otherwise generate Containerfile and use podman or buildah
    s2i build . quay.io/odh-jupyterhub/jupyterhub:v3.5.1 --as-dockerfile Containerfile
    podman build --tls-verify=false --layers -f Containerfile quay.io/$USER/jupyterhub-img:some-fix
5. Push
6. Update jupyterhub-img ImageStream

s2i build . quay.io/odh-jupyterhub/jupyterhub:v3.5.4  quay.io/myeung/jupyterhub-img:v1

s2i generate ...
s2i build ... --as-dockerfile xxx

s2i vs oc new-build
oc new-build openjdk-11-rhel8:1.0~ssh://git@git.xxx.int:7999/app-ma/ma-mm.git#CM-825-ocp-lab —context-dir=ma-mm-jar \
     —source-secret repo-at-ocpteknik123 —allow-missing-imagestream-tags —build-config-map=settings-mvn:/tmp/artifacts/configuration

[jupyterhub-odh] OpenShift Authenticator
    https://github.com/opendatahub-io/jupyterhub-odh

    oc new-build --name jupyterhub-imgg python:3.6-ubi8~https://github.com/opendatahub-io/jupyterhub-odh.git
    s2i build . quay.io/odh-jupyterhub/jupyterhub:v3.5.4 quay.io/myeung/jupyterhub-img:latest

[opendatahub-io/odh-manifests] https://github.com/opendatahub-io/odh-manifests
    - odh components kustomize manifests

[jsp-wrapper]
    make remote

    [https://github.com/myeung18/jupyterhub-singleuser-profiles]
        - 
****************************************
[kubeflow]
    https://learning.oreilly.com/scenarios/deploy-kubeflow/9781098116217/


[OAuth + JupyterHub Authenticator = OAuthenticator heart] with OpenShfitOAuthenticator
    https://github.com/jupyterhub/oauthenticator
    https://github.com/opendatahub-io/oauthenticator


[https://github.com/opendatahub-io/opendatahub-operator]
    - operator deploys and manages kubeflow (https://www.kubeflow.org/docs/started/installing-kubeflow/)

[jupyterhub discussion]
    https://discourse.jupyter.org/c/jupyterhub/10

[Python]
    https://realpython.com/pipenv-guide/
    vs : pip, virtualenv, requirements.txt
    pipenv shell
    pipenv --venv | --where
    pipenv update
    pipenv install --ignore-pipfile  #use pipfile.lock to install
    Package Distribution
      - setup.py 

    jupyterhub-singleuser-profiles = {editable = true, ref = "learning", git = "https://github.com/myeung18/jupyterhub-singleuser-profiles.git"}
    
        "jupyterhub-singleuser-profiles": {
            "editable": true,
            "git": "https://github.com/myeung18/jupyterhub-singleuser-profiles.git",
            "hashes": [
                "sha256:694496326df169e2a0d6cddb17ad7d63118d70634dce1c5eb025f9f6eb0b2227",
                "sha256:a77abdecaf1b183e718ebf03bf34ab4c207fa93104dee0fa780674c4b58edab8"
            ],
            "ref": "16667f5f14f106b2378162da762c11908f1252de"
        },