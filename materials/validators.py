from rest_framework import serializers


def wrong_links_validator(text):
    words = text.split(' ')
    example_links = ['.com', '.ru', '.org']
    right_link = 'youtube.com'
    having_wrong_links = []
    for word in words:
        for example_link in example_links:
            if example_link in word:
                if right_link in word:
                    continue
                else:
                    having_wrong_links.append(word)
    if len(having_wrong_links) > 0:
        raise serializers.ValidationError("You should delete wrong links")
