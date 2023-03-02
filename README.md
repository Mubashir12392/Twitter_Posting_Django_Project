# Twitter Posting Django Project

This is a Django project that allows users to post tweets on their Twitter account using the Twitter API. Users can authenticate with their Twitter account, create a new tweet, and view their own timeline.

## Features

- Twitter authentication with OAuth
- Ability to post tweets on user's behalf
- View user's own timeline

## Getting Started

1. Clone this repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Set up your Twitter developer account and create a new app to obtain your API key, API secret key, access token, and access token secret.
4. Create a `.env` file in the root directory of the project and add your Twitter API credentials in the following format:

    CONSUMER_KEY=<your_consumer_key>
CONSUMER_SECRET=<your_consumer_secret>
ACCESS_TOKEN=<your_access_token>
ACCESS_TOKEN_SECRET=<your_access_token_secret>


5. Run `python manage.py migrate` to apply the database migrations.
6. Start the development server using `python manage.py runserver`.

## Usage

1. Navigate to `http://localhost:8000/` in your web browser.
2. Click on the "Log in with Twitter" button to authenticate with your Twitter account.
3. Once authenticated, you will be redirected to the home page where you can create a new tweet or view your own timeline.

## Contributing

Contributions are always welcome! If you have any suggestions or found a bug, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---
I'am currently working on this project.
