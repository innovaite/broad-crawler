# broad-crawler
## To test the crawler for yourself, follow the steps listed below.
1. Install Scrapy using the following command:
```
pip install scrapy
```
2. Create a ```broad-crawler``` directory and begin a new Scrapy project by running the following command in the ```broad-crawler``` directory:
```
scrapy startproject broad
```
This will create a ```broad``` directory with the following contents:
```
broad/
    scrapy.cfg
    broad/
        __init__.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
```
3. In the ```spiders``` directory, create a file named ```spider.py```, in which you will place the code from the corresponding file in this repository.

4. In the first ```broad``` directory, create 3 new files named ```combine.py```, ```format```, and ```script.py```, in which you will place the code from the corresponding files in this repository.

5. Replace ```ENDPOINT``` in the last line of ```script.py``` with your Elasticsearch domain's endpoint.

6. To run the program, execute the following command:
```
python script.py DOMAIN
```
where ```DOMAIN``` is the name of the website. For example, to scrape and upload the text at https://www.innovaite.com/, run the following command:
```
python script.py innovaite
```
