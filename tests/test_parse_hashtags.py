import sys
sys.path.append('../script')
import common

def test_parse_hashtags_with_null():
    json_hashtags = []
    assert common.parse_hashtags(json_hashtags) == None

def test_parse_hashtags_with_english():
    json_hashtags = [{"text": "python"}, {"text": "ruby"}]
    assert common.parse_hashtags(json_hashtags) == ["#python", "#ruby"]

def test_parse_hashtags_with_japanese():
    json_hashtags = [{"text": "日本"}, {"text": "中国"}]
    assert common.parse_hashtags(json_hashtags) == ["#日本", "#中国"]

def test_parse_hashtags_with_null_text():
    json_hashtags = [{"text": "日本"}, {"text": ""}]
    assert common.parse_hashtags(json_hashtags) == ["#日本", "#"]
