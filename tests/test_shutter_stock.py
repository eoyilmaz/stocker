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
    """test initialization
    """
    from stocker.models import ShutterStock
    sst = ShutterStock()
    assert isinstance(sst, ShutterStock)


def test_data_structure():
    """test some simple data
    """
    from stocker.models import ShutterStock
    sst = ShutterStock()

    # test data
    filename = 'footage_filename.mov'
    title = 'Up to 200 characters,Most important keywords first. ' \
            'Max 50 keywords.'
    category1 = 'Holidays'
    category2 = 'Transportation'
    keywords = [
        'background',
        'bay',
        'behind',
        'blue',
        'boat',
        'city',
        'cloud',
    ]

    sst.filename = filename
    sst.title = title
    sst.category1 = category1
    sst.category2 = category2
    sst.keywords = keywords

    assert sst.filename == filename
    assert sst.title == title
    assert sst.category1 == category1
    assert sst.category2 == category2
    assert sst.keywords == keywords


def test_initialization_with_keywords():
    """test some simple data
    """
    from stocker.models import ShutterStock

    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'title': 'Up to 200 characters,Most important keywords first. '
                 'Max 50 keywords.',
        'category1': 'Holidays',
        'category2': 'Transportation',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'editorial': False
    }
    sst = ShutterStock(**kwargs)

    assert sst.filename == kwargs['filename']
    assert sst.title == kwargs['title']
    assert sst.category1 == kwargs['category1']
    assert sst.category2 == kwargs['category2']
    assert sst.keywords == kwargs['keywords']
    assert sst.editorial == kwargs['editorial']


def test_to_csv():
    """tests to_csv method
    """
    from stocker.models import ShutterStock

    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'title': 'Up to 200 characters,Most important keywords first. '
                 'Max 50 keywords.',
        'category1': 'Holidays',
        'category2': 'Transportation',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'editorial': False
    }
    sst = ShutterStock(**kwargs)

    assert sst.to_csv() == 'footage_filename.mov,"Up to 200 characters,Most ' \
                           'important keywords first. ' \
                           'Max 50 keywords.","background,bay,behind,blue,' \
                           'boat,city,cloud","Holidays,Transportation",no'


def test_conversion_to_adobe_stock():
    """Testing conversion to AdobeStock format
    """
    from stocker.models import ShutterStock

    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'title': 'Up to 200 characters,Most important keywords first. '
                 'Max 50 keywords.',
        'category1': 'Holidays',
        'category2': 'Transportation',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'editorial': False
    }
    sst = ShutterStock(**kwargs)
    ast = sst.to_adobe_stock()

    from stocker.models import AdobeStock
    assert isinstance(ast, AdobeStock)


def test_conversion_to_adobe_stock_data_integrity():
    """Testing conversion to AdobeStock format, data integrity
    """
    from stocker.models import ShutterStock

    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'title': 'Up to 200 characters,Most important keywords first. '
                 'Max 50 keywords.',
        'category1': 'Holidays',
        'category2': 'Transportation',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'editorial': False
    }
    sst = ShutterStock(**kwargs)
    ast = sst.to_adobe_stock()

    from stocker.models import AdobeStock
    assert isinstance(ast, AdobeStock)
    assert ast.filename == sst.filename
    assert ast.title == sst.title
    assert ast.category == 'Travel'
    assert ast.keywords == sst.keywords
    assert ast.releases == []
