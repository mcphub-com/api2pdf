markdown
# Api2Pdf MCP Server

Welcome to the Api2Pdf MCP server, a robust solution designed for seamless PDF generation and manipulation. This service offers a plethora of functionalities that cater to your PDF needs without imposing any rate limits or file size constraints.

## Overview

Api2Pdf is a comprehensive PDF generation service that runs on AWS Lambda, ensuring reliability and cost-effectiveness. It supports multiple tools and technologies to convert HTML, URLs, images, and office documents into PDFs, as well as merging multiple PDFs into one. The service includes advanced formatting options, especially when using wkhtmltopdf and Headless Chrome.

## Features

- **PDF Generation**: Create PDFs from various sources including raw HTML, URLs, images, and office documents.
- **No Rate Limits**: Enjoy unlimited requests without worrying about usage limits.
- **No File Size Constraints**: Convert files of any size with ease.
- **High Reliability**: Built on AWS Lambda, ensuring high availability and performance.
- **Cost-effective**: Offers a freemium model with competitive pricing for advanced plans.

## Tool List and Functions

Api2Pdf offers a range of tools, each with specific functions to cater to different PDF conversion needs:

1. **wkhtmltopdf**
   - Convert raw HTML to PDF
   - Convert URL to PDF

2. **Headless Chrome**
   - Convert URL to PDF
   - Convert raw HTML to PDF

3. **LibreOffice**
   - Convert office documents, images, or other file types to PDF

4. **Merge**
   - Combine multiple PDFs into a single PDF

## Tool Declarations

- **wkhtmltopdf_html**: Convert raw HTML to PDF.
- **wkhtmltopdf_url**: Convert URL to PDF.
- **chrome_url**: Convert URL to PDF.
- **chrome_html**: Convert raw HTML to PDF.
- **libreoffice_convert**: Convert office documents, images, or other file types to PDF.
- **merge**: Combine multiple PDFs into a single PDF.

## Usage

The Api2Pdf MCP server is designed for developers and businesses who need a reliable and scalable solution for PDF creation and management. With Api2Pdf, you can experiment with different endpoints to see the results firsthand, making it a versatile tool for a wide range of applications.

For more details on how to utilize these tools, explore the various functions and their descriptions above. Whether you are converting a simple HTML page or merging multiple PDFs, Api2Pdf provides the functionality you need with ease and efficiency.

---

Thank you for choosing Api2Pdf MCP server for your PDF generation needs. We are confident that our service will meet your expectations and provide a seamless experience.