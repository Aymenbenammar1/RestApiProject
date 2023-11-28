from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import os

app = FastAPI()

datasets = {}


@app.get("/datasets/")
def list_datasets():
    return JSONResponse(content=list(datasets.keys()))
    
@app.post("/datasets/")
async def create_dataset(file: UploadFile = File(...)):
    # Save the file to a temporary location
    file_path = f'/tmp/{file.filename}'
    with open(file_path, 'wb') as temp_file:
        temp_file.write(file.file.read())

    # Use pandas to read the CSV file
    df = pd.read_csv(file_path)

    # Clean up the temporary file
    os.remove(file_path)

    dataset_id = len(datasets) + 1
    datasets[dataset_id] = df
    return JSONResponse(content={'id': dataset_id, 'url': f'/datasets/{dataset_id}'})

@app.get("/datasets/{dataset_id}/")
def get_dataset_info(dataset_id: int):
    if dataset_id not in datasets:
        raise HTTPException(status_code=404, detail="Dataset not found")

    df = datasets[dataset_id]
    return JSONResponse(content={'file_name': f'dataset_{dataset_id}.csv', 'size': df.size})

@app.delete("/datasets/{dataset_id}/")
def delete_dataset(dataset_id: int):
    if dataset_id not in datasets:
        raise HTTPException(status_code=404, detail={"error": "Dataset not found"})

    del datasets[dataset_id]
    return {"message": "Dataset deleted successfully"}

@app.get("/datasets/{dataset_id}/stats/")
def get_dataset_stats(dataset_id: int):
    if dataset_id not in datasets:
        raise HTTPException(status_code=404, detail={"error": "Dataset not found"})

    df = datasets[dataset_id]
    return JSONResponse(content=df.describe().to_dict())

@app.get("/datasets/{dataset_id}/plot/")
def generate_plot(dataset_id: int):
    if dataset_id not in datasets:
        raise HTTPException(status_code=404, detail={"error": "Dataset not found"})

    df = datasets[dataset_id]
    # Remplacez File par le type de fichier que vous générez, par exemple, PDF.
    return FileResponse(f"dataset_{dataset_id}_plot.pdf", filename=f"dataset_{dataset_id}_plot.pdf")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)

