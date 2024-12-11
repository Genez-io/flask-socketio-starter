<div align="center"> <a href="https://genezio.com/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/genez-io/graphics/raw/HEAD/svg/Icon_Genezio_White.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/genez-io/graphics/raw/HEAD/svg/Icon_Genezio_Black.svg">
    <img alt="genezio logo" src="https://github.com/genez-io/graphics/raw/HEAD/svg/Icon_Genezio_Black.svg" height="100" >
  </picture>
 </div>

<div align="center">

[![Join our community](https://img.shields.io/discord/1024296197575422022?style=social&label=Join%20our%20community%20&logo=discord&labelColor=6A7EC2)](https://discord.gg/uc9H5YKjXv)
[![Follow @geneziodev](https://img.shields.io/twitter/url/https/twitter.com/geneziodev.svg?style=social&label=Follow%20%40geneziodev)](https://twitter.com/geneziodev)

</div>

# Flask-SocketIO Chat Application

A simple real-time chat application built with Flask and Socket.IO.

## Features

- Real-time messaging using WebSocket connections
- Message history persistence during server runtime
- Cross-origin resource sharing (CORS) enabled
- Broadcasting messages to all connected clients

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Genez-io/flask-socketio-starter
cd flask-socketio-starter
```

2. Install the required dependencies:
```bash
pip install flask flask-socketio flask-cors
```

## Running the Application

Start the server by running:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
flask-socketio-starter/
├── app.py              # Main application file
├── templates/          
│   └── index.html     # Frontend template
└── README.md          # This file
```

## API Endpoints

- `GET /` - Serves the main chat interface
- WebSocket Events:
  - `request_history` - Client requests message history
  - `message` - Send/receive chat messages
  - `message_history` - Receive message history from server

## Usage

1. Open the application in multiple browser windows
2. Type messages in any window
3. See messages appear in real-time across all connected clients
4. Message history is preserved during server runtime


# Deploy
:rocket: You can deploy your own version of the template to Genezio with one click:

[![Deploy to Genezio](https://raw.githubusercontent.com/Genez-io/graphics/main/svg/deploy-button.svg)](https://app.genez.io/start/deploy?repository=https://github.com/Genez-io/flask-socketio-starter)


## Genezio CLI Commands

Genezio also provides a CLI tool that you can use to deploy your project from your machine.
All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install -g genezio`  | Installs genezio globally                        |
| `genezio login`           | Logs in to genezio                               |
| `genezio local`           | Starts a local server                            |
| `genezio deploy`          | Deploys a production project                     |
| `genezio --help`          | Get help using genezio                           |

## Learn more

To learn more about Genezio, take a look at the following resources:

- [Official genezio documentation](https://genezio.com/docs)
- [Tutorials](https://genezio.com/blog)

## Contact

If you need support or you have any questions, please join us in our [Discord channel](https://discord.gg/uc9H5YKjXv). We'd love to chat!

## Built With

- [Genezio](https://genezio.com/)
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

***

<div align="center"> <a href="https://genezio.com/">
  <p>Built with Genezio with ❤️ </p>
  <img alt="genezio logo" src="https://raw.githubusercontent.com/Genez-io/graphics/main/svg/powered_by_genezio.svg" height="40">
</div>