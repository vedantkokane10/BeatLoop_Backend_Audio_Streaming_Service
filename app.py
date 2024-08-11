# from flask import Flask, request, jsonify, send_file, redirect, make_response, render_template_string
# import requests
# import yt_dlp as youtube_dl
# import io
# import urllib.parse

# app = Flask(__name__)

# @app.route('/')
# def greey():
#     return "hello"

# @app.route('/stream_audio/<video_id>')
# def stream_audio(video_id):
#     video_id = urllib.parse.unquote(video_id)
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'quiet': True,
#         'noplaylist': True
#     }

#     try:
#         audio_url = ""
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             video_info = ydl.extract_info(video_id, download=False)
#             audio_url = video_info['url']
#             print(audio_url)
#             return jsonify({"url":audio_url})
        
        
#     except Exception as e:
#         return jsonify({'error': 'Failed to stream audio', 'details': str(e)}), 500


# if __name__ == '__main__':
#     app.run(port=7000, debug=True)
from flask import Flask, request, jsonify
import yt_dlp as youtube_dl
import urllib.parse

app = Flask(__name__)

@app.route('/')
def greet():
    return "Hello"

@app.route('/stream_audio/<video_id>')
def stream_audio(video_id):
    video_id = urllib.parse.unquote(video_id)

    # Use the video ID directly to get the audio stream URL
    ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True,
            'geo_bypass': True,
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
    }


    try:
        audio_url = ""
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(video_id, download=False)
            audio_url = video_info.get('url', '')
            if not audio_url:
                return jsonify({'error': 'Failed to get audio URL'}), 500
            print(audio_url)
            return jsonify({"url": audio_url})
        
    except Exception as e:
        return jsonify({'error': 'Failed to stream audio', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
