# Rough-sleeper-Token-App
# Homeless Shelter Donation App

This Flask-based application allows donors to contribute directly to homeless shelters. Each individual is identified by an ID that links them to their shelter, and donations fund their accommodation and basic needs. The application integrates with PayPal to securely process donations.

## Features
- Individual tracking: Link donations to specific individuals.
- Shelter integration: Funds go to shelter accounts for better management.
- Donation tracking: Track fund amounts and accommodation days per individual.
- PayPal Integration: Secure payment processing.

## Setup

### Prerequisites
- Python 3.8+
- A PayPal Developer Account
- Flask

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/homeless-shelter-donation-app.git
    cd homeless-shelter-donation-app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure your PayPal API keys in `config.py`.

4. Run the application:
    ```bash
    python app.py
    ```

5. Access the app at `http://127.0.0.1:5000`.

### Folder Structure
- `app.py`: Main application logic
- `config.py`: PayPal configuration
- `templates/`: HTML templates for views

## License
MIT License
