# docker + tensorflow + flask + gunicorn + supervisor

## example app

app/web/app.py

## build

```docker build -t patrickdmiller/tensorflow-flask .```


## run

```docker run --rm -p 5000:5000 -v  /app_tf/model-builder/tf/data:/data patrickdmiller/tensorflow-flask```