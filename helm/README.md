# NUST Scrapper Helm Chart

This Helm chart deploys the NUST selection list scrapper as a Kubernetes deployment.

## Usage

1. Build and push your Docker image to a registry, then update `values.yaml` with the image repository and tag.
2. Set your environment variables in `values.yaml` (or override via `--set` on install).
3. Install the chart:
   ```sh
   helm install nust-scrapper ./helm-chart
   ```

## Configuration
- `config.URL`: URL to scrape
- `config.SELECTOR`: CSS selector for the target element
- `config.EXPECTED_TEXT`: Expected text to compare
- `config.NOTIFY_RUN_CHANNEL`: notify.run channel URL for push notifications

## Files
- `Chart.yaml`: Chart metadata
- `values.yaml`: Default values
- `templates/deployment.yaml`: Deployment manifest
- `templates/service.yaml`: Service manifest
- `templates/configmap.yaml`: ConfigMap for configuration values
