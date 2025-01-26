---
#  Biomedical Named Entity Recognition and Normalization Tool BERN2 API

### Retrieve JSON  
To fetch JSON data, use the BERN2 API:  
**An Advanced Neural Biomedical Named Entity Recognition and Normalization Tool**  

<a href="http://bern2.korea.ac.kr/" target="_blank">
  <img src="https://img.shields.io/badge/Named_Entity_Recognition_-_BERN2_API-ff69b4.svg?style=for-the-badge&logo=Streamlit" alt="BERN2 API">
</a>  

Send a POST request to <a href="http://bern2.korea.ac.kr/" target="_blank">http://bern2.korea.ac.kr/</a>.  
Include your text data to annotate in the request body (plain text).  
BERN2 returns JSON annotations, which you can paste into this app.

#### Example Response  
```json
{
    "annotations": [
        {"mention": "protein1", "obj": "protein"},
        {"mention": "disease1", "obj": "disease"},
        {"mention": "gene1", "obj": "gene"}
    ]
}
```

---

### Screenshot  
Below is a screenshot that showcases the response from the BERN2 API:  
<img src="https://github.com/ParthebhanMedi/BioMed/blob/main/Screenshot%202025-01-26%20at%2009-01-59%20BERN2.png?raw=true" alt="Screenshot" width="600">

---

# JSON Annotations Viewer  

## This Streamlit app allows you to extract and filter unique mentions from a JSON file containing annotation data.  
You can filter mentions by object type and download the results as a CSV file.  

## 🌐 Try the App  
Access the app directly using the link below:  

<a href="https://jsonfilter.streamlit.app/" target="_blank">
  <img src="https://img.shields.io/badge/JSON_Annotations_Viewer_-_Streamlit_App-ff69b4.svg?style=for-the-badge&logo=Streamlit" alt="JSON Annotations Viewer">
</a>  

---

### Features  
- Parse JSON data containing `annotations`.  
- Extract all unique **mentions** and **object types**.  
- Sidebar filter option to view mentions by specific object types.  
- Download filtered mentions as a CSV file.  

---

## Author  
**Parthebhan Pari**

---
