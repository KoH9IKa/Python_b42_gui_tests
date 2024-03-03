# import generator.groups  # раскомментировать что бы запустить генератор перед тестами


def test_add_group(app, xlsx_data):
    # print(xlsx_data[0])
    group_name = xlsx_data[0]
    old_list = app.groups.get_groups_list()
    app.groups.add_new_group(group_name)
    new_list = app.groups.get_groups_list()
    old_list.append(group_name)
    assert sorted(new_list) == sorted(old_list)


