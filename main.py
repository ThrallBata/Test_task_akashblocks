import requests
import base64


API_URL = "https://akash-rpc.polkachu.com/block?height="


def get_transactions_next_block(block_height=12544752):

    decrypted_data_list = []
    next_block_height = block_height + 1

    response = requests.get(f"{API_URL}{str(next_block_height)}")
    json_data = response.json()

    encrypted_data_list = json_data['result']['block']['data']['txs']

    if encrypted_data_list != []:
        for encrypted_data in encrypted_data_list:
            decrypted_data_list.append(base64.b64decode(encrypted_data))

    return decrypted_data_list


print(get_transactions_next_block())


