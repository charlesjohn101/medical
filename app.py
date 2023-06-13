import streamlit as st

# Main Heading
st.title("Human Anatomy: Modality: Normal vs Abnormal")

# Create three equal-sized columns
col1, col2, col3 = st.columns(3)

# Select Box for 'a'
with col1:
    a_option = st.selectbox("Organ", ('Brain', 'Liver', 'Heart', 'Kidney'))

# Select Box for 'b'
with col2:
    b_option = st.selectbox("Modality", ('MRI', 'CT Scan', 'X-Ray'))

# Select Box for 'c'
with col3:
    if b_option == "X-Ray":
        c_option = st.selectbox("View", ('Anterior-posterior', 'Lateral'))
    else:
        c_option = st.selectbox("View", ('Axial', 'Sagittal', 'Coronal'))

# Create the subtitle based on the selected organ
subtitle = a_option + " Diseases"

# Display the subtitle with smaller font size
st.markdown(f"<h2 style='font-size: 22px;'>{subtitle}</h2>", unsafe_allow_html=True)
if a_option == 'Brain':
    st.markdown("<h4 style='font-size: 16px;'>1) Glioblastoma</h4>", unsafe_allow_html=True)
    option = st.radio("", ("Contrast", "Non-Contrast"))

    if b_option == "MRI" and c_option == "Axial":
        if option == "Contrast":
            image_files = ["Axial_C_N.jpg", "Axial_C_AB.jpg"]
        elif option == "Non-Contrast":
            image_files = ["Axial_NC_N.jpg", "Axial_NC_AB.jpg"]

    elif b_option == "MRI" and c_option == "Sagittal":
        if option == "Contrast":
            image_files = ["Sagittal_C_N.jpg", "Sagittal_C_AB.jpg"]
        elif option == "Non-Contrast":
            image_files = ["Sagittal_NC_N.jpg", "Sagittal_NC_AB.jpg"]

    elif b_option == "MRI" and c_option == "Coronal":
        if option == "Contrast":
            image_files = ["Coronal_C_N.jpg", "Coronal_C_AB.jpg"]
        elif option == "Non-Contrast":
            image_files = ["Coronal_NC_N.jpg", "Coronal_NC_AB.jpg"]

    elif b_option == "CT Scan" and c_option == "Axial":
        if option == "Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]
        elif option == "Non-Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]

    elif b_option == "CT Scan" and c_option == "Sagittal":
        if option == "Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]
        elif option == "Non-Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]

    elif b_option == "CT Scan" and c_option == "Coronal":
        if option == "Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]
        elif option == "Non-Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]

    elif b_option == 'X-Ray' and c_option == 'Anterior-posterior':
        if option == 'Contrast':
            image_files = ['Untitled design.jpg', 'Untitled design.jpg']
        elif option == 'Non-Contrast':
            image_files = ['Untitled design.jpg', 'Untitled design.jpg']

    elif b_option == 'X-Ray' and c_option == 'Lateral':
        if option == 'Contrast':
            image_files = ['Untitled design.jpg', 'Untitled design.jpg']
        elif option == 'Non-Contrast':
            image_files = ['Untitled design.jpg', 'Untitled design.jpg']

    col1, col2 = st.columns(2)
    for i, image_file in enumerate(image_files):
        with col2 if i % 2 != 0 else col1:
            # Add captions based on image type
            caption = "Normal Image" if i == 0 else "Abnormal Image"
            st.image(image_file, use_column_width=True, caption=caption)

    # Predefined bullet points


    with col1:
        st.markdown(
            "<ul style='text-align: justify'>"
            "<li>Glioblastoma is a type of astrocytoma, a cancer that forms from star-shaped cells in the brain called astrocytes.</li>"
            "<li>In adults, this cancer usually starts in the cerebrum, the largest part of your brain.</li>"
            "<li>Glioblastoma tumors make their own blood supply, which helps them grow. It’s easy for them to invade normal brain tissue.</li>"
            "<li>Glioblastoma is life-threatening and has a median survival time of only 15 months.</li>"
            "</ul>",
            unsafe_allow_html=True,
        )
    with col2:
        if b_option == "MRI":
            if c_option == "Axial" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>Irregular shaped ill-defined intra-axial space occupying lesion involving the inferior aspect of left temporooccipital region exhibits heterogeneous enhancement in post contrast study and exerting a positive mass effect upon the temporal horn of left lateral ventricle.</li>"
                    "<li>Multiple areas of intralesional necrosis are noted.</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Axial" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>An irregular heterogenous partially-enhancing mass, with cystic/necrotic components, is located medially in the left temporo-occipital and inferior parietal regions. This appears to be of intra-ventricular/subependymal origin, invading adjacent parenchyma, with extensive surrounding vasogenic edema and mass effect.</li>"
                    "<li>The left lateral ventricular atrium is severely compressed/replaced and displaced laterally, with obstructive dilatation of the temporal horn.</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Sagittal" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>Irregular shaped ill-defined intra-axial space occupying lesion involving the inferior aspect of left temporooccipital region exhibits heterogeneous enhancement in post contrast study and exerting a positive mass effect upon the temporal horn of left lateral ventricle.</li>"
                    "<li>Multiple areas of intralesional necrosis are noted.</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Sagittal" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>The sections show features of a densely cellular astrocytic tumor. The tumor cells show elongated, angulated and hyperchromatic nuclei. Some of the cells are smaller with rounder nuclei.</li>"
                    "<li>Nuclear molding is not seen. Scattered mitotic figures are identified.</li>"
                    "<li>There are foci of endothelial cell hyperplasia. Areas of necrosis are present.</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Coronal" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>Ring-enhancing mass in the right temporo-parietal region. </li>"
                    "<li>Some nodular componenets. Surrounding edema.</li>"
                    "<li> Blooming on GRE indicative of intralesional hemorrhage.</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Coronal" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>28*32*38 mm right temporal lobe abnormal signal intra-axial mass lesion with a central necrotic component and thick irregular wall enhancement associated with marked vasogenic edematous changes.</li>"
                    "<li>Mass effect and vasogenic edema causing the midline shift, effacement of right perimesencephalic cistern and pressure effect on the right cerebral peduncle.</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
        elif b_option == "CT Scan":
            if c_option == "Axial" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Axial Contrast bullet point 1</li>"
                    "<li>CT Scan Axial Contrast bullet point 2</li>"
                    "<li>CT Scan Axial Contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Axial" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Axial Non-contrast bullet point 1</li>"
                    "<li>CT Scan Axial Non-contrast bullet point 2</li>"
                    "<li>CT Scan Axial Non-contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Sagittal" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Sagittal Contrast bullet point 1</li>"
                    "<li>CT Scan Sagittal Contrast bullet point 2</li>"
                    "<li>CT Scan Sagittal Contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Sagittal" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Sagittal Non-contrast bullet point 1</li>"
                    "<li>CT Scan Sagittal Non-contrast bullet point 2</li>"
                    "<li>CT Scan Sagittal Non-contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Coronal" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Coronal Contrast bullet point 1</li>"
                    "<li>CT Scan Coronal Contrast bullet point 2</li>"
                    "<li>CT Scan Coronal Contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Coronal" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Coronal Non-contrast bullet point 1</li>"
                    "<li>CT Scan Coronal Non-contrast bullet point 2</li>"
                    "<li>CT Scan Coronal Non-contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
        elif b_option == "X-Ray":
            if c_option == "Anterior-posterior" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>X-Ray Anterior-posterior Contrast bullet point 1</li>"
                    "<li>X-Ray Anterior-posterior Contrast bullet point 2</li>"
                    "<li>X-Ray Anterior-posterior Contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Anterior-posterior" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>X-Ray Anterior-posterior Non-contrast bullet point 1</li>"
                    "<li>X-Ray Anterior-posterior Non-contrast bullet point 2</li>"
                    "<li>X-Ray Anterior-posterior Non-contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Lateral" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>X-Ray Lateral Contrast bullet point 1</li>"
                    "<li>X-Ray Lateral Contrast bullet point 2</li>"
                    "<li>X-Ray Lateral Contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Lateral" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>X-Ray Lateral Non-contrast bullet point 1</li>"
                    "<li>X-Ray Lateral Non-contrast bullet point 2</li>"
                    "<li>X-Ray Lateral Non-contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )



    st.markdown("<h4 style='font-size: 16px;'>2) Ischemic strokes </h4>", unsafe_allow_html=True)
    option = st.radio(" ", ("Contrast", "Non-Contrast"))

    if b_option == "MRI" and c_option == "Axial":
        if option == "Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]
        elif option == "Non-Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]

    elif b_option == "MRI" and c_option == "Sagittal":
        if option == "Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]
        elif option == "Non-Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]

    elif b_option == "MRI" and c_option == "Coronal":
        if option == "Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]
        elif option == "Non-Contrast":
            image_files = ["Untitled design.jpg", "Untitled design.jpg"]

    col1, col2 = st.columns(2)
    for i, image_file in enumerate(image_files):
        with col2 if i % 2 != 0 else col1:
            # Add captions based on image type
            caption = "Normal Image" if i == 0 else "Abnormal Image"
            st.image(image_file, use_column_width=True, caption=caption)

    # Predefined bullet points
    
    with col1:
        st.markdown("<ul style='text-align: justify'>"
                    "<li>Ischemic stroke is one of three types of stroke and is caused by a blockage in an artery that supplies blood to the brain.</li>"
                    "<li>If circulation isn’t restored quickly, brain damage can be permanent.</li>"
                    "<li>Ischemic stroke occurs when an artery that supplies blood to the brain is blocked by a blood clot or fatty buildup, called plaque.</li>"
                    "<li>Approximately 87 percent of all strokes are ischemic strokes.</li>"
                    "</ul>", unsafe_allow_html=True)
    with col2:
        if b_option == "MRI":
            if c_option == "Axial" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>MRI Axial Contrast bullet point 1</li>"
                    "<li>MRI Axial Contrast bullet point 2</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Axial" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>MRI Axial Non-contrast bullet point 1</li>"
                    "<li>MRI Axial Non-contrast bullet point 2</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Sagittal" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>MRI Sagittal Contrast bullet point 1</li>"
                    "<li>MRI Sagittal Contrast bullet point 2</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Sagittal" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>MRI Sagittal Non-contrast bullet point 1</li>"
                    "<li>MRI Sagittal Non-contrast bullet point 2</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Coronal" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>MRI Coronal Contrast bullet point 1</li>"
                    "<li>MRI Coronal Contrast bullet point 2</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Coronal" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>MRI Coronal Non-contrast bullet point 1</li>"
                    "<li>MRI Coronal Non-contrast bullet point 2</li>"
                    "<li>MRI Coronal Non-contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
        elif b_option == "CT Scan":
            if c_option == "Axial" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Axial Contrast bullet point 1</li>"
                    "<li>CT Scan Axial Contrast bullet point 2</li>"
                    "<li>CT Scan Axial Contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Axial" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Axial Non-contrast bullet point 1</li>"
                    "<li>CT Scan Axial Non-contrast bullet point 2</li>"
                    "<li>CT Scan Axial Non-contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Sagittal" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Sagittal Contrast bullet point 1</li>"
                    "<li>CT Scan Sagittal Contrast bullet point 2</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Sagittal" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Sagittal Non-contrast bullet point 1</li>"
                    "<li>CT Scan Sagittal Non-contrast bullet point 2</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Coronal" and option == "Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Coronal Contrast bullet point 1</li>"
                    "<li>CT Scan Coronal Contrast bullet point 2</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )
            elif c_option == "Coronal" and option == "Non-Contrast":
                st.markdown(
                    "<ul style='text-align: justify'>"
                    "<li>CT Scan Coronal Non-contrast bullet point 1</li>"
                    "<li>CT Scan Coronal Non-contrast bullet point 2</li>"
                    "<li>CT Scan Coronal Non-contrast bullet point 3</li>"
                    "</ul>",
                    unsafe_allow_html=True,
                )



    


