import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.VideoUrlException import VideoUrlException


@pytest.mark.parametrize('service, value', [
    [('vimeo',), 'https://player.vimeo.com/video/71787467'],
    [('vimeo',), 'https://vimeo.com/71787467'],
    [('youtube',), 'https://www.youtube.com/embed/netHLn9TScY'],
    [('youtube',), 'https://www.youtube.com/watch?v=netHLn9TScY'],
    [('youtube',), 'https://youtu.be/netHLn9TScY'],
    [tuple(), 'https://player.vimeo.com/video/71787467'],
    [tuple(), 'https://vimeo.com/71787467'],
    [tuple(), 'https://www.youtube.com/embed/netHLn9TScY'],
    [tuple(), 'https://www.youtube.com/watch?v=netHLn9TScY'],
    [tuple(), 'https://youtu.be/netHLn9TScY'],
    [('twitch',), 'https://www.twitch.tv/videos/320689092'],
    [('twitch',), 'https://clips.twitch.tv/BitterLazyMangetoutHumbleLife'],
])
def test_success_videoUrl(service, value):
    if service:
        assert v.videoUrl(*service).validate(value)
        assert v.videoUrl(*service).check(value) is None
        assert v.videoUrl(*service).claim(value) is None
    else:
        assert v.videoUrl().validate(value)
        assert v.videoUrl().check(value) is None
        assert v.videoUrl().claim(value) is None


@pytest.mark.parametrize('service, value', [
    [('vimeo',), 'https://www.youtube.com/watch?v=netHLn9TScY'],
    [('youtube',), 'https://vimeo.com/71787467'],
    [tuple(), 'example.com'],
    [tuple(), 'ftp://youtu.be/netHLn9TScY'],
    [tuple(), 'https:/example.com/'],
    [tuple(), 'https:/youtube.com/'],
    [tuple(), 'https://vimeo'],
    [tuple(), 'https://vimeo.com71787467'],
    [tuple(), 'https://www.google.com'],
    [tuple(), 'tel:+1-816-555-1212'],
    [tuple(), 'text'],
    [tuple(), 'https://twitch.tv/'],
    [tuple(), 'https://www.twitch.tv/yabbadabbado'],
    [tuple(), 'https://clips.twitch.tv/videos/90210'],
    [tuple(), 'https://clips.twitch.tv/90210'],
    [tuple(), 'https://clips.twitch.tv/'],
])
def test_fail_videoUrl(service, value):
    if service:
        assert v.videoUrl(*service).validate(value) is False

        with pytest.raises(VideoUrlException, match=r' must be a valid.*video URL'):
            assert v.videoUrl(*service).check(value)
            assert v.videoUrl(*service).claim(value)
    else:
        assert v.videoUrl().validate(value) is False

        with pytest.raises(VideoUrlException, match=r' must be a valid.*video URL'):
            assert v.videoUrl().check(value)
            assert v.videoUrl().claim(value)


@pytest.mark.parametrize('service, value', [
    [1, 'https://clips.twitch.tv/90210'],
    ['abc', 'https://clips.twitch.tv/'],
])
def test_fail_videoUrl2(service, value):

    with pytest.raises(ComponentException, match=r' is not a recognized video service'):
        assert v.videoUrl(service).validate(value)
        assert v.videoUrl(service).check(value)
        assert v.videoUrl(service).claim(value)
