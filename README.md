# SMASH hotfix issue 279

Use [mitmproxy](https://mitmproxy.org/) to intercept SMASH requests and fix them.
See [SMASH issue #279](https://github.com/geopaparazzi/smash/issues/279).

## Usage

### Without Docker

```bash
mitmdump --mode reverse:http://gss:8080 --listen-port=8000 -s src/fix-form.py
```

### Docker

``` bash
docker run --rm -p 8000 ghcr.io/ninanor/smash-hotfix:main \
    mitmdump --mode reverse:http://gss:8080 --listen-port=8000 -s /addons/fix-form.py
```
