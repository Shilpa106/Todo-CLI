import commands.lists
import commands.todos


# map command name to the command function
commands_dict={

    'show':lists.show_lists,
    'use':lists.use_list,
    'create':lists.create_list,
    'all':todos.show_items,
    'add':todos.add_item,

    # 'edit': todos.edit_item,
    # 'remove': todos.remove_item,
    # 'complete': todos.complete_item,
    # 'incomplete': todos.incomplete_item
}