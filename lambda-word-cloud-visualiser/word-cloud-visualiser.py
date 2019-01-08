from wordcloud import WordCloud
import matplotlib.pyplot as plt

import base64
import json

def visualise(event, context):
    #return event
    #body_data = base64.b64decode(event['request']['data']['body'])
    #decoded_body = json.loads(body_data)['counts']

    decoded_body = event['counts']
    frequencies = {d['keyWord']: d['count'] for d in decoded_body}

    wordcloud = WordCloud(background_color='white', max_font_size=40, margin=0).generate_from_frequencies(frequencies)
    figure = plt.figure()
    frame = plt.gca()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")

    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)

    from io import BytesIO
    figfile = BytesIO()
    figure.savefig(figfile, format='png', bbox_inches='tight', pad_inches=0)
    figfile.seek(0)

    data = base64.b64encode(figfile.getvalue()).decode('utf-8')

    response = {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/png"
        },
        "body": data
    }

    #return response

    return {
        "contentType": "image/png",
        "data": data
    }
