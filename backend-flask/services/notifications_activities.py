from datetime import datetime, timedelta, timezone # import this data as we need to mock the data
class NotificationsActivities:
  def run(): # Sinlge run which is standard for Service objects -> Only having one entry point into out application
    now = datetime.now(timezone.utc).astimezone() # again used for mocking data
    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'handle':  'Kamran Abid',
      'message': 'Apis are fun',
      'created_at': (now - timedelta(days=2)).isoformat(), # 2 days in the past
      'expires_at': (now + timedelta(days=5)).isoformat(), # 5 days in the future // USED FOR MOCKING DATA
      'likes_count': 5,
      'replies_count': 1,
      'reposts_count': 0,
      'replies': [{ 
        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Worf',
        'message': 'This post has no honor!',
        'likes_count': 0,
        'replies_count': 0,
        'reposts_count': 0,
        'created_at': (now - timedelta(days=2)).isoformat()
      }]
    }
    ]
    return results