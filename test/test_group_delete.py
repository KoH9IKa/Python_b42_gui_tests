from random import randrange
import time
from datetime import datetime

name_raw = datetime.now()


def test_delete_group(app):
    if len(app.groups.get_groups_list()) == 1:  # если там 1 группа, то нам не даст её удалить, надо минимум 2
        group_name = ("group " + str(name_raw)[:-7])
        app.groups.add_new_group(group_name)
    old_list = app.groups.get_groups_list()
    index = randrange(len(old_list))
    group = old_list[index]
    app.groups.select_group_by_index(index)
    app.groups.delete_group()
    old_list.remove(group)
    new_list = app.groups.get_groups_list()
    assert sorted(new_list) == sorted(old_list)
    print("\n", new_list, "\n", old_list)
