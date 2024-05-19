from supabase_client import supabase

def submit_feedback(user_id: str, rating: int, comments: str):
    response = supabase.table('feedback').insert({
        'user_id': user_id,
        'rating': rating,
        'comments': comments
    }).execute()
    return response

def get_feedback():
    response = supabase.table('feedback').select('*').execute()
    return response['data']
