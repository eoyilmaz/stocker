# stocker
Stock data conversion between ShutterStock, AdobeStock and GettyImages

**Motivation**

Don't convert data from one stock site to other by hand.

**Goal**

Supply UI for the user to upload their files to the three big stock sites
and let them enter the information only once. The system should convert the
metadata from one site to the other.

**API Usage**

Any file that has a Json sidecar file is considered a valid media file. So if
there is a file named ``birds.mp4`` along with the ``birds.json`` than this
file is considered as a media and the system can read metadata from the sidecar
file.

The sidecar file format is as follows:

```json
{
  "title": "title",
  "description": "description",
  "category1": "category1",
  "category2": "category2",
  "keywords": ["list of keywords"],
  "country": "The Name of the country",
  "poster_timecode": "Poster time code as a string like 00:00:01",
  "releases": ["model release filenames"],
  "editorial": false
}
```

This file contains all the information needed to generate data for all the
three major stock sites.

Example:

```python
from stocker.models import StockManager, ShutterStock

sm = StockManager()
sm.discover_media("path")  # The path should point to a folder that has
                           # media files along with json sidecar files.

# now if there is any media file discovered
# then it is in sm.media list

for s in sm.media:
    print(sm.media.filename)

# we can now generate a CSV file for ShutterStock with the metadata
csv_content = sm.generate_csv(ShutterStock)

# and we can write the content to a file
with open('path_to_csv_file.csv', 'w') as f:
    f.write(csv_content)
```

that's it. Now you can upload your media files and also upload the CSV file
to the server to enter the metadata information.

And then we can generate one CSV file for AdobeStock:

```python
from stocker.models import StockManager, AdobeStock
sm = StockManager()
sm.discover_media("path") 
adobe_csv_content = sm.generate_csv(AdobeStock)
with open('path_to_csv_file.csv', 'w') as f:
    f.write(adobe_csv_content)
```

as you have noticed we did not change our category information for AdobeStock.
The system does that automatically.
