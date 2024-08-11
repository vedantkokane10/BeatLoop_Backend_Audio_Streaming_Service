from flask import Flask, request, jsonify, send_file, redirect, make_response, render_template_string
import requests
import yt_dlp as youtube_dl
import io
import urllib.parse

app = Flask(__name__)
@app.route('/stream_audio/<video_id>')
def stream_audio(video_id):
    video_id = urllib.parse.unquote(video_id)
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True
    }

    try:
        audio_url = ""
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(video_id, download=False)
            audio_url = video_info['url']
            print(audio_url)
            return jsonify({"url":audio_url})
        
        
    except Exception as e:
        return jsonify({'error': 'Failed to stream audio', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run(port=7000, debug=True)
