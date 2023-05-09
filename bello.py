import supabase
import openai


def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']



openai.api_key = ""

client = supabase.create_client("", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvZHN6dW10bHZvZ3VkdnF3ZWd1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODM1NjE4MjAsImV4cCI6MTk5OTEzNzgyMH0.b_KBO_Jnd7SVST2DFfjY-5yDMYZlsmkGLyntNryHjds")

table_name = "live_information"

data = [

    {"attribute": "id_volo", "value": "FR6592", "embedding": get_embedding("id_volo")},
    {"attribute": "ritardo", "value": "60", "embedding": get_embedding("ritardo")},
    {"attribute": "terminal", "value": "1", "embedding": get_embedding("terminal")},
]

result = client.table(table_name).insert(data).execute()

query_vector = get_embedding("numero volo")

query = "SELECT * FROM live_information"

client.supabase_url = "https://kodszumtlvogudvqwegu.supabase.co"
client.supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvZHN6dW10bHZvZ3VkdnF3ZWd1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODM1NjE4MjAsImV4cCI6MTk5OTEzNzgyMH0.b_KBO_Jnd7SVST2DFfjY-5yDMYZlsmkGLyntNryHjds"


results = client.from_(table_name).select(query)
print(results.json)
