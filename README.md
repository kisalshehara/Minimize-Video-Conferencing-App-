# Minimize Video Conferencing Web App

## Overview

The **Minimize Video Conferencing Web App** is a web application built using the Python Flask microframework and integrated with the Zego Cloud API. This app offers features for user authentication, meeting scheduling, and interactive video meetings with functionalities such as screen sharing, chat, and reactions

## Features

- **User Authentication**
  - **Sign In:** Create a new account.
  - **Log In:** Access your account.

- **Meeting Management**
  - **Schedule Meeting:** Create new meetings.
  - **Join Meeting:** Join existing meetings.
  - **Start New Meeting:** Initiate new meetings.

- **Video Meeting Room**
  - **Screen Sharing:** Share your screen with other participants.
  - **Chat:** Real-time messaging during meetings.
  - **Reactions:** Express yourself with reactions during meetings.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kisalshehara/Minimize-Video-Conferencing-App-
   cd Minimize-Video-Conferencing-App-
Activate the Virtual Environment:

## On Windows:

bash
Copy code
venv\Scripts\activate

## On macOS/Linux:

bash
Copy code
source venv/bin/activate

## Install Required Packages:

bash
Copy code
pip install -r requirements.txt
Configure Environment Variables:

## Create a .env file in the root directory of the project and add the following:

env
Copy code
SECRET_KEY=your_secret_key
Zego_APP_ID=your_zego_app_id
Zego_APP_SIGN_KEY=your_zego_app_sign_key
Replace your_secret_key, your_zego_app_id, and your_zego_app_sign_key with your actual values.

## Run the Flask Application:

bash
Copy code
flask run
The application will be accessible at http://127.0.0.1:5000.

## Usage
Sign In: Go to /signup to create a new account.
Log In: Go to /login to log in.
Dashboard: Navigate to /dashboard to manage your meetings.
Schedule Meeting: Use /schedule_meeting to create a new meeting.
Join Meeting: Access /meeting/<meeting_id> to join a meeting.
Meeting Room: Access /meeting_room/<meeting_id> to start or participate in a meeting, with screen sharing, chat, and reactions.

## Configuration
SECRET_KEY: Used for session management.
Zego Cloud API: Set your Zego Cloud API credentials in the .env file.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your contributions are well-documented and tested.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, please contact kisal@cabeska.lk.

## Acknowledgements
Flask: A micro web framework for Python.
Zego Cloud API: Provides real-time video and audio functionalities.