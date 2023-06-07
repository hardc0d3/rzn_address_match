# RZN Address Match

## Project Description
Small experimental project to play with different methods for address matching.
There are two methods used:
* Google geocode - using google service directly it recognize itself *place_id* and group on it.
* Levenshtein distance - used on preprocessed address strings:
  * Addresses are translated to english with googletrans
  * Address components are split, stripped and sorted
  * Levenshtein module calculate similarity ratio on each pair
  * Names are grouped

## Setup ( Docker / Compose)
### Prerequisites
* Docker and docker-compose
* Internet access - ( for google translate and geocode )
* Googlemaps API key ( for geocode method)
  * put dot env file (.env) in project root with it
  ```commandline
    GOOLEMAPS_API_KEY='AIza...'
    ```
### 
### Run all tests and experiments
```commandline
# Run pytest 

docker-compose up rzn_match_test

# Run translation

docker-compose up rzn_match_translate

# Run Levenshtein distance method ( first it translate original source)

docker-compose up rzn_match_main_ld

# Run googlemaps API geocode method

docker-compose up rzn_match_main_gl

```
### Custom configuration
To change input and ouput of tranlate.py and main.py one can change envirnoment variables specified in docker-compose.yml.

### Working directly with command line tools and virtual env
After one creates python virtual environment

```commandline
$ pip install -r requirements.txt
$ python translate.py --help
$ python main.py --help
```


