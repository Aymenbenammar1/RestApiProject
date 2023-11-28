# Datapane API Server and CLI

This project includes a simple Python 3-based REST API server and corresponding command-line client for Datapane, an API-driven product that handles and processes datasets.

## Getting Started

Follow these instructions to set up and run the Datapane API server and CLI on your local machine.

### Prerequisites

- Python 3.8 or higher

### Installing


1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Server

1. Run the server:

    ```bash
    uvicorn server:app --reload

    ```

   The server will be accessible at [http://localhost:5000](http://localhost:5000).

### Running the Client

Use the command-line client to interact with the server. Here are some examples:

- List datasets:

    ```bash
    python client.py list
    ```

- Create a dataset from a CSV file:

    ```bash
    python client.py create path/to/your/file.csv
    ```

- Get information about a dataset:

    ```bash
    python client.py info 1
    ```

- Export a dataset to Excel:

    ```bash
    python client.py excel 1
    ```

- Delete a dataset:

    ```bash
    python client.py delete 1
    ```

- Get statistics for a dataset:

    ```bash
    python client.py stats 1
    ```

- Generate a plot for a dataset:

    ```bash
    python client.py plot 1
    ```

