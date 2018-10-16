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


def test_initialization():
    """testing initialization
    """
    from stocker.models import GettyImages
    gti = GettyImages()
    assert isinstance(gti, GettyImages)


def test_initialization_data_integrity():
    """testing initialization data integrity
    """
    from stocker.models import GettyImages
    gti = GettyImages()

    # test data
    filename = 'footage_filename.mov'
    description = 'this is the description'
    title = 'Stock video title'
    country = 'Turkey'
    keywords = [
        'background',
        'bay',
        'behind',
        'blue',
        'boat',
        'city',
        'cloud',
    ]
    poster_timecode = '00:00:00:00'

    gti.filename = filename
    gti.description = description
    gti.title = title
    gti.country = country
    gti.keywords = keywords
    gti.poster_timecode = poster_timecode

    assert gti.filename == filename
    assert gti.description == description
    assert gti.title == title
    assert gti.country == country
    assert gti.keywords == keywords
    assert gti.poster_timecode == poster_timecode


def test_initialization_with_keywords():
    """testing initialization with keywords
    """
    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'description': 'this is the description',
        'title': 'Stock video title',
        'country': 'Turkey',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'poster_timecode': '00:00:00:00'
    }
    from stocker.models import GettyImages
    gti = GettyImages(**kwargs)

    assert gti.filename == kwargs['filename']
    assert gti.description == kwargs['description']
    assert gti.title == kwargs['title']
    assert gti.country == kwargs['country']
    assert gti.keywords == kwargs['keywords']
    assert gti.poster_timecode == kwargs['poster_timecode']


def test_to_csv():
    """testing the to_csv() method
    """
    """testing initialization with keywords
    """
    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'description': 'this is the description',
        'title': 'Stock video title',
        'country': 'Turkey',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'poster_timecode': '00:00:00:00'
    }
    from stocker.models import GettyImages
    gti = GettyImages(**kwargs)

    assert gti.to_csv() == \
           'footage_filename.mov,"this is the description",Turkey,' \
           '"Stock video title","background,bay,behind,blue,boat,city,cloud",' \
           '00:00:00:00'


def test_to_adobe_stock():
    """testing conversion to AdobeStock
    """
    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'description': 'this is the description',
        'title': 'Stock video title',
        'country': 'Turkey',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'poster_timecode': '00:00:00:00'
    }
    from stocker.models import GettyImages
    gti = GettyImages(**kwargs)

    ast = gti.to_adobe_stock()
    from stocker.models import AdobeStock
    assert isinstance(ast, AdobeStock)


def test_to_adobe_stock_data_integrity():
    """testing conversion to AdobeStock
    """
    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'description': 'this is the description',
        'title': 'Stock video title',
        'country': 'Turkey',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'poster_timecode': '00:00:00:00'
    }
    from stocker.models import GettyImages
    gti = GettyImages(**kwargs)

    ast = gti.to_adobe_stock()
    assert ast.filename == gti.filename
    assert ast.title == gti.title
    assert ast.keywords == gti.keywords


def test_to_shutter_stock():
    """testing conversion to ShutterStock
    """
    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'description': 'this is the description',
        'title': 'Stock video title',
        'country': 'Turkey',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'poster_timecode': '00:00:00:00'
    }
    from stocker.models import GettyImages
    gti = GettyImages(**kwargs)

    sst = gti.to_shutter_stock()
    from stocker.models import ShutterStock
    assert isinstance(sst, ShutterStock)


def test_to_shutter_stock_data_integrity():
    """testing conversion to ShutterStock
    """
    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'description': 'this is the description',
        'title': 'Stock video title',
        'country': 'Turkey',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'poster_timecode': '00:00:00:00'
    }
    from stocker.models import GettyImages
    gti = GettyImages(**kwargs)

    sst = gti.to_shutter_stock()
    assert sst.filename == gti.filename
    assert sst.title == gti.title
    assert sst.keywords == gti.keywords
