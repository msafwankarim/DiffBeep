# 🔍 DiffBeep

A lightweight, containerized tool that monitors web pages for content changes and sends notifications when changes are detected

## Features

- 🔍 **Web Page Monitoring** - Continuously monitors specified web pages for content changes
- 🎯 **CSS Selector Targeting** - Uses precise CSS selectors to monitor specific page elements
- 📱 **Push Notifications** - Sends instant notifications via [notify.run](https://notify.run) when changes are detected
- ⏰ **Configurable Intervals** - Set custom monitoring intervals (default: 5 minutes)
- 🐳 **Docker Support** - Fully containerized for easy deployment
- ☸️ **Kubernetes/Helm Ready** - Includes Helm charts for Kubernetes deployment
- 🔧 **Environment-Based Configuration** - All settings configurable via environment variables
- ✅ **Configuration Validation** - Built-in validation ensures all required settings are present

## Quick Start

### Using Docker

#### Option 1: Using pre-built image from GitHub Container Registry

1. **Create configuration file**
   ```bash
   cp docker/config.env docker/config.local.env
   # Edit docker/config.local.env with your configuration
   ```

2. **Run with pre-built image**
   ```bash
   docker run --env-file docker/config.local.env ghcr.io/msafwankarim/diffbeep:latest
   ```

#### Option 2: Build locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/msafwankarim/DiffBeep.git
   cd diffbeep
   ```

2. **Configure environment variables**
   ```bash
   cp docker/config.env docker/config.local.env
   # Edit docker/config.local.env with your configuration
   ```

3. **Build and run with Docker**
   ```bash
   docker build -t diffbeep .
   docker run --env-file docker/config.local.env diffbeep
   ```

### Using Python Directly

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables and run**
   ```bash
   export URL="https://example.com"
   export SELECTOR=".content"
   export EXPECTED_TEXT="Current content"
   export NOTIFY_RUN_CHANNEL="https://notify.run/your-channel"
   export INTERVAL_MINUTES="5"
   export NOTIFICATION_TITLE="Change Detected!"
   export NOTIFICATION_TEXT="The page content has changed"
   
   python main.py
   ```

### Using Python Virtual Environment

1. **Create and activate virtual environment**
   ```bash
   python -m venv diffbeep-env
   source diffbeep-env/bin/activate  # On Windows: diffbeep-env\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables and run**
   ```bash
   export URL="https://example.com"
   export SELECTOR=".content"
   export EXPECTED_TEXT="Current content"
   export NOTIFY_RUN_CHANNEL="https://notify.run/your-channel"
   export INTERVAL_MINUTES="5"
   export NOTIFICATION_TITLE="Change Detected!"
   
   python main.py
   ```

4. **Deactivate when done**
   ```bash
   deactivate
   ```

## Configuration

All configuration is done through environment variables:

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `URL` | ✅ | The web page URL to monitor | `https://example.com/page` |
| `SELECTOR` | ✅ | CSS selector for the element to monitor | `.content`, `#main-text`, `table tr:first-child` |
| `EXPECTED_TEXT` | ✅ | The expected text content (change triggers notification) | `No updates available` |
| `NOTIFY_RUN_CHANNEL` | ✅ | Your notify.run channel URL | `https://notify.run/abc123` |
| `INTERVAL_MINUTES` | ✅ | Check interval in minutes | `5`, `10`, `30` |
| `NOTIFICATION_TITLE` | ✅ | Title for notifications | `Update Available!` |
| `NOTIFICATION_TEXT` | ❌ | Custom notification text (optional) | `Check the website now` |

### Setting up Notifications

1. Visit [notify.run](https://notify.run) and click "Create Channel"
2. Copy your unique channel URL (e.g., `https://notify.run/abc123xyz`)
3. Open this URL on your devices (phone, computer) and click "Subscribe"
4. Allow notifications when prompted
5. Use the channel URL as your `NOTIFY_RUN_CHANNEL` environment variable

## Kubernetes Deployment

### Option 1: Using Pre-built Helm Chart from OCI Registry

The easiest way to deploy DiffBeep to Kubernetes is using the pre-built Helm chart:

1. **Install from OCI registry**
   ```bash
   helm install diffbeep oci://ghcr.io/msafwankarim/charts/diffbeep \
     --set config.URL="https://example.com/page" \
     --set config.SELECTOR=".content" \
     --set config.EXPECTED_TEXT="Current content" \
     --set config.NOTIFY_RUN_CHANNEL="https://notify.run/your-channel" \
     --set config.NOTIFICATION_TITLE="Change Detected!"
   ```

2. **Or create a values file and install**
   ```bash
   # Create values.yaml with your configuration
   cat > my-values.yaml << EOF
   config:
     URL: "https://example.com/page"
     SELECTOR: ".content"
     EXPECTED_TEXT: "Current content"
     NOTIFY_RUN_CHANNEL: "https://notify.run/your-channel"
     INTERVAL_MINUTES: 5
     NOTIFICATION_TITLE: "Change Detected!"
     NOTIFICATION_TEXT: "Custom message"
   EOF
   
   # Install with values file
   helm install diffbeep oci://ghcr.io/msafwankarim/charts/diffbeep -f my-values.yaml
   ```

3. **Upgrade deployment**
   ```bash
   helm upgrade diffbeep oci://ghcr.io/msafwankarim/charts/diffbeep -f my-values.yaml
   ```

### Option 2: Using Local Helm Chart

Deploy using the Helm chart included in this repository:

1. **Configure values**
   ```bash
   cp helm/values.yaml helm/values.local.yaml
   # Edit helm/values.local.yaml with your configuration
   ```

2. **Deploy to Kubernetes**
   ```bash
   helm install diffbeep ./helm -f helm/values.local.yaml
   ```

3. **Upgrade deployment**
   ```bash
   helm upgrade diffbeep ./helm -f helm/values.local.yaml
   ```

### Helm Configuration

The Helm chart supports the same environment variables. Configure them in `values.yaml`:

```yaml
config:
  URL: "https://example.com"
  SELECTOR: ".content"
  EXPECTED_TEXT: "Current content"
  NOTIFY_RUN_CHANNEL: "https://notify.run/your-channel"
  INTERVAL_MINUTES: 5
  NOTIFICATION_TITLE: "Change Detected!"
  NOTIFICATION_TEXT: "Custom message"
```

## Use Cases

- **Admission Lists**: Monitor university admission results
- **Job Postings**: Track new job openings on career pages
- **Product Availability**: Watch for stock updates on e-commerce sites
- **News Updates**: Monitor news sites for breaking news
- **Government Announcements**: Track official websites for new announcements

## File Structure

```
├── main.py              # Main application code
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker container configuration
├── .github/
│   └── workflows/
│       └── build-and-publish.yml # GitHub Actions workflow
├── docker/
│   ├── config.env      # Environment template
│   └── config.local.env # Local configuration (gitignored)
├── helm/               # Kubernetes deployment chart
└── README.md          # This file
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
