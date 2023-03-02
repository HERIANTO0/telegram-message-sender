from telethon import TelegramClient, events
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import asyncio

# replace the values below with your own API ID, API HASH, and BOT TOKEN
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# create a new TelegramClient instance
client = TelegramClient('my_session', api_id, api_hash)

# start the client
client.start(bot_token=bot_token)

# create a list of usernames to send messages to
usernames = ['user1_username', 'user2_username', 'user3_username']

# define the message to send
message = 'Hello! This is a bulk message sent by my Telegram bot.'

# define a coroutine function to send the message to each user
async def send_message(username):
    try:
        # resolve the username to a user ID
        result = await client(ResolveUsernameRequest(username))
        user_id = result.peer.user_id

        # send the message to the user
        await client.send_message(user_id, message)
        print(f'Successfully sent message to {username}')
    except UserPrivacyRestrictedError:
        print(f'Could not send message to {username}: user has privacy restrictions')
    except PeerFloodError:
        print(f'Could not send message to {username}: flooding')
    except Exception as e:
        print(f'Could not send message to {username}: {e}')

# create a list of tasks to send the message to each username
tasks = [send_message(username) for username in usernames]

# run the tasks concurrently
asyncio.gather(*tasks)

# stop the client
client.disconnect()
