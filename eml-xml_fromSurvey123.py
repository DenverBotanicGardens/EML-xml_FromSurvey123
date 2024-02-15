import pandas as pd
import zipfile
import os
import xml.etree.ElementTree as ET

def create_eml_xml(title,metadata_language, update_frequency, abstract, metadataProvider,individualName, givenName,surName,organizationName,positionName,address,deliveryPoint,city,administrativeArea,postalCode,country,phone, electronicMailAddress,personnel_identifier_provider, personnel_directory_provider):
    # Create the root element
    root = ET.Element("eml")

    # Create the dataset element
    dataset = ET.SubElement(root, "dataset")

    # Add the title element
    title_element = ET.SubElement(dataset, "title")
    title_element.text = title

    # Add the language element
    language_element = ET.SubElement(dataset, "language")
    language_element.text = metadata_language

    # Add the abstract element
    abstract_element = ET.SubElement(dataset, "abstract")
    abstract_element.text = abstract

    # Add the maintenance element with maintenanceUpdateFrequency
    maintenance_element = ET.SubElement(dataset, "maintenance")
    update_frequency_element = ET.SubElement(maintenance_element, "maintenanceUpdateFrequency")
    update_frequency_element.text = update_frequency

    # Add the metadataprovider element with sub elements
    metadataProvider_element = ET.SubElement(dataset, "metadataProvider")
    individualName_element = ET.SubElement(metadataProvider, "individualName")
    givenName_element = ET.SubElement(individualName, "givenName")
    surName_element = ET.SubElement(individualName, "surName")
    organizationName_element = ET.SubElement(metadataProvider, "organizationName")
    positionName_element = ET.SubElement(metadataProvider, "positionName")
    address_element = ET.SubElement(metadataProvider, "address")
    deliveryPoint_element = ET.SubElement(address, "deliveryPoint")
    city_element = ET.SubElement(address, "city")
    administrativeArea_element = ET.SubElement(address, "administrativeArea")
    postalCode_element = ET.SubElement(address, "postalCode")
    country_element = ET.SubElement(address, "country")
    phone_element = ET.SubElement(metadataProvider,"phone")
    electronicMailAddress_element = ET.SubElement(metadataprovider, "electronicMailAddress")
    user_id_element = ET.SubElement(dataset, "userId")
    user_id_element.set("directory", personnel_directory_provider)
    user_id_element.text = personnel_identifier_provider



    # Create the XML tree
    xml_tree = ET.ElementTree(root)

    return xml_tree

def main():
    # Path to the zipped folder
    zip_path = "./S123_879ca03c04fc4811ba89d191e85218f9_CSV.zip"
    
    # Extract the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("temp")

    # Path to the directory containing extracted files
    directory = "temp"

    # Read the Dataset_Metadata_0.csv file into a DataFrame
    metadata_df = pd.read_csv(os.path.join(directory, "Dataset_Metadata_0.csv"))

    # Extract values from the DataFrame
    title = metadata_df["Title"].iloc[0]  # Assuming there is only one title in the DataFrame
    metadata_language = metadata_df["metadataLanguage"].iloc[0]  # Assuming there is only one language in the DataFrame
    update_frequency = metadata_df["Update Frequency"].iloc[0]  # Assuming there is only one update frequency in the DataFrame
    abstract = metadata_df["Description"].iloc[0]
    givenName = metadata_df["firstName_provider"].iloc[0]
    surName = metadata_df["lastName_provider"].iloc[0]
    organizationName = metadata_df["organization_provider"].iloc[0]
    positionName = metadata_df["position_provider"].iloc[0]
    deliveryPoint = metadata_df["address_provider"].iloc[0]
    city = metadata_df["city_provider"].iloc[0]
    administrativeArea = metadata_df["stateProvince_provider"].iloc[0]
    postalCode = metadata_df["postalCode_provider"].iloc[0]
    country = metadata_df["country_provider"].iloc[0]
    phone = metadata_df["phone_provider"].iloc[0]
    electronicMailAddress = metadata_df["email_provider"].iloc[0]
    personnel_directory_provider = metadata_df["personnelDirectory_provider"].iloc[0]  # Assuming there is only one directory provider in the DataFrame
    personnel_identifier_provider = metadata_df["personnelIdentifier_provider"].iloc[0]  # Assuming there is only one identifier provider in the DataFrame
   
    # Create EML XML structure
    xml_tree = create_eml_xml(title,metadata_language, update_frequency,abstract,givenName,surName,organizationName,positionName,deliveryPoint,city,administrativeArea,postalCode,country,phone,electronicMailAddress,personnel_directory_provider,personnel_identifier_provider)

    # Write the XML tree to a file
    output_filename = "eml_output.xml"
    xml_tree.write(output_filename)

if __name__ == "__main__":
    main()
