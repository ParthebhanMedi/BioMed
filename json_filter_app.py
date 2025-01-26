import json
import pandas as pd
import streamlit as st

# Streamlit App
st.title("JSON Annotations Viewer")
st.write("This app extracts all unique mentions and allows filtering by object type.")
st.write("Created By : Parthebhan Pari")
st.write("\n")

# Text Area to Paste JSON
st.subheader("Paste Your JSON Data Below")
json_input = st.text_area("Paste your JSON here:")

if json_input:  # If JSON is provided
    try:
        # Parse JSON
        data = json.loads(json_input)

        # Create a DataFrame from the "annotations" key
        annotations = data["annotations"]
        df = pd.DataFrame(annotations)

        # Extract unique mentions and unique objects
        unique_mentions = df["mention"].unique()
        unique_objects = df["obj"].unique()

        # Sidebar: Object Type Filter (Radio Button)
        st.sidebar.title("Filter Options")
        selected_object = st.sidebar.radio(
            "Select an Object Type to Filter", ["All"] + list(unique_objects)
        )

        # Filter DataFrame by selected object type
        if selected_object != "All":
            filtered_df = df[df["obj"] == selected_object]
            filtered_mentions = filtered_df["mention"].unique()  # Filtered unique mentions
        else:
            filtered_mentions = unique_mentions  # Show all mentions

        # Display Results
        st.write(f"**Showing Mentions for Object Type: `{selected_object}`**")
        st.write(f"**Number of Unique Mentions:** {len(filtered_mentions)}")

        # Display filtered mentions as a comma-separated string
        st.subheader("**Filtered Mentions:**")
        mentions_str = ", ".join(filtered_mentions)  # Convert to comma-separated string
        st.write(mentions_str)

        # Offer Download Button for Filtered Mentions as CSV
        csv_data = pd.DataFrame({"Unique Mentions": filtered_mentions})
        st.download_button(
            label="Download Filtered Mentions as CSV",
            data=csv_data.to_csv(index=False),
            file_name=f"filtered_mentions_{selected_object}.csv",
            mime="text/csv",
        )
    except Exception as e:
        st.error(f"Invalid JSON! Please check your input. Error: {e}")
else:
    st.info("Please paste your JSON data above to view the extracted mentions and click")
