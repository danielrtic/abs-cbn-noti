# abs-cbn-news scraping

## Description:

Web scraping with python to extract titles and links from the news website and send them by email: https://news.abs-cbn.com/

All extractions will go through deepl translation or deep_translator python module.

## Origin of this project

This project was created to learn how to use python to extract data from a website and send it by email.

Also because I like to know every day the news from the Philippines and that they reach me by email.

## Implementation

### Python modules required:

You will need to run pip to install the following python modules

```
pip install requests
pip install bs4
pip install python-decouple
pip install deep_translator
pip install lxml
```
### To configure the project:

You must open from the root folder of the project the ".env" file.

open to configure the json api of your proxy provider, user and password of the smtp email server you have and the corresponding mails (from and where you want to be notified).

Some scripts still work with the deepl api, you will need it, it is free and the per character limit itself fits in without problems.

Although in a future update this will be removed and the deep_translator module will be used with google translator to remove script execution limits.

It has to be placed in the cront tab like this

### make the script run with crontab

``sudo nano /etc/crontab``

```
Example of job definition:
.---------------- minute (0 - 59)
|  .------------- hour (0 - 23)
|  |  .---------- day of month (1 - 31)
|  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
|  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)
|  |  |  |  |
*  *  *  *  * user-name  path to script .py
```
And then restart the service.

``service cron restart``

## Future updates:

- Improve how to extract and pass everything to deep_translator and abandon deepl (due to the limitations of the free api).

- Implement other scripts for other sections of abs-cbn news web site