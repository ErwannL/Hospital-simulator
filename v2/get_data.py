
MY_DATA = [
    ('vervolg consult', 'preassesment_opname', 'laboratory', 'e.e.g.', 'operation', 'mri', 'revalidatie'),
    ('laboratory', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'mri', 'vervolg consult'),
    ('revalidatie', 'laboratory', 'preassesment_opname', 'laboratory', 'e.c.g', 'operation', 'revalidatie', 'laboratory', 'e.c.g', 'laboratory', 'revalidatie', 'mri', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory', 'ct_scan', 'laboratory', 'ct_scan', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'vervolg consult', 'operation', 'mdo', 'vervolg_consult', 'revalidatie', 'mdo'),
    ('eerste_consult', 'preassesment_opname', 'revalidatie', 'laboratory', 'mri', 'laboratory', 'e.e.g.', 'operation', 'revalidatie', 'mri', 'mdo', 'vervolg consult', 'revalidatie', 'vervolg_consult', 'mdo', 'vervolg consult'),
    ('doorverwijzing', 'eerste_consult', 'preassesment_opname', 'laboratory', 'operation', 'mri', 'mdo', 'laboratory', 'vervolg_consult'),
    ('eerste_consult', 'e.c.g', 'preassesment_opname', 'laboratory', 'operation', 'mri', 'mdo', 'vervolg consult', 'vervolg_consult', 'revalidatie'),
    ('laboratory', 'revalidatie', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'mri', 'revalidatie', 'mdo'),
    ('preassesment_opname', 'laboratory', 'operation', 'laboratory', 'mri', 'laboratory', 'mdo'),
    ('laboratory', 'e.c.g', 'laboratory', 'preassesment_opname', 'ct_scan', 'laboratory', 'operation', 'laboratry', 'operation', 'laboratory', 'mri', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory', 'vervolg consult'),
    ('laboratory', 'mri', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory'),
    ('preassesment_opname', 'mdo', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'mri'),
    ('e.c.g', 'eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'revalidatie', 'vervolg_consult'),
    ('preassesment_opname', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'mri', 'laboratory', 'vervolg consult'),
    ('laboratory', 'ct_scan', 'eerste_consult', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'mri', 'revalidatie', 'laboratory', 'revalidatie', 'mdo', 'vervolg_consult', 'mdo'),
    ('eerste_consult', 'vervolg_consult', 'doorverwijzing', 'eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'mri', 'operation', 'mri', 'mdo', 'vervolg consult'),
    ('eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'ct_scan', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'vervolg consult'),
    ('eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'e.e.g.', 'operation', 'vervolg consult', 'mri', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'vervolg consult', 'laboratory', 'operation', 'laboratory', 'ct_scan', 'operation', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'vervolg consult', 'laboratory', 'medebehandeling', 'laboratory', 'vervolg consult'),
    ('preassesment_opname', 'vervolg consult', 'laboratory', 'mri', 'laboratory', 'operation', 'revalidatie', 'mri', 'e.e.g.', 'revalidatie', 'eerste_consult', 'spoedeisende_hulp', 'e.c.g', 'laboratory', 'e.c.g', 'revalidatie', 'vervolg_consult'),
    ('laboratory', 'e.c.g', 'laboratory', 'preassesment_opname', 'laboratory', 'vervolg consult', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'mri', 'vervolg consult', 'e.c.g'),
    ('eerste_consult', 'e.c.g', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'mri'),
    ('e.c.g', 'eerste_consult', 'preassesment_opname', 'vervolg_consult'),
    ('e.c.g', 'eerste_consult', 'preassesment_opname', 'laboratory', 'operation', 'vervolg_consult', 'revalidatie', 'mri', 'revalidatie'),
    ('laboratory', 'preassesment_opname', 'laboratory', 'vervolg consult', 'laboratory', 'operation', 'revalidatie', 'mri'),
    ('eerste_consult', 'e.c.g', 'preassesment_opname', 'laboratory', 'e.e.g.', 'operation', 'laboratory', 'operation', 'laboratory', 'mri', 'revalidatie'),
    ('laboratory', 'e.c.g', 'eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'vervolg consult'),
    ('eerste_consult', 'e.c.g', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'mri', 'laboratory', 'revalidatie', 'vervolg consult', 'revalidatie', 'mri', 'revalidatie', 'eerste_consult', 'e.c.g', 'preassesment_opname', 'laboratory', 'operation', 'mri', 'revalidatie', 'vervolg_consult', 'revalidatie'),
    ('laboratory', 'eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'e.c.g', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'vervolg_consult', 'mdo', 'eerste_consult', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'e.e.g.', 'mdo', 'revalidatie', 'mri', 'vervolg_consult', 'mdo'),
    ('laboratory', 'e.c.g', 'eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'mri', 'vervolg_consult'),
    ('eerste_consult', 'vervolg_consult', 'e.c.g', 'revalidatie', 'preassesment_opname'),
    ('eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'ct_scan', 'laboratory', 'ct_scan', 'e.e.g.', 'laboratory', 'mri', 'laboratory'),
    ('revalidatie', 'eerste_consult', 'preassesment_opname', 'revalidatie', 'laboratory', 'operation', 'laboratory', 'operation', 'e.c.g', 'revalidatie', 'laboratory', 'mri', 'revalidatie'),
    ('laboratory', 'e.c.g', 'eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'operation', 'mri', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'vervolg consult', 'revalidatie', 'vervolg consult'),
    ('doorverwijzing', 'eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'mdo', 'vervolg consult', 'mdo', 'vervolg consult', 'vervolg_consult', 'preassesment_opname', 'laboratory', 'revalidatie', 'laboratory', 'operation', 'revalidatie', 'mri', 'revalidatie'),
    ('doorverwijzing', 'eerste_consult', 'laboratory', 'e.c.g', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'mri', 'mdo'),
    ('doorverwijzing', 'eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'ct_scan', 'e.e.g.', 'operation', 'laboratory', 'revalidatie', 'mri', 'revalidatie', 'mdo', 'vervolg_consult'),
    ('mdo', 'eerste_consult', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory', 'mri', 'preassesment_opname', 'revalidatie', 'laboratory', 'e.e.g.', 'operation', 'mri', 'mdo', 'revalidatie', 'laboratory', 'revalidatie', 'vervolg consult'),
    ('mdo', 'doorverwijzing', 'e.c.g', 'eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'mdo'),
    ('eerste_consult', 'laboratory', 'e.c.g', 'laboratory', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'mdo', 'laboratory', 'vervolg_consult'),
    ('laboratory', 'eerste_consult', 'laboratory', 'operation', 'laboratory', 'revalidatie', 'laboratory', 'operation', 'mdo', 'vervolg consult', 'vervolg_consult'),
    ('eerste_consult', 'e.c.g', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'mdo', 'vervolg consult', 'vervolg_consult'),
    ('eerste_consult', 'e.c.g', 'preassesment_opname', 'laboratory', 'operation', 'mri', 'mdo', 'vervolg consult'),
    ('doorverwijzing', 'e.c.g', 'eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'mdo', 'vervolg consult', 'revalidatie', 'vervolg_consult', 'laboratory'),
    ('eerste_consult', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'mri', 'mdo', 'laboratory', 'vervolg_consult', 'mdo'),
    ('revalidatie', 'preassesment_opname', 'revalidatie', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie'),
    ('eerste_consult', 'e.c.g', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'mri', 'mdo', 'vervolg consult', 'revalidatie', 'vervolg_consult'),
    ('eerste_consult', 'vervolg_consult', 'revalidatie', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'mdo', 'vervolg_consult', 'revalidatie', 'mdo'),
    ('doorverwijzing', 'eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'mri', 'laboratory', 'mdo', 'vervolg consult'),
    ('mdo', 'eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'e.e.g.', 'operation', 'mri', 'operation', 'vervolg consult', 'vervolg_consult', 'mdo'),
    ('eerste_consult', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'mdo', 'vervolg_consult'),
    ('eerste_consult', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'mri', 'mdo', 'vervolg consult', 'revalidatie', 'vervolg_consult'),
    ('doorverwijzing', 'eerste_consult', 'revalidatie', 'preassesment_opname', 'laboratory', 'operation', 'revalidatie', 'mri', 'revalidatie', 'mdo', 'vervolg_consult'),
    ('eerste_consult', 'vervolg_consult', 'revalidatie', 'laboratory', 'preassesment_opname', 'laboratory', 'e.e.g.', 'operation', 'mri', 'mdo', 'vervolg consult'),
    ('doorverwijzing', 'eerste_consult', 'laboratory', 'e.c.g', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'revalidatie', 'mri', 'revalidatie', 'mdo'),
    ('doorverwijzing', 'eerste_consult', 'revalidatie'),
    ('e.c.g', 'eerste_consult', 'preassesment_opname', 'laboratory', 'operation'),
    ('doorverwijzing', 'eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation'),
    ('mdo', 'laboratory', 'eerste_consult', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'ct_scan', 'laboratory', 'mri', 'e.e.g.', 'operation', 'laboratory', 'operation', 'laboratory', 'revalidatie', 'laboratory', 'ct_scan', 'e.c.g', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'mdo'),
    ('laboratory', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'mdo'),
    ('doorverwijzing', 'eerste_consult', 'laboratory', 'e.c.g', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'mri', 'mdo'),
    ('operation'),
    ('laboratory', 'ct_scan', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'mri', 'revalidatie', 'vervolg_consult', 'ct_scan', 'operation', 'preassesment_opname', 'laboratory', 'ct_scan', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'vervolg consult', 'operation', 'spoedeisende_hulp', 'vervolg consult'),
    ('eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'mri', 'vervolg consult', 'mdo', 'vervolg consult', 'preassesment_opname', 'laboratory', 'e.c.g', 'operation', 'revalidatie', 'mri', 'mdo', 'vervolg consult', 'vervolg_consult', 'mdo'),
    ('eerste_consult', 'preassesment_opname', 'laboratory', 'operation', 'mri', 'vervolg_consult', 'mdo', 'vervolg consult', 'laboratory', 'preassesment_opname', 'laboratory', 'e.e.g.', 'operation', 'mri', 'mdo', 'laboratory', 'vervolg_consult', 'mdo'),
    ('eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'revalidatie', 'mri', 'mdo', 'vervolg_consult', 'mdo'),
    ('eerste_consult', 'laboratory', 'e.c.g', 'laboratory', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'revalidatie', 'laboratory', 'mri', 'revalidatie', 'laboratory', 'ct_scan', 'e.c.g', 'laboratory', 'ct_scan', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory'),
    ('eerste_consult', 'laboratory', 'e.c.g', 'laboratory', 'preassesment_opname', 'laboratory', 'e.e.g.', 'operation', 'mri', 'revalidatie', 'vervolg consult', 'mdo'),
    ('doorverwijzing', 'e.c.g', 'eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'revalidatie'),
    ('preassesment_opname', 'laboratory', 'operation', 'revalidatie', 'mri', 'laboratory', 'ct_scan', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'vervolg consult', 'mdo'),
    ('doorverwijzing', 'eerste_consult', 'revalidatie', 'laboratory', 'revalidatie', 'mri', 'laboratory', 'operation', 'revalidatie', 'mri', 'mdo', 'vervolg consult', 'vervolg_consult'),
    ('laboratory', 'operation', 'medebehandeling', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'vervolg consult', 'laboratory', 'mri', 'laboratory', 'operation', 'laboratory', 'vervolg consult', 'revalidatie', 'preassesment_opname', 'laboratory', 'revalidatie', 'laboratory', 'e.e.g.', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'revalidatie', 'mri', 'vervolg consult', 'laboratory', 'ct_scan', 'laboratory', 'operation', 'laboratory', 'vervolg consult', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'vervolg consult', 'mdo'),
    ('vervolg consult', 'laboratory', 'mri', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'operation', 'laboratory', 'vervolg_consult'),
    ('doorverwijzing', 'eerste_consult', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'mdo', 'vervolg consult'),
    ('laboratory', 'eerste_consult', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'operation', 'revalidatie', 'operation', 'laboratory', 'revalidatie', 'mri', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'mdo', 'vervolg consult', 'vervolg_consult'),
    ('operation', 'eerste_consult', 'preassesment_opname', 'laboratory', 'operation', 'revalidatie', 'mri', 'mdo'),
    ('laboratory', 'eerste_consult', 'laboratory', 'mri', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'operation', 'mdo'),
    ('eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'e.c.g', 'laboratory', 'mri', 'laboratory', 'operation', 'mri', 'revalidatie', 'mdo', 'vervolg consult', 'vervolg_consult', 'mdo'),
    ('eerste_consult', 'laboratory', 'mri', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'revalidatie', 'mri', 'mdo', 'vervolg_consult', 'mdo'),
    ('eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'mri', 'laboratory', 'operation', 'mdo', 'vervolg consult'),
    ('eerste_consult', 'preassesment_opname', 'laboratory', 'operation', 'laboratory', 'revalidatie', 'mri', 'revalidatie', 'vervolg consult', 'laboratory'),
    ('doorverwijzing', 'eerste_consult', 'laboratory', 'mri', 'preassesment_opname', 'laboratory', 'e.e.g.', 'operation', 'laboratory'),
    ('eerste_consult', 'mri', 'preassesment_opname', 'laboratory', 'eerste_consult', 'laboratory', 'mri', 'laboratory', 'spoedeisende_hulp', 'laboratory', 'ct_scan', 'laboratory', 'operation', 'laboratory', 'revalidatie', 'mri', 'revalidatie', 'laboratory', 'revalidatie', 'laboratory', 'revalidatie', 'vervolg consult', 'laboratory', 'vervolg_consult', 'mdo'),
    ('eerste_consult', 'laboratory', 'e.c.g', 'laboratory', 'mri', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'mri', 'mdo', 'vervolg consult', 'vervolg_consult'),
    ('laboratory', 'e.c.g', 'eerste_consult', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'ct_scan', 'laboratory', 'operation', 'mdo'),
    ('eerste_consult', 'laboratory', 'e.c.g', 'laboratory', 'preassesment_opname', 'laboratory', 'operation', 'revalidatie', 'mri', 'revalidatie', 'laboratory', 'revalidatie', 'mdo', 'laboratory', 'vervolg_consult')
]



from re import X
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# Function to load and preprocess data from a CSV file
def load_data(file_path):
    """
    Loads the CSV file at the specified path, processes the 'prod_agb_spec_omschr' column,
    and returns a list of sequences after preprocessing (e.g., splitting strings into lists).

    Arguments:
    file_path -- str : The path to the CSV file

    Returns:
    list : A list of sequences where each sequence is a list of items (e.g., steps in a pathway)
    """
    # Read the CSV file into a pandas DataFrame.
    # The DataFrame is a table-like data structure used for data manipulation and analysis.
    df = pd.read_csv(file_path)

    # Preprocess the 'prod_agb_spec_omschr' column:
    # 1. Extract the string content between the square brackets by removing the first and last characters.
    # 2. Remove all single quotes from the string to clean it up.
    # 3. Split the cleaned string into individual items using ', ' as a delimiter.
    # 4. Convert each processed string into a Python list.
    # Apply these transformations to each row in the column and return the result as a list of lists.
    data = df['prod_agb_spec_omschr'].apply(
        lambda x: x[1:-1].replace("'", "").split(", ")
    ).tolist()

    # Return the preprocessed data as a list of sequences
    return data

def find_repeated_sequences(data, length=5):
    """
    Finds the most repeated sequences of a specified length within the given data.
    Each sequence is extracted from a group, and their frequency of occurrence is calculated.

    Arguments:
    data -- list : A list of groups, where each group is a list of items (e.g., sequences of steps).
    length -- int : The length of the sequences to search for (default is 5).

    Returns:
    list : A list of the top 5 most repeated sequences, each represented as a tuple (sequence, count).
    """
    # Initialize an empty dictionary to count the occurrences of each sequence
    sequence_counts = {}

    # Iterate over each group in the data
    for group in data:
        # Slide through the group to extract all subsequences of the specified length
        for i in range(len(group) - length + 1):
            sequence = tuple(group[i:i + length])  # Extract a subsequence as a tuple

            # Check if the sequence already exists in the dictionary
            if sequence in sequence_counts:
                # Increment the count if it exists
                sequence_counts[sequence] += 1
            else:
                # Initialize the count if it's the first occurrence
                sequence_counts[sequence] = 1

    # Sort the sequences by their frequency in descending order
    # Each item in the sorted list is a tuple: (sequence, count)
    sorted_sequences = sorted(sequence_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the top 5 most repeated sequences
    return sorted_sequences[:5]

# Function to add suffixes to steps in a pathway based on specific conditions
def add_suffixes(path, pathway_number):
    """
    Adds suffixes to the steps in a pathway based on conditions such as the presence of "laboratory" or "MRI".
    The suffixes help differentiate between similar steps based on their occurrence in the pathway.

    Arguments:
    path -- list : A list of steps in a pathway (e.g., patient care steps).
    pathway_number -- int : The pathway number that affects the suffix for laboratory steps.

    Returns:
    list : A modified list of steps with suffixes appended where necessary.
    """
    # Initialize an empty list to store the updated pathway with suffixes
    updated_path = []

    # Initialize counters for laboratory and operation steps to ensure unique suffixes
    laboratory_count = 1
    operation_count = 1

    # Adjust initial counters based on the pathway number
    if pathway_number == 1 or pathway_number == 4:
        operation_count += 1  # Start the operation count from 2 for specific pathways
    if pathway_number == 2:
        laboratory_count += 1  # Adjust laboratory count for pathway 2

    # Iterate through each step in the given pathway
    for step in path:
        if "laboratory" in step:  # Check if the step is related to a laboratory
            suffix = laboratory_count  # Assign the current laboratory count as the suffix
            laboratory_count += 1  # Increment the laboratory counter for the next laboratory step
        elif "operation" in step:  # Check if the step is related to an operation
            suffix = operation_count  # Assign the current operation count as the suffix
            operation_count += 1  # Increment the operation counter for the next operation step
        else:
            suffix = None  # No suffix for other steps

        # Append the step with its suffix if applicable, or just append the step itself
        if suffix:
            updated_path.append(f"{step}_{suffix}")
        else:
            updated_path.append(step)  # No suffix, just append the step as it is

    # Return the modified pathway with suffixes
    return updated_path

# Function to create pathways with added suffixes
def create_pathways(sorted_patterns):
    """
    Processes the sorted patterns and creates pathways with added suffixes.

    Arguments:
    sorted_patterns -- list : A list of sorted patterns, where each pattern is a tuple 
                              containing a sequence of steps and its corresponding support value.

    Returns:
    list : A list of pathways, where each pathway is a tuple with the updated pattern (with suffixes) 
           and its corresponding support value.
    """
    # Initialize an empty list to store the pathways with suffixes
    pathways = []

    # Iterate over each sorted pattern, including both the pattern (sequence of steps) and support value
    for idx, (pattern, support) in enumerate(sorted_patterns):
        # Add suffixes to the current pattern using the add_suffixes function, treating the first pattern differently
        updated_pattern = add_suffixes(pattern, idx)

        # Append the updated pattern with its support value to the pathways list
        pathways.append((updated_pattern, support))

    # Return the list of pathways with suffixes
    return pathways

# Function to create the network graph from the pathways
def create_graph(pathways):
    """
    Creates a graph (network) from the given pathways where each step in a pathway is a node,
    and edges represent transitions between steps with pattern support as edge weights.

    Arguments:
    pathways -- list : A list of pathways where each pathway is a tuple containing a list of steps 
                        and its corresponding support (frequency) value.

    Returns:
    networkx.Graph : A NetworkX graph object representing the pathways and transitions.
    """
    # Create an empty undirected graph using NetworkX
    G = nx.Graph()

    # Iterate over each pathway in the pathways list
    for idx, (pathway, frequency) in enumerate(pathways):
        # Iterate over consecutive steps in the current pathway to create edges between them
        for i in range(len(pathway) - 1):
            source = pathway[i]  # The current step (source node)
            target = pathway[i + 1]  # The next step (target node)

            # If an edge already exists between the source and target, add the current pattern and frequency to it
            if G.has_edge(source, target):
                # Append the pattern and frequency to the existing edge's 'patterns' attribute
                G[source][target]['patterns'].append((idx, frequency))
            else:
                # If no edge exists, create a new edge with the 'patterns' attribute initialized
                G.add_edge(source, target, patterns=[(idx, frequency)])

    # Return the constructed graph
    return G

# Function to determine the positions of the nodes for visualization
def position_nodes(pathways):
    """
    Assigns specific positions to each node in the graph based on the order of appearance in the pathways.
    The first pathway is placed horizontally, and the other pathways are placed vertically.

    Arguments:
    pathways -- list : A list of pathways, where each pathway is a list of steps (nodes).

    Returns:
    dict : A dictionary with node names as keys and their positions (x, y coordinates) as values.
    """
    # Initialize an empty dictionary to store the positions of each node
    node_positions = {}

    # Horizontal positioning for the first pathway
    horizontal_path = pathways[0][0]  # Get the first pathway (list of steps)
    for i, node in enumerate(horizontal_path):
        # Place nodes from the first pathway horizontally with a gap of 3 units between nodes
        node_positions[node] = (i * 3, 0)  # x-coordinate increases by 3 for each node, y is fixed at 0

    # Initialize y-position for subsequent pathways to be placed vertically
    y_position = -2  # Start with a negative y-position for the second pathway
    same_height_nodes = 3  # Control the vertical placement of nodes at the same y-level
    changed_node_position = 0  # Track if a node's position has changed

    # Iterate through the remaining pathways (excluding the first one)
    for idx, (pathway, _) in enumerate(pathways[1:], start=1):
        for i, node in enumerate(pathway):
            # Only position nodes that haven't been positioned already
            if node not in node_positions:
                # Adjust y-position based on available space
                if same_height_nodes == 0:
                    y_position -= 2  # Move to the next row after 3 nodes
                    changed_node_position = 2  # Reset the node position counter
                else:
                    changed_node_position = same_height_nodes
                    same_height_nodes -= 1  # Decrease counter as nodes are positioned

                # Place nodes based on their position in the pathway and vertical constraints
                if changed_node_position == 1:
                    node_positions[node] = ((i + 1) * 3, y_position)  # Position node at the current y-level
                elif same_height_nodes == 0:
                    node_positions[node] = ((i - 2) * 3, y_position + 2)  # Position node at a higher y-level
                else:
                    node_positions[node] = ((i - 1) * 3, y_position)  # Continue positioning nodes at current y-level

    # Return the dictionary with node positions (x, y coordinates)
    return node_positions

# Function to draw the graph
def draw_graph(G, node_positions, pathways):
    """
    Draws the network graph using the positions of nodes and color-coded edges to represent different pathways.

    Arguments:
    G -- networkx.Graph : The graph object representing the pathways
    node_positions -- dict : A dictionary of node positions (x, y coordinates)
    pathways -- list : A list of pathways (for color coding of edges)
    """
    plt.figure(figsize=(15, 5))  # Set up the figure size for visualization

    # Draw nodes with beige color and border matching the node color
    nx.draw_networkx_nodes(G, node_positions, node_size=2000, node_color="beige", edgecolors="beige")

    # Initialize dictionaries for edge labels (frequencies) and label positions
    edge_labels = {}  # Store edge labels with frequencies
    label_positions = {}  # Placeholder for storing label positions (optional for further customization)

    # Define a color map for different pathways
    path_colors = {
        0: "pink",   # Color for the first pathway
        1: "gray",   # Color for the second pathway
        2: "blue",   # Color for the third pathway
        3: "green",  # Color for the fourth pathway
        4: "brown",  # Color for the fifth pathway
    }

    top_or_down = 0.2  # Control for edge position offset (up or down)

    mri_okay = 2  # A flag to control certain edge conditions

    # Iterate over each edge in the graph to draw them
    for edge in G.edges(data=True):
        source, target, attributes = edge  # Extract edge details (source, target, and attributes)

        # Get the list of path colors for each pattern in the edge
        color_list = [path_colors[pattern_idx] for pattern_idx, _ in attributes['patterns']]
        num_lines = len(color_list)  # Count how many different edges are drawn for this connection
        offset = 0  # Initialize offset for edge positioning

        # Draw each edge separately for each pattern
        for pattern_idx, frequency in attributes['patterns']:
            color = path_colors[pattern_idx]  # Determine the color for the current pattern
            if source == pathways[0][0][0] and target == pathways[1][0][2] and mri_okay != 0:
                mri_okay -= 1
                top_or_down = 0.2  # Adjust offset based on specific conditions
            else:
                top_or_down = -0.2  # Adjust offset for other cases

            if (color == "green" or color == "brown") and source == pathways[0][0][0]:
                offset -= 1  # Adjust the offset when certain colors are involved

            y_offset_adjusted = offset * top_or_down  # Adjust vertical offset to prevent overlap
            nx.draw_networkx_edges(
                G, node_positions,
                edgelist=[(source, target)],
                edge_color=color,
                width=frequency / 2,  # Set edge width based on frequency
                arrows=True,  # Display arrows on edges to indicate direction
                alpha=0.7,  # Set transparency for edges
                style='solid',  # Solid edge style
                connectionstyle=f"arc3,rad={y_offset_adjusted}"  # Add curvature to the edges
            )
            edge_labels[(source, target, color)] = frequency  # Store the frequency for edge labeling
            offset += 1.5  # Increment offset to prevent overlapping edges

    # Draw node labels (names of the nodes)
    nx.draw_networkx_labels(G, node_positions, font_size=6, font_weight='bold', font_color="black")

    # Draw edge labels (frequencies)
    last = None  # Variable to track the last edge for label positioning
    pos = 0.5  # Starting position for edge labels
    pos_or_neg_adjustment = 1  # Directional switch for label positioning
    x_move = 0.2  # Horizontal shift for label movement
    for (source, target, color), frequency in edge_labels.items():
        if last == (source, target):
            pos += (x_move * pos_or_neg_adjustment)  # Adjust position for repeating edges
            pos_or_neg_adjustment *= -1  # Alternate direction for alternating edges
            x_move += 0.2  # Increase horizontal shift for successive edges
        else:
            pos = 0.5  # Reset position for new edge
            x_move = 0.2  # Reset horizontal movement increment
        nx.draw_networkx_edge_labels(
            G, node_positions,
            edge_labels={(source, target): frequency},  # Show frequency as label
            font_size=8,
            font_weight='bold',
            font_color=color,
            verticalalignment="center",
            horizontalalignment="center",
            label_pos=pos  # Position label at the adjusted position
        )
        last = (source, target)  # Update last edge for positioning

    # Final adjustments and plot settings
    plt.title("UMCG Patient Care Pathway Visualization", fontdict={
              'fontsize': 16,  # Title font size
              'fontweight': 'bold',  # Bold title font
              'fontfamily': 'serif',  # Title font style
              'color': 'darkblue'  # Title color
          })
    plt.axis("off")  # Hide axes for cleaner visualization
    plt.tight_layout()  # Ensure tight layout with no overlaps
    plt.show()  # Display the graph

# Main function to execute the workflow
def main():
    """
    Main function that loads data, processes patterns, creates the network graph,
    and visualizes the results.
    """
    # Path to the data file
    # output_path = "/content/drive/Shareddrives/UMCG/Data and Code/Input Output/OutputEfficient/DataOutputReducedNEW.csv"

    # Load and preprocess data
    # data = load_data(output_path)

    # Find frequent patterns in the data
    sorted_patterns = find_repeated_sequences(MY_DATA)

    # Create pathways with suffixes added
    pathways = create_pathways(sorted_patterns)

    # # Create the graph based on the pathways
    G = create_graph(pathways)

    # # Determine the node positions for visualization
    node_positions = position_nodes(pathways)

    # # Draw and visualize the graph
    draw_graph(G, node_positions, pathways)

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
