import streamlit as st
import serpapi
import pandas as pd

# Application Title
st.title("Google Patents Search App Using SerpAPI - 5 search")
st.write("Search for patents using the [SerpAPI Google Patents engine](https://serpapi.com/google-patents-api).")

st.write("Created By: Parthebhan Pari")

# Input search query
query = st.text_input("Enter your search query", "(Coffee)")

# Initialize SerpAPI client using API key
api_key = st.text_input("Enter your SerpAPI Key", type="password")  # API key field
print(api_key)

if not api_key:
    st.error("Provide Valid SeriAPI Key")
    st.stop()

client = serpapi.Client(api_key=api_key)

if st.button("Start Search"):
    if not query.strip():
        st.warning("Please enter a valid search query.")
    else:
        with st.spinner("Fetching data..."):
            all_extracted_data = []  # Master data list
            page_number = 1  # Initial page number

            try:
                while len(all_extracted_data) < 100:
                    # Perform API search
                    results = client.search({
                        "engine": "google_patents",
                        "q": query.strip(),
                        "page": page_number
                    })

                    # Extract organic results
                    organic_results = results.get("organic_results", [])
                    
                    if not organic_results:
                        st.info(f"No results found for query: {query.strip()}")
                        break

                    # Collect data from organic results
                    for result in organic_results:
                        all_extracted_data.append({
                            "Title": result.get("title"),
                            "Snippet": result.get("snippet"),
                            "Filing Date": result.get("filing_date"),
                            "Grant Date": result.get("grant_date"),
                            "Inventor": result.get("inventor"),
                            "Assignee": result.get("assignee"),
                            "Patent ID": result.get("patent_id")
                        })

                    # Check if there's a next page
                    if "next" in results.get("serpapi_pagination", {}):
                        page_number += 1
                    else:
                        break

                # Display results if data is available
                if all_extracted_data:
                    df = pd.DataFrame(all_extracted_data)
                    st.success(f"Search completed. Total results: {len(all_extracted_data)}")
                    
                    # Display results in a table
                    st.dataframe(df)

                    # Download as CSV
                    csv = df.to_csv(index=False, encoding='utf-8')
                    st.download_button(
                        label="Download CSV",
                        data=csv,
                        file_name="patents_data.csv",
                        mime="text/csv",
                    )
                else:
                    st.warning("No results to display.")

            except Exception as e:
                st.error(f"An error occurred: {e}")