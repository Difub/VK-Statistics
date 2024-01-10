#token 51791387
import json
import requests


def GroupStats(group_id=223409448, days = 1):
        """
        Получение общей статистики о группе
        group_id = int NOT null #id отслеживаемой группы
        days = int #кол-во дней
        """
        # переменные 
        TOKEN = 'vk1.a.ffz8V74U97TFrCaEpawBueGdAHENUIcBXE3c_u0sP3AsOqOX2SOmZuG7uJ7feAzD65B1GJYi89YZ3HjDxA_xe2Khknvdsg2nofghcZ_Xa8JfXiGm5JMcD4-mVRz3AO4AqpzFExzU4uN1oKFdVMVjvrxxzqxrU7ttYJIxTpVjt7EDEa-j0OZuuoEPQg1oVF2pNgPY3-Pq_2jgQhDoxUfVfQ'
        VERSION = 5.199 #версия апи

        # через api vk вызываем статистику группы за последние DAYS дня
        response = requests.get('https://api.vk.com/method/stats.get',
        params={'access_token': TOKEN,
                'v': VERSION,
                'group_id': group_id,
                'intervals_count': days,
                })
        data = response.json()
        if 'response' in data:
                return data['response']
        else:
                return "err"



def miniParserGroupStats(days=2):
        t = ['activity', 'reach', 'visitors']
        activity = {'likes':0 , 'subscribed':0, 'comments':0 , 'copies':0, 'hidden':0, 'unsubscribed':0}
        print(GroupStats(days)[0])
        for i in GroupStats(days):
                if 'activity' in i:
                        activity['likes'] = i['activity']['likes']
                        activity['subscribed'] = i['activity']['subscribed']


print(miniParserGroupStats())


#def getGroupPostStats():
#        """ Работает если у группы более 5000 подписчиков
#        нужен иной метод"""
#        # переменные 
#        TOKEN = 'vk1.a.pcU0nhQM46KfPGCYKIT9XE0sm09j_CMqRjet93cZ5gv5J_iNF6ywTeWsWJX1KwE4wMx7brLOpwl8-a5YShfMfdAtyU5Ny4wPQiO3rew3xjZYtb4s4KIPdi6q2RM4vF-SHAb8wBzX6qACQVqmWWXoPE8B-KUd0PaiUdcFH7XMNOyyq9DdOq-r0M5qUqLmKHvgQasqkXXb9WhL2vS9RGMJ9A'
#        VERSION = 5.199 #версия апи
#        owner_id = 'difub' #id владельца записи
#        post_ids = '342428651_26' #id записи
#
#        # через api vk вызываем статистику группы за последние DAYS дня
#        response = requests.get('https://api.vk.com/method/stats.getPostReach',
#        params={'access_token': TOKEN,
#                'v': VERSION,
#                'owner_id': owner_id,
#                'post_ids': post_ids,
#                })
#        return response.json()