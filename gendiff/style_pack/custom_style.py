def make_custom_style(diff_data):
    all_keys = diff_data['all_keys']
    output = {}
    if len(all_keys) > 0:
        for key in all_keys:
            if key in diff_data['added']:
                output['+ ' + key] = diff_data['added'].get(key)
            elif key in diff_data['removed']:
                output['- ' + key] = diff_data['removed'].get(key)
            elif key in diff_data['updated']['old_value']:
                output['- ' + key] = diff_data['updated']['old_value'].get(key)
                output['+ ' + key] = diff_data['updated']['new_value'].get(key)
            elif key in diff_data['updated']['new_value']:
                output['- ' + key] = diff_data['updated']['old_value'].get(key)
                output['+ ' + key] = diff_data['updated']['new_value'].get(key)
            elif key in diff_data['nested']:
                output[key] = make_custom_style(diff_data['nested'].get(key))
            elif key in diff_data['same']:
                output[key] = diff_data['same'][key]
    return output
