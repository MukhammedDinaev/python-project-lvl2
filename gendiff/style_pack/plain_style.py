def is_in_group(group, value):
    return value in group


def get_value(value):
    if type(value) == str:
        return '\'{}\''.format(value)
    elif value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif not type(value) == dict:
        return value
    return '[complex value]'


def make_plain_stile(diff_data, path='', result=None):
    if result is None:
        result = []
    all_keys = diff_data['all_keys']
    if all_keys:
        for key in all_keys:
            if is_in_group(diff_data['added'], key):
                path1 = path + key
                value = get_value(diff_data['added'][key])
                result.append('Property \'{}\' was added with value: {}'.format(path1, value))
            elif is_in_group(diff_data['removed'], key):
                path1 = path + key
                result.append('Property \'{}\' was removed'.format(path1))
            elif is_in_group(diff_data['updated']['old_value'], key):
                path1 = path + key
                old_value = get_value(diff_data['updated']['old_value'][key])
                new_value = get_value(diff_data['updated']['new_value'][key])
                result.append('Property \'{}\' was updated. From {} to {}'.format(path1, old_value, new_value))
            elif is_in_group(diff_data['nested'], key):
                make_plain_stile(diff_data['nested'][key], path + key + '.', result)
    return '\n'.join(result)
