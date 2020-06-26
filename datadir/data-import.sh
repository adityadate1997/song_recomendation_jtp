#! /bin/bash

mongoimport --host mongo --db songs --collection app_newsongdetails --type json --file /datadir/SongDataMongo.json --jsonArray