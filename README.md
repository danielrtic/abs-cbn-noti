# abs-cbn-news scraping

## Description:

Web scraping with python to extract titles and links from the news website and send them by email: https://news.abs-cbn.com/

All extractions will go through deepl translation or deep_translator python module.


# Implementation

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
```
And then restart the service.

``service cron restart``.


