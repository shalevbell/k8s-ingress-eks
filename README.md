Apply order:

Add 2 config maps:
(kubectl create configmap bg --from-literal=BG_COLOR=pink
kubectl create configmap bg2 --from-literal=BG_COLOR=blue)

Apply nginx ingress controller (kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml)

Add IP from remote nfs server to pv config and edit /etc/exports at nfs server to include cluster nodes.

Apply pv and pvc.

Change LB url in ingress.yaml to match the url of the LB that was launched by eks and apply ingress resource.

Apply both deployments along with services.

Access each project from the LB url along with the fitting prefix.
