def generate_diff(data1, data2):
    keys_data1 = set(data1.keys())
    keys_data2 = set(data2.keys())

    new_keys = keys_data2 - keys_data1
    removed_keys = keys_data1 - keys_data2
    common_keys = keys_data1 & keys_data2
    all_keys = sorted(new_keys | removed_keys | common_keys)

    diff_result = {}
    diff_result['added'] = {}
    diff_result['removed'] = {}
    diff_result['updated'] = {'old_value': {}, 'new_value': {}}
    diff_result['nested'] = {}
    diff_result['same'] = {}
    diff_result['all_keys'] = all_keys

    for key in all_keys:
        if key in new_keys:
            diff_result['added'].update({key: data2.get(key)})

        elif key in removed_keys:
            diff_result['removed'].update({key: data1.get(key)})

        elif key in common_keys:
            if type(data1[key]) == dict and type(data2[key]) == dict:
                diff_result['nested'].update({key: generate_diff(data1[key], data2[key])})

            elif data1[key] == data2[key]:
                diff_result['same'].update({key: data1.get(key)})

            else:
                diff_result['updated']['old_value'].update({key: data1.get(key)})
                diff_result['updated']['new_value'].update({key: data2.get(key)})

    return diff_result
