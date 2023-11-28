import argparse
import requests


# Base URL for the API
BASE_URL = 'http://localhost:5000'




def list_datasets():
    response = requests.get(f'{BASE_URL}/datasets/')
    print(response.json())

def create_dataset(file_path):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(f'{BASE_URL}/datasets/', files=files)
        print(response.json())

def get_dataset_info(dataset_id):
    response = requests.get(f'{BASE_URL}/datasets/{dataset_id}/')
    print(response.json())


def export_to_excel(dataset_id: int):
    response = requests.get(f'{BASE_URL}/datasets/{dataset_id}/excel/')
    with open(f'dataset_{dataset_id}.xlsx', 'wb') as file:
        file.write(response.content)
    print(f'Dataset exported to dataset_{dataset_id}.xlsx')


def delete_dataset(dataset_id: int):
    response = requests.delete(f'{BASE_URL}/datasets/{dataset_id}/')
    print(response.json())


def get_dataset_stats(dataset_id: int):
    response = requests.get(f'{BASE_URL}/datasets/{dataset_id}/stats/')
    print(response.json())



def generate_plot(dataset_id):
    response = requests.get(f'{BASE_URL}/datasets/{dataset_id}/plot/')
    with open(f'dataset_{dataset_id}_plot.pdf', 'wb') as file:
        file.write(response.content)
    print(f'Plot generated and saved to dataset_{dataset_id}_plot.pdf')





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Datapane CLI')
    parser.add_argument('action', choices=['list', 'create', 'info', 'excel', 'delete', 'stats', 'plot'])

    args = parser.parse_args()

    if args.action == 'list':
        list_datasets()
    elif args.action == 'create':
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        create_dataset(args.file_path)
    elif args.action == 'info':
        parser.add_argument('dataset_id', type=int, help='ID of the dataset')
        get_dataset_info(args.dataset_id)
    elif args.action == 'excel':
        parser.add_argument('dataset_id', type=int, help='ID of the dataset')
        export_to_excel(args.dataset_id)
    elif args.action == 'delete':
        parser.add_argument('dataset_id', type=int, help='ID of the dataset')
        delete_dataset(args.dataset_id)
    elif args.action == 'stats':
        parser.add_argument('dataset_id', type=int, help='ID of the dataset')
        get_dataset_stats(args.dataset_id)
    elif args.action == 'plot':
        parser.add_argument('dataset_id', type=int, help='ID of the dataset')
        generate_plot(args.dataset_id)