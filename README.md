## INTERESTING WORDS PROJECT

This small project searches for the most frequent words in a given set of files and then returns their counts as well as information on where they appear in each file (document index and sentence indexes).

### Running the project
This work is intended to be run with Docker and it contains all the necessary configuration for that.
If you wish to run it outside Docker, you will need to configure your environment according to the settings in `docker/Dockerfile`.

All the dependencies are listed in `requirements.txt` and are installed during the build stage of the docker image.

### Run docker container
```
docker-compose up
```

#### Run the code
To run the code on the input documents available in the folder `files', you can run the following command:

```
docker exec -it <container_name_or_id> python3 -m run
```

Please note that this will run the search for the first 2 most frequent words.

#### Run the linter
This code uses Flake8 as linter. To run:

```
docker exec -it <container_name_or_id> python3 -m flake8
```


#### Run the tests

```
docker exec -it <container_name_or_id> python3 -m pytest
```


### Additional comments

Keeping the container running is an intentional choice to facilitate work of the developer.

This work is not final and will require further work:

- test coverage is not adequate
- logging should provide more information about how the app works
- the pre-processing pipeline could contain more steps and allow for configuration (selection of stopwords, for example)
- the pre-processing tasks should be part of a pipeline and improvements are needed to help performance
- the output of results could be done in a more user-friendly manner (table with the actual document names and sentence texts)
- the main execution should allow for a parameter to define how many most frequent words to be returned