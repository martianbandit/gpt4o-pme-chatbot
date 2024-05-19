from supabase import create_client, Client
import config

def init_supabase() -> Client:
    supabase_url = config.SUPABASE_URL
    supabase_key = config.SUPABASE_KEY
    return create_client(supabase_url, supabase_key)

supabase = init_supabase()

