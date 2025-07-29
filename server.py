import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/api2pdf/api/api2pdf'

mcp = FastMCP('api2pdf')

@mcp.tool()
def wkhtmltopdf_html(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Convert raw HTML to PDF'''
    url = 'https://api2pdf-api2pdf-v1.p.rapidapi.com/wkhtmltopdf/html'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'api2pdf-api2pdf-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def wkhtmltopdf_url(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Convert URL to PDF'''
    url = 'https://api2pdf-api2pdf-v1.p.rapidapi.com/wkhtmltopdf/url'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'api2pdf-api2pdf-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def chrome_url(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Convert URL to PDF'''
    url = 'https://api2pdf-api2pdf-v1.p.rapidapi.com/chrome/url'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'api2pdf-api2pdf-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def chrome_html(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Convert raw HTML to PDF'''
    url = 'https://api2pdf-api2pdf-v1.p.rapidapi.com/chrome/html'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'api2pdf-api2pdf-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def libreoffice_convert(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Convert office doc, image, or other type of file to PDF'''
    url = 'https://api2pdf-api2pdf-v1.p.rapidapi.com/libreoffice/convert'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'api2pdf-api2pdf-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def merge(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Combine multiple PDFs into a single PDF'''
    url = 'https://api2pdf-api2pdf-v1.p.rapidapi.com/merge'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'api2pdf-api2pdf-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
