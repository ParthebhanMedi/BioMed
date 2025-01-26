# FyLED



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

### Prerequisites  
- **Python >= 3.7**  
- Install the following Python libraries:  
  - `streamlit`  
  - `pandas`  

### Installation  
1. Clone the repository or copy the code.  
2. Install the required dependencies:  
   ```bash  
   pip install streamlit pandas
   ```  

### Usage  
1. Run the Streamlit app:  
   ```bash  
   streamlit run app.py
   ```  
   Replace `app.py` with the filename containing your Streamlit code.  

2. Paste your JSON into the provided text box in the app.  
   Ensure that the JSON follows this format:  
   ```json  
   {
       "annotations": [
           {"mention": "mention1", "obj": "objectType1"},
           {"mention": "mention2", "obj": "objectType2"},
           {"mention": "mention3", "obj": "objectType1"}
       ]
   }
   ```  

3. Use the **sidebar filter** to select an object type or "All" to view all mentions.  

4. Download filtered mentions as a CSV by clicking **Download Filtered Mentions as CSV**.  

### Expected Output  
When a valid JSON file is provided:  

#### Input JSON Example:  
```json  
{
    "annotations": [
        {"mention": "hello", "obj": "greeting"},
        {"mention": "world", "obj": "location"},
        {"mention": "streamlit", "obj": "tool"},
        {"mention": "hello", "obj": "greeting"}
    ]
}
```  

#### App Output (For Object Type: `greeting`):  
- **Number of Unique Mentions**: 1  
- **Filtered Mentions**: `hello`  

#### Output CSV Example:  
| **Unique Mentions** |  
|----------------------|  
| hello                |  

### Error Handling  
- If the pasted JSON is invalid, the app will display an error like:  
  ```
  Invalid JSON! Please check your input. Error: <description of the error>
  ```  

### Notes  
- The app expects the JSON structure to have an `annotations` key containing a list of objects with `mention` and `obj` fields.  
- Invalid or empty JSON input will result in an error message.  

### Author  
**Parthebhan Pari**  

---  
