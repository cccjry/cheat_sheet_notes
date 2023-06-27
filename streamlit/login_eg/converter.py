import streamlit_authenticator as stauth
import yaml

def credential_generator(inputs: dict, yaml_file_name='.secrets', cookie_expiry=1):

    #- Initialize the config file -#
    config = {'credentials': {
        'usernames': {}
        }
    }

    for user in inputs.keys():
        print(f"Generating credentials for {user}")

        new_user = {
            'name': user,
            'email': user + '@gmail.com',
            'password': stauth.Hasher([inputs[user]]).generate()[0]
        }
        config['credentials']['usernames'][user] = new_user

    #- add cookie expiration days, key, and name -#
    cookie_setting = {'expiry_days': cookie_expiry, 'key': 'my_key', 'name': 'my_app'}
    config.update({'cookie': cookie_setting})
    #- add preauthorized users -#
    preauthorized_emails = {'emails': ['test@gmail.com']}
    config.update({'preauthorized': preauthorized_emails})

    #- dump YAML file -#
    with open(f"{yaml_file_name}.yaml","w") as file:
        yaml.dump(config, file, default_flow_style=False)


#- Create a list of dictionaries with usernames and passwords -#
inputs = {
    'admin': 'admin',
    'jerrychen': 'password',
    'new_user': 'new$user',
}

#- Generate the credentials file -#
credential_generator(inputs)