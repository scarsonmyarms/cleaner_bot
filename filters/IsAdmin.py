# Из библиотеки typing мы импортировали List, чтобы корректно указать, что мы можем передавать либо список, либо одиночный идентификатор администратора.
from typing import List
# Из библиотеки aiogram мы импортировали BaseFilter и Message, необходимые для создания пользовательского фильтра и работы с сообщениями
from aiogram.filters import BaseFilter
from aiogram.types import Message

# Фильтр, который мы создали, называется IsAdmin. Этот фильтр предназначен для проверки, является ли пользователь, отправивший сообщение, администратором
class IsAdmin(BaseFilter):
    #Конструктор init инициализирует объект класса IsAdmin и принимает один параметр user_ids. Этот параметр может быть либо целым числом (если у нас только один администратор), либо списком целых чисел (если у нас несколько администраторов). Мы сохраняем этот параметр в атрибуте self.user_ids
    def __init__(self, user_ids: int | List[int]) -> None:
        self.user_ids = user_ids
# Асинхронный метод call
# Метод call является обязательным для классов пользовательских фильтров. Этот метод вызывается каждый раз, когда необходимо применить фильтр к сообщению
    async def __call__(self, message: Message) -> bool:
        if isinstance(self.user_ids, int):
            # Если self.user_ids является целым числом (int), значит у нас один администратор. В этом случае мы просто проверяем, совпадает ли идентификатор пользователя, отправившего сообщение (message.from_user.id), с self.user_ids
            return message.from_user.id == self.user_ids
        # Если self.user_ids является списком (List[int]), значит у нас несколько администраторов. В этом случае мы проверяем, содержится ли идентификатор пользователя в этом списке
        return message.from_user.id in self.user_ids
# Стоит отметить, что, будь то пользовательские фильтры или магические фильтры, их конечная цель всегда заключается в получении булевого значения True или False. Иными словами, написание класса фильтров или конструкции магического фильтра сводится к проверке условия: если условие истинно, действие выполняется; если нет — действие не выполняется