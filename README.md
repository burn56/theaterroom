# Plex Web Trigger Setup

## How to Find Your Plex Player ID

1. Open a web browser and navigate to your Plex Web interface (`http://your-plex-server-ip:32400/web`).
2. Log in with your Plex account credentials.
3. Click on the settings icon (the wrench and screwdriver) in the top-right corner.
4. Navigate to "Authorized Devices" under the "Devices" section.
5. Look for your device (e.g., Xbox) in the list and click on it to view its details.
6. Copy the Player ID (also known as "Device ID" or "Machine Identifier").

## How to Get Your Plex Token

1. Open a web browser and navigate to your Plex Web interface.
2. Log in with your Plex account credentials.
3. Right-click on any movie or show in your library and select "Get Info."
4. Click "View XML" in the bottom right corner of the info window.
5. In the URL of the XML page, find the parameter `X-Plex-Token=YOUR_TOKEN_HERE`.
6. Copy the token value.

## How to Add to Portainer

1. Make sure you have Portainer installed and running on your Synology NAS.
2. Open Portainer and go to the "Stacks" section.
3. Click "Add Stack."
4. Name your stack (e.g., `plex-web-trigger`).
5. Copy and paste the content of your `docker-compose.yml` file into the "Web editor" field.
6. Click "Deploy the stack."
7. Once the stack is deployed, you can access the Flask app by visiting `http://your-synology-ip:5000/play_movie`.

## Configuring Your RFID Token

Configure your RFID token in Hubitat to open the URL `http://your-synology-ip:5000/play_movie` when scanned, which will trigger the movie playback on your Plex server.