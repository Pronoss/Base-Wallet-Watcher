# Base Wallet Balance

A simple web service to view a wallet balance on the Base blockchain using Python and Flask.

## Features

- View the current balance of a wallet on Base.
- Validate the entered wallet address.
- Simple and intuitive web page.

## Technologies

- Python
- Flask
- Web3.py
- HTML/CSS

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/base-wallet-balance.git
    cd base-wallet-balance
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root of the project and add:

    ```env
    SECRET_KEY=your_secret_key_here
    BASE_RPC_URL=https://base-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
    ```

5. **Run the application:**

    ```bash
    python run.py
    ```

6. **Open your browser:**

    Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## License

This project is licensed under the MIT License.
