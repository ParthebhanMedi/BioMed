

---

#  Biomedical Named Entity Recognition and Normalization Tool BERN2 API
### Retrieve JSON
To fetch JSON data, use the BERN2 API:  - 
**An Advanced Neural Biomedical Named Entity Recognition and Normalization Tool**

[![Streamlit A](https://img.shields.io/badge/Named_Entity_Recognition_-_BERN2_API-ff69b4.svg?style=for-the-badge&logo=Streamlit)](http://bern2.korea.ac.kr/)

Send a POST request to http://bern2.korea.ac.kr/
Include your text data to annotate in the request body (plain text).
BERN2 returns JSON annotations, which you can paste into this app.

Example Response:
{
    "annotations": [
        {"mention": "protein1", "obj": "protein"},
        {"mention": "disease1", "obj": "disease"},
        {"mention": "gene1", "obj": "gene"}
    ]
}

---

Below is a screenshot that showcases the response from the BERN2 API:  

<img src="https://github.com/ParthebhanMedi/BioMed/blob/main/Screenshot%202025-01-26%20at%2009-01-59%20BERN2.png?raw=true" alt="Screenshot" width="400">

---


# JSON Annotations Viewer  
## This Streamlit app allows you to extract and filter unique mentions from a JSON file containing annotation data.  
You can filter mentions by object type and download the results as a CSV file.  

## 🌐 Try the App
Access the app directly using the link below:


[![Streamlit A](https://img.shields.io/badge/JSON_Annotations_Viewer_-_Streamlit_App-ff69b4.svg?style=for-the-badge&logo=Streamlit)](https://jsonfilter.streamlit.app/)


### Features  
- Parse JSON data containing `annotations`.  
- Extract all unique **mentions** and **object types**.  
- Sidebar filter option to view mentions by specific object types.  
- Download filtered mentions as a CSV file.  

---

## Author  
**Parthebhan Pari**

---  
