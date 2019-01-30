from gist_search.utils import get_gists

def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return None
    
    users_gists = get_gists(username)
    results = []
    
    for gist in users_gists:
        if description and description not in gist['description']:
            continue
    
        if file_name:
            matched = False
            
            for fname in gist['files']:
                if file_name.lower() in fname.lower():
                    matched = True
                    break
            
            if not matched:
                continue
                
#         if id and id not in gist['id']:
#             continue            
                
        results.append(gist)
    return results
        
        
    
#     if description and file_name and id:
#         # Do some code
#         if description.lower() in gist['description'].lower():
#             for fname in gist['files']:
#                 if file_name.lower() in fname.lower():
#                     results.append(gist)
#                     break
#         elif description and file_name:
#             pass
        
#         elif description and id:
#             pass
        
#         elif file_name and id
#             pass
        
#         elif description:
#             pass
        
#         elif file_name:
#             pass
        
#         elif id:
#             pass
    
    
#     for gist in users_gists: 
#         if description:
#             if description.lower() in gist['description'].lower():
#                 results.append(gist)
                
#         if file_name:
#             for fname in gist['files']:
#                 if file_name in fname:
#                     results.append(gist)
#                     break
