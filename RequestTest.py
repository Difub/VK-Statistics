#token 51791387

import posts
import json
import requests

# переменные 
TOKEN_USER = 'vk1.a.pcU0nhQM46KfPGCYKIT9XE0sm09j_CMqRjet93cZ5gv5J_iNF6ywTeWsWJX1KwE4wMx7brLOpwl8-a5YShfMfdAtyU5Ny4wPQiO3rew3xjZYtb4s4KIPdi6q2RM4vF-SHAb8wBzX6qACQVqmWWXoPE8B-KUd0PaiUdcFH7XMNOyyq9DdOq-r0M5qUqLmKHvgQasqkXXb9WhL2vS9RGMJ9A'
VERSION = 5.199
DOMAIN = 223409448

# через api vk вызываем статистику группы за последние 31 день
response = requests.get('https://api.vk.com/method/stats.get',
params={'access_token': TOKEN_USER,
        'v': VERSION,
        'group_id': DOMAIN,
        'intervals_count': 7,
        })

data = response.json()

print (data)