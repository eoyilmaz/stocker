# -*- coding: utf-8 -*-
# Stocker a data conversion tool for stock image/video sites.
# Copyright (C) 2018 Erkan Ozgur Yilmaz
#
# This file is part of Stocker.
#
# Stocker is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# Stocker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with Stocker.  If not, see <http://www.gnu.org/licenses/>


class Status:
    """Stock status
    """

    statuses = ['Pending', 'Accepted', 'Rejected']


class StockManager:
    """This is a helper class that generates CSV files from TXT files in
    different format.

    Does several things mostly related to file system.
    """

    def __init__(self):
        self.media = []

    @classmethod
    def generate_csv(cls, path):
        """Generates CSV files from txt files at the given path.

        It searches for the path for TXT files, generates a list and then
        searches other files with the same names.

            Media1.mov  \
                         } it wil match these two files
            Media1.json /

        It accepts txt files in the following format.

        title,description,category,keywords,country,poster_timecode,releases,
        editorial

        This is the GenericStock format.

        It doesn't need to read the related media name because the filename

        :param path: A path to a folder where the txt files resides.
        :return:
        """
        raise NotImplementedError()

    def discover_media(self, path):
        """Discovers media in the given path.

        What is a media? Should we use file extensions like ['*.mov', '*.mp4'

        :param path:
        :return:
        """
        raise NotImplementedError()


class StockBase:
    """The base class for other stock classes
    """

    csv_header = ''
    format = ''

    def __init__(self, filename="", path="", title="", keywords=None):

        if keywords is None:
            keywords = []

        self.filename = filename
        self.path = path
        self.title = title
        self.keywords = keywords

    def to_csv(self):
        """abstract method
        """
        raise NotImplementedError()

    def from_file(self, path):
        """Extract metadata from the given JSON file
        """
        import json
        with open(path) as f:
            data = json.load(f)

        self.title = data['title']
        self.keywords = data['keywords']

    def from_sidecar_file(self):
        """Extracts metadata from the JSON file that resides right beside the
        original file.
        """
        # read from the the sidecar file
        # the sidecar file should be in the same path
        # with the same file name but with json extension
        self.from_file(self.sidecar_full_path)

    def to_sidecar_file(self):
        """dumps the data to sidecar file
        """
        import json

        raw_data = {
            'title': self.title,
            'keywords': self.keywords
        }
        with open(self.sidecar_full_path, 'w') as f:
            json.dump(raw_data, f, indent=2)

    @property
    def sidecar_filename(self):
        """returns the sidecar filename based on the filename
        """
        import os
        filename, ext = os.path.splitext(self.filename)
        return '%s.json' % filename

    @property
    def sidecar_full_path(self):
        import os
        return os.path.join(self.path, self.sidecar_filename)


