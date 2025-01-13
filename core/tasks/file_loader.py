import os
import logging

import pandas as pd

from rest_framework import status
from rest_framework.response import Response

from core.tasks.api.serializers import TaskSerializer


logger = logging.Logger("File Loader")


def handle_file(file):
    extension = os.path.basename(file.name).split(".")[-1]

    if not valid_file_type(extension):
        logger.error(f"Invalid file extension: {extension}")
        return Response(
            {
                "message": "Invalid file extension.",
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    df = load_file(file, extension)

    return valid_and_load_file(df)

def valid_file_type(extension):           
    if extension not in ["csv", "xlsx"]:
        return False
    return True

def load_file(file, extension):
    if extension == "csv":
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    
    return df

def valid_and_load_file(df):
    if all(col in df.columns for col in ["name", "status", "created_by"]):
        bulk_tasks = [{"name": item.name, "status": item.status, "created_by": item.created_by} for item in df.itertuples()]
        
        serializer = TaskSerializer(data=bulk_tasks, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        
        return Response(
            {
                "message": "File was uploaded with success.",
            },
            status=status.HTTP_201_CREATED
        )
    
    logger.error("The file must have the following columns: name, status, created_by")
    return Response(
        {
            "message": "The file must have the following columns: name, status, created_by",
        },
        status=status.HTTP_201_CREATED
    )