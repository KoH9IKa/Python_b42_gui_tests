import time


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_groups_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def delete_button(self):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()

    def select_group_by_name(self, name):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        for node in root.children():
            if node.text() == name:
                node.click()

    def select_group_by_index(self, index, t=0.5):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        tree.wait("visible")
        root = tree.tree_root()
        nodes = root.children()
        time.sleep(t)
        nodes[index].click()

    def delete_group_by_index(self, index):
        self.open_group_editor()
        self.select_group_by_index(index)
        self.delete_group()

    def delete_group(self, t=0):
        time.sleep(t)
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        time.sleep(t)
        self.group_deleter = self.app.application.window(title="Delete group")
        self.group_deleter.wait("visible")
        time.sleep(t)
        self.group_deleter.window(auto_id="uxDeleteAllRadioButton").click()
        time.sleep(t)
        self.group_deleter.window(auto_id="uxOKAddressButton").click()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()
