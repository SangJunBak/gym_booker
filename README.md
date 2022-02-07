## Instructions

Make sure you install Selenium and the Chrome web driver https://www.youtube.com/watch?v=2WVxzRD6Ds4.

Replace .env.example with .env using your Duo credentials.

Once installed, run `python3 gym_booker.py`

Make sure for the `DUO_CODES`, you replace the ones there with the ones linked to your account. You can do this by logging in and pressing "Enter a Pascode" then "Send me new codes".

Currently it scrapes for PAC. If you want CIF, uncomment `GYM="CIF..."`.

## Dependencies

pip3 install python-dotenv
pip3 install selenium
