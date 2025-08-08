# New service file added to simulate outdated state
import time
from typing import List, Dict, Any

class DataService:
    def __init__(self):
        self.cache = {}
    
    def process_data(self, data: List[Any]) -> List[Any]:
        # Process data with caching
        cache_key = str(data)
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = [item * 2 for item in data]
        self.cache[cache_key] = result
        return result
    
    def clear_cache(self):
        # Clear the cache
        self.cache.clear()

class NotificationService:
    def __init__(self):
        self.notifications = []
    
    def send_notification(self, message: str, user_id: str):
        # Send a notification
        notification = {
            'message': message,
            'user_id': user_id,
            'timestamp': time.time(),
            'status': 'sent'
        }
        self.notifications.append(notification)
        return notification
    
    def get_notifications(self, user_id: str) -> List[Dict[str, Any]]:
        # Get notifications for a user
        return [n for n in self.notifications if n['user_id'] == user_id]
