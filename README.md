# abs-cbn-news scraping

## Description:

Web scraping with python to extract titles and links from the news website and send them by email: https://news.abs-cbn.com/

All extractions will go through deepl translation or deep_translator python module.

## Origin of this project

This project was created to learn how to use python to extract data from a website and send it by email.

Also because I like to know every day the news from the Philippines and that they reach me by email.

## Implementation

It has to be placed in the cront tab like this

``nano /etc/crontab``

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