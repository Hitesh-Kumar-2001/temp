import pickle

def get_keys():
    """import api keys"""
    keys = open("Scripts/key.txt", "r").read().splitlines()
    return keys
def get_folder_ids():
    ids = open("folders.txt", "r").read().splitlines()
    return ids

    # def gel_all_ids():
    #     ids = data_retriever.get_folder_ids()
    #     file_ids = []
    #     for id in ids:
    #         file_ids.append(get_ids(id))
    #
    #     return ids
#
#auth verification
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")

