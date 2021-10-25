
```

cd /home/myeung/gosrc/gomod/secretless-broker
go run ./cmd/secretless-broker/main.go -f secretless.yml -debug


HTTP_PROXY=http://localhost:8099 python secretless.py

```





```
Dockerfile 
https://github.com/conjurdemos/kubernetes-conjur-demo/blob/main/test_app_summon/Dockerfile#L10

https://docs.conjur.org/Latest/en/Content/Integrations/Kubernetes_deployAuthenticatorSidecar.htm?tocpath=Integrations%7COpenShift%252C%20Kubernetes%7CDeploy%20Applications%7C_____1#Sidecar

```


```
docker build -t simple-python .
docker run -d -it -p 3800:3800 simple-python:latest

docker build -f Dockerfile.jup -t quay.io/myeung/os-climate-poc-app:0.1 .
```

oc get cm dap-config -n cyberlab -o yaml | sed "s/namespace: cyberlab/namespace: user3/" | oc apply -f - -n user3
oc create cm secretless-config --from-file=template/secretless.yaml -n user3

oc exec -it os-climate-app-team1-848f9b5484-ndcgl -- bash -c "python secretless.py"


Jupyter on OpenShift Part 3: Creating a S2I Builder Image
  -  https://cloud.redhat.com/blog/jupyter-on-openshift-part-3-creating-a-s2i-builder-image
     https://cloud.redhat.com/blog/jupyter-openshift-part-2-using-jupyter-project-images?extIdCarryOver=true&sc_cid=7013a000002pop9AAA


[jupyter notebook]
  oc new-app jupyter/minimal-notebook:latest -n user3
  oc new-app quay.io/myeung/os-climate-poc-app:0.1 -n user3
  oc adm policy add-scc-to-user anyuid -z default -n user3 


https://dap-service-node.cyberlab.svc.cluster.local/api/authn-k8s/os-climate-poc


























2021/10/24 16:04:31 [DEBUG] Waiting for new configuration...
2021/10/24 16:05:04 [DEBUG] HTTP Proxy on tcp://0.0.0.0:8099: Got request / secretless.empty GET secretless.empty
2021/10/24 16:05:04 [DEBUG] HTTP Proxy on tcp://0.0.0.0:8099: Using connector 'aws' for request secretless.empty
2021/10/24 16:05:04 Instantiating provider 'conjur'
2021/10/24 16:05:04 Info: Conjur provider using Kubernetes authenticator-based authentication
2021/10/24 16:05:04 Info: Conjur provider is authenticating as host/user1/os-climate-app-team1 ...
INFO:  2021/10/24 16:05:04.832046 authenticator.go:207: CAKC040 Authenticating as user 'host/user1/os-climate-app-team1'
ERROR: 2021/10/24 16:05:04.984769 authenticator.go:136: CAKC029 Received invalid response to certificate signing request. Reason: status code 401,
ERROR: 2021/10/24 16:05:04.984800 authenticator.go:240: CAKC015 Login failed
2021/10/24 16:05:04 Info: Conjur provider received an error on authenticate: CAKC015 Login failed

root@conjur-cli-5969fcdcf5-nz5gz:/# conjur list
[
  "lab:policy:root",
  "lab:policy:conjur/authn-k8s/os-climate-poc",
  "lab:variable:conjur/authn-k8s/os-climate-poc/kubernetes/service-account-token",
  "lab:variable:conjur/authn-k8s/os-climate-poc/kubernetes/ca-cert",
  "lab:variable:conjur/authn-k8s/os-climate-poc/kubernetes/api-url",
  "lab:variable:conjur/authn-k8s/os-climate-poc/ca/cert",
  "lab:variable:conjur/authn-k8s/os-climate-poc/ca/key",
  "lab:webservice:conjur/authn-k8s/os-climate-poc",
  "lab:group:conjur/authn-k8s/os-climate-poc/consumers",
  "lab:policy:LabVault",
  "lab:group:LabVault/Labs-admins",
  "lab:policy:LabVault/Labs",
  "lab:group:LabVault/Labs/LabSafe1-admins",
  "lab:policy:LabVault/Labs/LabSafe1",
  "lab:policy:LabVault/Labs/LabSafe1/delegation",
  "lab:group:LabVault/Labs/LabSafe1/delegation/consumers",
  "lab:variable:LabVault/Labs/LabSafe1/AWS/access_key",
  "lab:variable:LabVault/Labs/LabSafe1/AWS/secret_key",
  "lab:policy:user1",
  "lab:group:user1/apps",
  "lab:host:user1/os-climate-app-team1"
]
root@conjur-cli-5969fcdcf5-nz5gz:/# conjur role members host:user1/os-climate-app-team1
[
  "lab:policy:user1"
]