class GenericStock(StockBase):
    """Generic stock data structure for data conversion

    To make things a little bit simple, this class uses ShutterStock category
    format not because it is more complete but it was the first one that the
    author of this library has dealt with.
    """

    csv_header = 'filename,title,description,category,keywords,country,' \
                 'poster_timecode,releases,editorial'

    categories = [
        'Abstract',
        'Animals/Wildlife',
        'Arts',
        'Backgrounds/Textures',
        'Beauty/Fashion',
        'Buildings/Landmarks',
        'Business/Finance',
        'Celebrities',
        'Education',
        'Food and drink',
        'Healthcare/Medical',
        'Holidays',
        'Industrial',
        'Interiors',
        'Miscellaneous',
        'Nature',
        'Objects',
        'Parks/Outdoor',
        'People',
        'Religion',
        'Science',
        'Signs/Symbols',
        'Sports/Recreation',
        'Technology',
        'Transportation',
        'Vintage'
    ]

    to_adobe_stock_categories = {
        'Abstract': 'Graphic Resources',
        'Animals/Wildlife': 'Animals',
        'Arts': 'Lifestyle',
        'Backgrounds/Textures': 'Graphic Resources',
        'Beauty/Fashion': 'Lifestyle',
        'Buildings/Landmarks': 'Buildings and Architecture',
        'Business/Finance': 'Business',
        'Celebrities': 'People',
        'Education': 'People',
        'Food and drink': 'Food',
        'Healthcare/Medical': 'Science',
        'Holidays': 'Travel',
        'Industrial': 'Industry',
        'Interiors': 'Buildings and Architecture',
        'Miscellaneous': 'Graphic Resources',
        'Nature': 'Landscapes',
        'Objects': 'Lifestyle',
        'Parks/Outdoor': 'Buildings and Architecture',
        'People': 'People',
        'Religion': 'Culture and Religion',
        'Science': 'Science',
        'Signs/Symbols': 'Graphic Resources',
        'Sports/Recreation': 'Sports',
        'Technology': 'Technology',
        'Transportation': 'Transport',
        'Vintage': 'Culture and Religion'
    }

    from_adobe_stock_categories = {}

    def __init__(self, filename="", path="", title="", description="",
                 category1="", category2="", keywords=None, country="",
                 poster_timecode="", releases=None, editorial=False):
        super(GenericStock, self).__init__(
            filename=filename, path=path, title=title, keywords=keywords
        )

        if releases is None:
            releases = []

        self.description = description
        self.category1 = category1
        self.category2 = category2
        self.country = country
        self.poster_timecode = poster_timecode
        self.releases = releases
        self.editorial = editorial

        # initialize the from_adobe_stock_categories
        for key, value in self.to_adobe_stock_categories.items():
            if value not in self.from_adobe_stock_categories:
                self.from_adobe_stock_categories[value] = key

    def from_(self, other_stock):
        """converts from other stock
        """
        if isinstance(other_stock, ShutterStock):
            self.from_shutter_stock(other_stock)
        elif isinstance(other_stock, AdobeStock):
            self.from_adobe_stock(other_stock)
        elif isinstance(other_stock, GettyImages):
            self.from_getty_images(other_stock)

    def from_shutter_stock(self, shutter_stock):
        """reads data from ShutterStock
        """
        self.filename = shutter_stock.filename
        self.title = shutter_stock.title
        self.category1 = shutter_stock.category1
        self.category2 = shutter_stock.category2
        self.editorial = shutter_stock.editorial
        self.keywords = shutter_stock.keywords

    def to_shutter_stock(self):
        """converts the data to ShutterStock
        """
        return ShutterStock(
            filename=self.filename,
            title=self.title,
            keywords=self.keywords,
            category1=self.category1,
            category2=self.category2,
            editorial=self.editorial
        )

    def from_adobe_stock(self, adobe_stock):
        """Fills data from the given AdobeStock instance

        :param AdobeStock adobe_stock: AdobeStock instance
        :return:
        """
        self.filename = adobe_stock.filename
        self.title = adobe_stock.title
        self.keywords = adobe_stock.keywords
        self.category1 = self.from_adobe_stock_categories[adobe_stock.category]
        self.releases = adobe_stock.releases

    def to_adobe_stock(self):
        """converts the data to AdobeStock CSV format
        """
        return AdobeStock(
            filename=self.filename,
            title=self.title,
            keywords=self.keywords,
            category=self.to_adobe_stock_categories[self.category1]
            if self.category1 != '' else '',
            releases=self.releases
        )

    def from_getty_images(self, getty_images):
        """Fills data from the given AdobeStock instance

        :param GettyImages getty_images: GettyImages instance
        :return:
        """
        self.filename = getty_images.filename
        self.title = getty_images.title
        self.keywords = getty_images.keywords

    def to_getty_images(self):
        """converts the data to GettyImages instancce
        """
        return GettyImages(
            filename=self.filename,
            title=self.title,
            description=self.title,
            keywords=self.keywords
        )

    def to_csv(self):
        """converts data to CSV format
        """
        raise NotImplementedError()

    def from_file(self):
        """parses data from a file
        """
        raise NotImplementedError()


