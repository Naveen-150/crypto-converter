# Crypto Converter Web App

## Overview
The **Crypto Converter Web App** is a simple, web-based application that allows users to convert various cryptocurrencies in real-time using data from the **CoinGecko API**. The app is built using **Flask** for the backend and a minimal frontend with HTML, CSS, and JavaScript.

## Features
- Convert popular cryptocurrencies like Bitcoin, Ethereum, Litecoin, and more.
- Real-time price fetching using **CoinGecko API**.
- Responsive and user-friendly interface.
- Lightweight and easy to deploy on **Akash Network**.
- **CI/CD automation with GitHub Actions** for seamless deployment.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **API**: CoinGecko API
- **Deployment**: Akash Network
- **CI/CD**: GitHub Actions & Docker

## Installation & Setup
### Prerequisites
Ensure you have Python installed (>= 3.7).

### Clone the Repository
```sh
git clone https://github.com/Naveen-150/crypto-converter.git
cd crypto-converter
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the Application Locally
```sh
python app.py
```
The app will be available at `http://localhost:8080`.

## API Usage Example
To convert **1 Bitcoin to Ethereum**, make a GET request:
```sh
curl "http://localhost:8080/convert?amount=1&from=bitcoin&to=ethereum"
```
**Response:**
```json
{
  "from": "bitcoin",
  "to": "ethereum",
  "original_amount": 1,
  "converted_amount": 14.32
}
```

## Deployment on Akash Network
### 1. Create Deployment YAML (`deploy.yaml`)
Define resources, services, and environment variables needed for Akash deployment.

### 2. Submit Deployment to Akash
Use the Akash Console or CLI to submit and deploy the service:
```sh
akash tx deployment create deploy.yaml --from your_wallet
```
Monitor your deployment and ensure the service is running.

##  CI/CD Automation with GitHub Actions
This project includes **GitHub Actions** for automated deployment:
- When code is pushed to the `main` branch, GitHub Actions:
  1. **Builds a Docker image** and pushes it to **Docker Hub**.
  2. **Deploys the latest image** to **Akash Network** automatically.

### ⚙ Setting Up GitHub Actions
To enable CI/CD, add the following **GitHub Secrets**:
- `DOCKER_USER` – Your Docker Hub username.
- `DOCKER_PASSWORD` – Your Docker Hub password.
- `AKASH_WALLET` – Your Akash wallet address.
- `AKASH_KEY` – Your Akash wallet private key.

## Demo Video
_A demo video showcasing the app will be added soon._

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is open-source and available under the **MIT License**.

---
_Developed & Deployed on Akash Network_ 

