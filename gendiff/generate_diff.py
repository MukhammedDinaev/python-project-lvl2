def generate_diff(data1, data2):
    keys_data1 = set(data1.keys())
    keys_data2 = set(data2.keys())

    new_keys = keys_data2 - keys_data1
    removed_keys = keys_data1 - keys_data2
    common_keys = keys_data1 & keys_data2
    all_keys = sorted(new_keys | removed_keys | common_keys)
    diff_result = {}
    for key in all_keys:

        if key in new_keys:
            diff_result['+ ' + key] = data2.get(key)
        elif key in removed_keys:
            diff_result['- ' + key] = data1.get(key)
        else:
            if data1[key] == data2[key]:
                diff_result['  ' + key] = data1.get(key)
            else:
                diff_result['- ' + key] = data1.get(key)
                diff_result['+ ' + key] = data2.get(key)

    return diff_result