class ShutterStock(StockBase):
    """Data structure for ShutterStock
    """

    csv_header = 'filename,title,keywords,category,editorial'

    format = '{filename},"{title}","{keywords}","{category1},{category2}",' \
             '{editorial}'

    def __init__(self, filename='', path='', title='', category1='',
                 category2='', editorial=False, keywords=None):
        super(ShutterStock, self).__init__(
            filename=filename, path=path, title=title, keywords=keywords
        )

        self.category1 = category1
        self.category2 = category2
        self.editorial = editorial

    def to_csv(self):
        """converts the the data to CSV
        """
        return self.format.format(
            filename=self.filename,
            title=self.title,
            keywords=','.join(self.keywords),
            category1=self.category1,
            category2=self.category2,
            editorial='yes' if self.editorial else 'no'
        )

    def to_adobe_stock(self):
        """Returns an AdobeStock instance
        """
        gst = GenericStock()
        gst.from_(self)
        return gst.to_adobe_stock()

    def from_file(self):
        """reads data from file
        """
        raise NotImplementedError()


class AdobeStock(StockBase):
    """Data structure for AdobeStock
    """

    csv_header = 'filename,title,keywords,category,releases'
    format = '{filename},{title},"{keywords}",{category},""'

    category_dict = {
        'Animals': 1,
        'Buildings and Architecture': 2,
        'Business': 3,
        'Drinks': 4,
        'The Environment': 5,
        'States of Mind': 6,
        'Food': 7,
        'Graphic Resources': 8,
        'Hobbies and Leisure': 9,
        'Industry': 10,
        'Landscapes': 11,
        'Lifestyle': 12,
        'People': 13,
        'Plants and Flowers': 14,
        'Culture and Religion': 15,
        'Science': 16,
        'Social Issues': 17,
        'Sports': 18,
        'Technology': 19,
        'Transport': 20,
        'Travel': 21
    }

    def __init__(self, filename='', path='', title='', category='',
                 keywords=None, releases=None):
        super(AdobeStock, self).__init__(
            filename=filename, path=path, title=title, keywords=keywords
        )
        if releases is None:
            releases = []

        self.category = category
        self.releases = releases

    def to_csv(self):
        """converts the data to CSV
        """
        return \
            '{filename},"{title}","{keywords}",{category},"{releases}"'.format(
                filename=self.filename, title=self.title,
                category=self.category_dict[self.category],
                keywords=','.join(self.keywords),
                releases=','.join(self.releases)
            )

    def to_shutter_stock(self):
        """returns a ShutterStock object
        """
        gst = GenericStock()
        gst.from_(self)
        return gst.to_shutter_stock()

    def to_getty_images(self):
        """returns a GettyImages object
        """
        gst = GenericStock()
        gst.from_(self)
        return gst.to_getty_images()

    def from_file(self):
        """reads from file
        """
        raise NotImplementedError()


class GettyImages(StockBase):
    """Data structure for GettyImages
    """

    csv_header = 'file name,description,country,title,keywords,poster ' \
                 'timecode'

    format = '{filename},"{description}",{country},"{title}","{keywords}",' \
             '{poster_timecode}'

    def __init__(self, filename='', path='', title='', description='',
                 country='', keywords=None, poster_timecode='00:00:00:00'):
        super(GettyImages, self).__init__(
            filename=filename, path=path, title=title, keywords=keywords
        )
        self.description = description
        self.country = country
        self.poster_timecode = poster_timecode

    def to_csv(self):
        """returns the data in CSV format
        """
        return self.format.format(
            filename=self.filename,
            description=self.description,
            country=self.country,
            title=self.title,
            keywords=','.join(self.keywords),
            poster_timecode=self.poster_timecode
        )

    def to_adobe_stock(self):
        """Returns a AdobeStock object
        :return:
        """
        gst = GenericStock()
        gst.from_(self)
        return gst.to_adobe_stock()

    def to_shutter_stock(self):
        """Returns a ShutterStock object
        :return:
        """
        gst = GenericStock()
        gst.from_(self)
        return gst.to_shutter_stock()

    def from_file(self):
        """reads from file
        """
        raise NotImplementedError()
