# DiffBeep Helm Chart

This Helm chart deploys DiffBeep, a web page change monitoring tool, as a Kubernetes deployment.

## Usage

1. Build and push your Docker image to a registry, then update `values.yaml` with the image repository and tag.
2. Set your environment variables in `values.yaml` (or override via `--set` on install).
3. Install the chart:
   ```sh
   helm install diffbeep ./helm
   ```

## Configuration
- `config.URL`: URL to monitor
- `config.SELECTOR`: CSS selector for the target element
- `config.EXPECTED_TEXT`: Expected text to compare against
- `config.NOTIFY_RUN_CHANNEL`: notify.run channel URL for push notifications
- `config.INTERVAL_MINUTES`: Check interval in minutes
- `config.NOTIFICATION_TITLE`: Title for notifications
- `config.NOTIFICATION_TEXT`: Custom notification text (optional)

## Files
- `Chart.yaml`: Chart metadata
- `values.yaml`: Default values
- `templates/deployment.yaml`: Deployment manifest
- `templates/service.yaml`: Service manifest
- `templates/configmap.yaml`: ConfigMap for configuration values
