from supabase_client import supabase

def register_user(email: str, password: str, is_admin: bool = False):
    response = supabase.auth.sign_up({
        'email': email,
        'password': password,
    })
    if response.get('user'):
        user_id = response['user']['id']
        supabase.table('users').update({'is_admin': is_admin}).eq('id', user_id).execute()
    return response

def login_user(email: str, password: str):
    response = supabase.auth.sign_in({
        'email': email,
        'password': password,
    })
    if response.get('user'):
        user = supabase.table('users').select('*').eq('id', response['user']['id']).execute()
        if user:
            response['user']['is_admin'] = user['data'][0]['is_admin']
    return response

