# Crypto monitor

### Overview: A weekend side project for keeping an eye on the highly volatile cryptos.    

No question, we can have a web-browser open for this, or even set limit orders on any of the trading platforms.     
The script is useful if one wants to monitor the prices without having to explicitly check any browser, mobile app or set reminders.      
Since the job would be scheduled (cron), a locked text-file will pop-up at a user-defined interval of time with the required info.

Additional feature - passing limit orders as arguments, the pop-up file displays that ticker under 'Action needed' if the current rate is below the limit passed. This overrides the default values set for each crypto in the script.

For example:
By passing arguments `-b 40000 -d 0.2 -e 2500` to `python ./src/crazy_crypto.py` we get the output as:
```
!!! ALERT !!!
Date: 2021-05-23
Time: 01:54:06 UTC
------------INFO-------------
eth: 2356.41  | %: -3.84   ↓
dog: 0.346578 | %: -2.29   ↓
btc: 38220.97 | %: 0.78    ↑
--------Action needed--------
ETH  - BTFD | Limit passed: 2500.0
BTC  - BTFD | Limit passed: 40000.0
```


## Scheduling
This job is scheduled using cron.    
An example cron job:    
`59 7-20 *  * 1-5 sh /Users/yash/personal_projects/crypto_monitor/src/run_crazy_crypto.sh`       
meaning - the job runs at 59th minute of every hour from 7 am to 8 pm, every weekday.

## How to use
Clone this repo to your machine, create a virtual env (if you prefer), pip install the requirements `pip install -r requirements.txt`.   
Next, edit the path variables in the `run_crazy_crypto.sh` file.
Set up a cronjob to run this shell script as per your specifications.   
You could also run the `crazy_crypto.py` file through terminal and the output will be printed on the same.

## Possible additions
The current script just re-writes and locks (`chmod u-w`) the text file at every run, as that is what I intend to do. We can definitely change this functionality to write the data to a database for further analysis, if needed.    
The script only gets data for 3 cryptos, we can add more as required.    

Any suggestions/improvements are welcome.
