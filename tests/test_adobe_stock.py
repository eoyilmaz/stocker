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
    from stocker.models import AdobeStock
    ast = AdobeStock()
    assert isinstance(ast, AdobeStock)


def test_data_structure():
    """test some simple data
    """
    from stocker.models import AdobeStock
    ast = AdobeStock()

    # test data
    filename = 'footage_filename.mov'
    title = 'Up to 200 characters,Most important keywords first. ' \
            'Max 50 keywords.'
    category = 'Graphic Resources'
    keywords = [
        'background',
        'bay',
        'behind',
        'blue',
        'boat',
        'city',
        'cloud',
    ]

    ast.filename = filename
    ast.title = title
    ast.category = category
    ast.keywords = keywords

    assert ast.filename == filename
    assert ast.title == title
    assert ast.category == category
    assert ast.keywords == keywords


def test_initialization_with_keywords():
    """test some simple data
    """
    from stocker.models import AdobeStock

    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'title': 'Up to 200 characters,Most important keywords first. '
                 'Max 50 keywords.',
        'category': 'Graphic Resources',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'releases': ['release1.pdf', 'release2.pdf']
    }
    ast = AdobeStock(**kwargs)

    assert ast.filename == kwargs['filename']
    assert ast.title == kwargs['title']
    assert ast.keywords == kwargs['keywords']
    assert ast.category == kwargs['category']
    assert ast.releases == kwargs['releases']


def test_to_csv():
    """tests to_csv method
    """
    from stocker.models import AdobeStock

    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'title': 'Up to 200 characters,Most important keywords first. '
                 'Max 50 keywords.',
        'category': 'Graphic Resources',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'releases': ['release1.pdf', 'release2.pdf']
    }
    ast = AdobeStock(**kwargs)

    assert ast.to_csv() == 'footage_filename.mov,"Up to 200 characters,Most ' \
                           'important keywords first. ' \
                           'Max 50 keywords.","background,bay,behind,blue,' \
                           'boat,city,cloud",8,"release1.pdf,release2.pdf"'


def test_to_shutter_stock():
    """Testing conversion to ShutterStock format
    """
    from stocker.models import AdobeStock

    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'title': 'Up to 200 characters,Most important keywords first. '
                 'Max 50 keywords.',
        'category': 'Graphic Resources',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'releases': ['release1.pdf', 'release2.pdf']
    }
    ast = AdobeStock(**kwargs)
    sst = ast.to_shutter_stock()
    from stocker.models import ShutterStock
    assert isinstance(sst, ShutterStock)


def test_to_shutter_stock_data_integrity():
    """Testing conversion to ShutterStock format, data integrity
    """
    from stocker.models import AdobeStock

    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'title': 'Up to 200 characters,Most important keywords first. '
                 'Max 50 keywords.',
        'category': 'Graphic Resources',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'releases': ['release1.pdf', 'release2.pdf']
    }
    ast = AdobeStock(**kwargs)
    sst = ast.to_shutter_stock()
    from stocker.models import ShutterStock
    assert isinstance(sst, ShutterStock)

    assert sst.filename == ast.filename
    assert sst.title == ast.title
    assert sst.category1 == 'Abstract'
    assert sst.category2 == ''
    assert sst.editorial is False
    assert sst.keywords == ast.keywords
