## Kubernetes ingress version upgrade (v1beta1 to v1)
- This project was made for automating the process of converting lots of ingress yaml files to apiVersion v1, since the Kubernetes version 1.22 deleted the v1beta1 API
- Read the following section before running the Python app

### Before running main.py
- Check if file "ingress_convert.yaml" follows the structure:
```
--- 
### hml-websites-example
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: hml-websites-public
  namespace: hml-website-example
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/load-balancer-name: hml-websites-pub
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP":80, "HTTPS": 443}]'
    alb.ingress.kubernetes.io/success-codes: 200,301,302
spec:
  rules:
    - host: hml-www.example.com.br
      http:
        paths:
          - path: /*
            backend:
              serviceName: hml-www-example
              servicePort: 3000

---
### prd-website-example
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: prd-websites-public
  namespace: prd-website-example
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/load-balancer-name: prd-websites-pub
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP":80, "HTTPS": 443}]'
    alb.ingress.kubernetes.io/success-codes: 200,301,302
spec:
  rules:
    - host: prd-www.example.com.br
      http:
        paths:
          - path: /*
            backend:
              serviceName: prd-www-example
              servicePort: 3000
```
- Where "---" separates yamls and "###" define the name of the files that will be created
- Check if kubectl convert is installed 