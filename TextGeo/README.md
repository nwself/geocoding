### Requirements
Elasticsearch 5.4

### Setup
Run `./setup.sh`

### TEST
`python2 geocode.py --infile tests/test_input.json --output tests/test_output.json`

OR 

```
ipython
>>> from geocode import BaseGeo
>>> from geoutils.dbManager import ESWrapper
>>> db = ESWrapper('geonames', 'places')
>>> geo = BaseGeo(db=db)
>>> geo.geocode_fromList(["US", "Arlington", "Virginia"], [])[0]
```

### Build the .whl with
`python setup.py sdist bdist_wheel`

Then you can `pip install <url_to_whl>`

### Port forward
Just in case:
```
# Optionally add -f to this command to background it
ssh -L localhost:9200:localhost:9200 montage.cs.vt.edu -N
```
