

def test_add_group(app):
    old_list = app.groups.get_groups_list()
    app.groups.add_new_group("my group")
    new_list = app.groups.get_groups_list()
    old_list.append("my group")
    assert sorted(new_list) == sorted(old_list)