# Add smaller-sized headings for specific diseases if 'Liver' is selected
if a_option == 'Liver':
    st.markdown("<h4 style='font-size: 16px;'>1) Cirrhosis</h4>", unsafe_allow_html=True)
    # Add information or content related to Cirrhosis here

    st.markdown("<h4 style='font-size: 16px;'>2) Hepatocellular carcinoma (HCC)</h4>", unsafe_allow_html=True)
    # Add information or content related to Hepatocellular carcinoma here

    st.markdown("<h4 style='font-size: 16px;'>3) Hepatic metastases</h4>", unsafe_allow_html=True)
    # Add information or content related to Hepatic metastases here



if a_option == 'Heart':
    st.markdown("<h4 style='font-size: 16px;'>1) Coronary Artery Disease (CAD)</h4>", unsafe_allow_html=True)
    option = st.radio("", ("Contrast", "Non-Contrast"))

    # Display images based on selected option
    if option == "Contrast":
        # Display images for Contrast
        col1, col2 = st.columns(2)
        with col1:
            st.image("CD1norm.jpg", use_column_width=True, caption="Contrast Image 1")
            st.markdown("- Predefined bullet point 1")
            st.markdown("- Predefined bullet point 2")
            st.markdown("- Predefined bullet point 3")
        with col2:   
            st.image("CD1abnorm.jpg", use_column_width=True, caption="Contrast Image 2")
            st.markdown("- Predefined bullet point 1")
            st.markdown("- Predefined bullet point 2")
            st.markdown("- Predefined bullet point 3")
    elif option == "Non-Contrast":
        # Display images for Non-Contrast
        col1, col2 = st.columns(2)
        with col1:

            st.image("NCD1norm.jpg", use_column_width=True, caption="Non-Contrast Image 1")
            st.markdown("- Predefined bullet point 1")
            st.markdown("- Predefined bullet point 2")
            st.markdown("- Predefined bullet point 3")
        with col2:
            st.image("NCD1abnorm.jpg", use_column_width=True, caption="Non-Contrast Image 2")
            st.markdown("- Predefined bullet point 1")
            st.markdown("- Predefined bullet point 2")
            st.markdown("- Predefined bullet point 3")
        st.markdown("<h4 style='font-size: 16px;'>2) Cardiomyopathy</h4>", unsafe_allow_html=True)
    # Add information or content related to Cardiomyopathy here


    # Add information or content related to Valvular Heart Disease here
if a_option == 'Kidney':
    st.markdown("<h4 style='font-size: 16px;'>1) Renal Cell Carcinoma (RCC)</h4>", unsafe_allow_html=True)
    # Add information or content related to Coronary Artery Disease here

    st.markdown("<h4 style='font-size: 16px;'>2) Polycystic Kidney Disease (PKD)</h4>", unsafe_allow_html=True)
    # Add information or content related to Cardiomyopathy here

    st.markdown("<h4 style='font-size: 16px;'>3) Kidney Stones (Renal Calculi)</h4>", unsafe_allow_html=True)
    # Add information or content related to Valvular Heart Disease here
 