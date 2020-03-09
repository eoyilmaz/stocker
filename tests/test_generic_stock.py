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
    from stocker.models import GenericStock
    gst = GenericStock()
    assert isinstance(gst, GenericStock)


def test_init_with_arguments():
    """testing initialization with keyword arguments
    """
    from stocker.models import GenericStock
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
        'country': 'Turkey',
        'editorial': False,
        'releases': ['release1.pdf', 'release2.pdf'],
        'poster_timecode': '00:00:00'
    }

    gst = GenericStock(**kwargs)
    assert gst.filename == kwargs['filename']
    assert gst.title == kwargs['title']
    assert gst.category1 == kwargs['category1']
    assert gst.category2 == kwargs['category2']
    assert gst.keywords == kwargs['keywords']
    assert gst.editorial == kwargs['editorial']
    assert gst.releases == kwargs['releases']
    assert gst.poster_timecode == kwargs['poster_timecode']
    assert gst.country == kwargs['country']


def test_init_title_with_description_attribute():
    """testing initialization the title attribute with the description if it is
    skipped
    """
    from stocker.models import GenericStock
    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'description': 'Up to 200 characters,Most important keywords first. '
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
        'country': 'Turkey',
        'editorial': False,
        'releases': ['release1.pdf', 'release2.pdf'],
        'poster_timecode': '00:00:00'
    }

    gst = GenericStock(**kwargs)
    assert gst.filename == kwargs['filename']
    assert gst.title == kwargs['description']
    assert gst.description == kwargs['description']
    assert gst.category1 == kwargs['category1']
    assert gst.category2 == kwargs['category2']
    assert gst.keywords == kwargs['keywords']
    assert gst.editorial == kwargs['editorial']
    assert gst.releases == kwargs['releases']
    assert gst.poster_timecode == kwargs['poster_timecode']
    assert gst.country == kwargs['country']


def test_from_method():
    """testing if the from_() method is working properly
    """
    raise NotImplementedError("Test is not implemented yet")


def test_to_method():
    """testing if the to() method is working properly
    """
    raise NotImplementedError("Test is not implemented yet")


def test_from_shutter_stock_method():
    """testing if the from_shutter_stock() method is working properly
    """
    raise NotImplementedError("Test is not implemented yet")


def test_to_shutter_stock_method():
    """testing if the to_shutter_stock() method is working properly
    """
    raise NotImplementedError("Test is not implemented yet")


def test_from_abobe_stock_method():
    """testing if the from_adobe_stock() method is working properly
    """
    raise NotImplementedError("Test is not implemented yet")


def test_to_abobe_stock_method():
    """testing if the to_adobe_stock() method is working properly
    """
    raise NotImplementedError("Test is not implemented yet")


def test_from_getty_images_method():
    """testing if the from_getty_images() method is working properly
    """
    raise NotImplementedError("Test is not implemented yet")


def test_to_getty_images_method():
    """testing if the from_to_images() method is working properly
    """
    raise NotImplementedError("Test is not implemented yet")


def test_from_file_method():
    """testing if the from_file method is working properly
    """
    import os
    here = os.path.abspath(os.path.dirname(__file__))

    test_data_path = os.path.join(here, 'test_data', 'some_video_1.json')

    from stocker.models import GenericStock
    gst = GenericStock()

    gst.from_file(test_data_path)

    assert gst.title == "Test video 1"
    assert gst.description == "This is a test video, created just for test!"
    assert gst.category1 == "Transportation"
    assert gst.category2 == "Holidays"
    assert gst.keywords == ["keyword 1", "keyword 2", "keyword 3"]
    assert gst.filename == "some_video_1.mp4"
    assert gst.path == os.path.join(here, 'test_data')
