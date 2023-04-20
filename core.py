import vk_api
from config import acces_token
from vk_api.exceptions import ApiError

class VkTools():
    def __init__(self, token):
        self.ext_api = vk_api.VkApi(token=token)


    def get_profile_info(self, user_id):
        try:
            info = self.ext_api.method('users.get',
                                                        {'user_id': user_id,
                                                         'fields': 'bdate, city, sex, relation'
                                                         }
                                                         )
        except ApiError:
            return

        return info



if __name__ == '__main__':
     tools = VkTools(acces_token)
     print(tools.get_profile_info(203056408))
