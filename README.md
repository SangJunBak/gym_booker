## Instructions

Make sure you install Selenium and the Chrome web driver https://www.youtube.com/watch?v=2WVxzRD6Ds4. Replace `WEBDRIVER_PATH` with wherever you put chromedriver.

Replace .env.example with .env using your Duo credentials.

Once installed, run `python3 gym_booker.py`

Make sure for the `DUO_CODES`, you replace the ones there with the ones linked to your account. You can do this by logging in and pressing "Enter a Pascode" then "Send me new codes".

Currently it scrapes for PAC. If you want CIF, uncomment `GYM="CIF..."`.

## Notes

Make sure when the webdriver opens Chromium, the page is fullscreen so that nothing blocks the "date" buttons (i.e. banners). This is the cause of the error that says a button is unreachable.

## Dependencies

- pip3 install python-dotenv
- pip3 install selenium

## How it works

`WANTED_TIMES` looks like this:

```
WANTED_TIMES = [
    {
        "day": "Mon",
        "times": [],
    },
    {
        "day": "Tue",
        "times": [],
    },
    {
        "day": "Wed",
        "times": [],
    },
    {
        "day": "Thu",
        "times": ["1 - 1:50 PM", "2 - 2:50 PM", "3 - 3:50 PM", "4 - 4:50 PM"],
    },
    {
        "day": "Fri",
        "times": ["1 - 1:50 PM", "2 - 2:50 PM", "3 - 3:50 PM", "4 - 4:50 PM"],
    },
    {
        "day": "Sat",
        "times": ["1 - 1:50 PM", "2 - 2:50 PM", "3 - 3:50 PM", "4 - 4:50 PM"],
    },
    {
        "day": "Sun",
        "times": ["1 - 1:50 PM", "2 - 2:50 PM", "3 - 3:50 PM", "4 - 4:50 PM"],
    },
]
```

Make sure `times` is consistent with the other time string values. It's going to try all time slots in the array, prioritizing from first entry to last. It's going to stop once it books one.

The scraper's going to poll every 10 minutes. You can adjust this by changing `POLL_TIME_MINUTES`.