root@conjur-cli-5969fcdcf5-nz5gz:/# conjur authn login  -u host/user1/os-climate-app-team1 -p 361d65v1wavn821xqr32t103ecnn1ry8hj029xdb551pq6c973303bxj
Logged in
root@conjur-cli-5969fcdcf5-nz5gz:/# conjur list
[
  "lab:webservice:conjur/authn-k8s/os-climate-poc",
  "lab:variable:LabVault/Labs/LabSafe1/AWS/access_key",
  "lab:variable:LabVault/Labs/LabSafe1/AWS/secret_key"
]





















WARN: Jupyter Notebook deprecation notice https://github.com/jupyter/docker-stacks#jupyter-notebook-deprecation-notice.
Adding passwd file entry for 1000630000
Container must be run with group "users" to update files
Executing the command: jupyter notebook
Traceback (most recent call last):
  File "/opt/conda/lib/python3.9/site-packages/traitlets/traitlets.py", line 537, in get
    value = obj._trait_values[self.name]
KeyError: 'runtime_dir'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/conda/bin/jupyter-notebook", line 10, in <module>
    sys.exit(main())
  File "/opt/conda/lib/python3.9/site-packages/jupyter_core/application.py", line 264, in launch_instance
    return super(JupyterApp, cls).launch_instance(argv=argv, **kwargs)
  File "/opt/conda/lib/python3.9/site-packages/traitlets/config/application.py", line 845, in launch_instance
    app.initialize(argv)
  File "/opt/conda/lib/python3.9/site-packages/traitlets/config/application.py", line 88, in inner
    return method(app, *args, **kwargs)
  File "/opt/conda/lib/python3.9/site-packages/notebook/notebookapp.py", line 2121, in initialize
    self.init_configurables()
  File "/opt/conda/lib/python3.9/site-packages/notebook/notebookapp.py", line 1650, in init_configurables
    connection_dir=self.runtime_dir,
  File "/opt/conda/lib/python3.9/site-packages/traitlets/traitlets.py", line 577, in __get__
    return self.get(obj, cls)
  File "/opt/conda/lib/python3.9/site-packages/traitlets/traitlets.py", line 540, in get
    default = obj.trait_defaults(self.name)
  File "/opt/conda/lib/python3.9/site-packages/traitlets/traitlets.py", line 1580, in trait_defaults
    return self._get_trait_default_generator(names[0])(self)
  File "/opt/conda/lib/python3.9/site-packages/jupyter_core/application.py", line 95, in _runtime_dir_default
    ensure_dir_exists(rd, mode=0o700)
  File "/opt/conda/lib/python3.9/site-packages/jupyter_core/utils/__init__.py", line 11, in ensure_dir_exists
    os.makedirs(path, mode=mode)
  File "/opt/conda/lib/python3.9/os.py", line 215, in makedirs
    makedirs(head, exist_ok=exist_ok)
  File "/opt/conda/lib/python3.9/os.py", line 215, in makedirs
    makedirs(head, exist_ok=exist_ok)
  File "/opt/conda/lib/python3.9/os.py", line 215, in makedirs
    makedirs(head, exist_ok=exist_ok)
  File "/opt/conda/lib/python3.9/os.py", line 225, in makedirs
    mkdir(name, mode)
PermissionError: [Errno 13] Permission denied: '/home/jovyan/.local'