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


class StockBase:
    """The base class for other stock classes
    """

    format = ''

    def to_csv(self):
        """abstract method
        """
        raise NotImplementedError()

    def from_file(self):
        """abstract method
        """
        raise NotImplementedError()


class GenericStock(StockBase):
    """Generic stock data structure for data conversion

    To make things a little bit simple, this class uses ShutterStock category
    format not because it is more complete but it was the first one that the
    author of this library has dealt with.
    """

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

    def __init__(self, filename="", title="", description="", category1="",
                 category2="", keywords=None, country="", poster_timecode="",
                 releases=None, editorial=False):
        if keywords is None:
            keywords = []

        if releases is None:
            releases = []

        self.filename = filename
        self.title = title
        self.description = description
        self.category1 = category1
        self.category2 = category2
        self.keywords = keywords
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
        """converts the data to ShutterStock CSV format
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
            category=self.to_adobe_stock_categories[self.category1],
            releases=self.releases
        )

    def to_getty_images(self):
        """converts the data to GettyImages CSV format
        """
        raise NotImplementedError()

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

    format = '{filename},"{title}","{keywords}","{category1},{category2}",' \
             '{editorial}'

    def __init__(self, filename='', title='', category1='', category2='',
                 editorial=False, keywords=None):

        if keywords is None:
            keywords = []

        self.filename = filename
        self.title = title
        self.category1 = category1
        self.category2 = category2
        self.editorial = editorial
        self.keywords = keywords

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

    def __init__(self, filename='', title='', category='', keywords=None,
                 releases=None):

        if keywords is None:
            keywords = []

        if releases is None:
            releases = []

        self.filename = filename
        self.title = title
        self.keywords = keywords
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

    def from_file(self):
        """reads from file
        """
        raise NotImplementedError()


class GettyImages(StockBase):
    """Data structure for GettyImages
    """

    format_header = 'file name,description,country,title,keywords,poster ' \
                    'timecode'

    format = '{filename},{description},{country},{title},"{keywords}",' \
             'poster_timecode'

    def __init__(self):
        self.filename = ''
        self.description = ''
        self.country = ''
        self.title = ''
        self.keywords = []
        self.poster_timecode = '00:00:00'

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

    def to_adobe_stock(self, adobe_stock):
        """Returns a AdobeStock object

        :param AdobeStock adobe_stock: AdobeStock instance
        :return:
        """
        gst = GenericStock()
        gst.from_(self)
        return gst.to_adobe_stock()

    def from_file(self):
        """reads from file
        """
        raise NotImplementedError()