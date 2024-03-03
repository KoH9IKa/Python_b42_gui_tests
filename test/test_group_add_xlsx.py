import generator.groups

def prepare_new_data():
    generator.groups.new_data_for_test()


def test_add_group(app, xlsx_data):
    print(xlsx_data)
    # # generator.groups.new_data_for_test()
    # old_list = app.groups.get_groups_list()
    # app.groups.add_new_group(xlsx_data[0])
    # new_list = app.groups.get_groups_list()
    # old_list.append(xlsx_data[0])
    # assert sorted(new_list) == sorted(old_list)


if __name__ == '__main__':
    prepare_new_data()

