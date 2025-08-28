from flask import Flask, request, jsonify
from twikit import Client
import asyncio

app = Flask(__name__)

# Initialize twikit client (replace with your credentials)
client = Client('en-US')

# Log in to Twitter/X (use your credentials or environment variables for security)
async def login():
    await client.login(
        username='YOUR_USERNAME',
        email='YOUR_EMAIL',
        password='YOUR_PASSWORD'
    )

# Run the login on startup
asyncio.run(login())

@app.route('/tweet', methods=['POST'])
async def post_tweet():
    try:
        data = request.get_json()
        tweet_text = data.get('text')
        if not tweet_text:
            return jsonify({'error': 'No text provided'}), 400

        # Post a tweet using twikit
        tweet = await client.create_tweet(tweet_text)
        return jsonify({'success': True, 'tweet_id': tweet.id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)