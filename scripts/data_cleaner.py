import pandas as pd
import numpy as np
import re

# First load in the answer key
answer_key = pd.read_csv('../data/answer_key.csv', index_col='index')

# Load full DataFrame and remove irrelevant columns
df = pd.read_csv('../../Private/screened.csv', skiprows=[1])
df.drop(columns=['StartDate', 'EndDate', 'Status', 'RecordedDate', 'UserLanguage', 'sig_year_1_TEXT',
                 'comp_year_1_TEXT', 'consent', 'more_thoughts'], inplace=True)


# Time to painstakingly go through each multi-select column and break each option into a unique column
def list_reformat(original_col, target, new_col=None):
    if not new_col: new_col = re.sub('\W', '', answer_key[original_col][i].title())
    df[new_col] = df[original_col].apply(lambda x: 0 if type(x) != str else int(str(target) in x.split(','))).astype('int8')

# For the resource location
list_reformat('resource_location', 1, 'CloudUser')
list_reformat('resource_location', 2, 'OnPremise')

# For the funding source of compute funds
for i, c in zip([1,9,10,11], ['UsedFree', 'UsedPersonal', 'UsedGrants', 'EmployerPaid']):
    list_reformat('compute_budget', i, c)

# For desired resources from the NAIRR
for i, c in zip([1,2,3,6,7], ['WantsData', 'WantsCompute', 'WantsStaff', 'WantsGrants', 'WantsStandards']):
    list_reformat('useful_resources', i, c)

# For AI subfields
for i, c in zip([6,7,8,9,10], ['CV', 'Robotics', 'NLP', 'RL', 'Other']):
    list_reformat('AI_subfield_i', i, c)

# Do the same for CV subfields but with some work arounds
for i in range(1, 10):
    list_reformat('vision_subfield_i', i)
list_reformat('vision_subfield_i', 10, 'CVOther')

# Do the same for robotics subfields but with some work arounds
for i in range(1, 9):
    list_reformat('robotics_subfield_i', i)
list_reformat('robotics_subfield_i', 9, 'RobotOther')

# Do the same for NLP subfields but with some work arounds
for i in range(35, 52):
    if i == 45: list_reformat('nlp_subfield_i', i, 'NLPOther')
    else: list_reformat('nlp_subfield_i', i)

# Next for RL subfields
for i in range(1, 9):
    if i == 7: list_reformat('rl_subfield_i', i, 'RLOther')
    else: list_reformat('rl_subfield_i', i)

# And finally for Other subfields
for i in range(6, 13):
    list_reformat('other_subfield_i', i)

# Reformat the sig_no_project column to have no NA values
df['NoSigProject'] = df['sig_no_project'].apply(lambda x: int(x == 1.))

# Drop columns that are now obsolete
df.drop(columns = ['resource_location', 'compute_budget', 'useful_resources', 'AI_subfield_i',
                  'vision_subfield_i', 'robotics_subfield_i', 'nlp_subfield_i', 'rl_subfield_i',
                  'other_subfield_i', 'sig_no_project'], inplace=True)


# If the most significant project was also the most compute-intensive, duplicate the answers to both columns
df['comp_total_cost'] = df.apply(lambda x: x['comp_total_cost'] if x['same_project'] == 4 else x['sig_total_cost'], axis=1)
df['comp_training_cost'] = df.apply(lambda x: x['comp_training_cost'] if x['same_project'] == 4 else x['sig_training_cost'], axis=1)
df['comp_team_size'] = df.apply(lambda x: x['comp_team_size'] if x['same_project'] == 4 else x['sig_team_size'], axis=1)
df['comp_year'] = df.apply(lambda x: x['comp_year'] if x['same_project'] == 4 else x['sig_year'], axis=1)
df['comp_component'] = df.apply(lambda x: x['comp_component'] if x['same_project'] == 4 else x['sig_component'], axis=1)


# Next, work through the categorical questions and reformat the answers to be non-numeric
def cat_reformat(col, new_name):
    df[new_name] = df[col].apply(lambda x: answer_key[col][x] if x in answer_key[col] else pd.NA)
    df.drop(columns=[col], inplace=True)

# Apply the above function to each categorical question
for c, n in zip(['sig_component', 'comp_component', 'budget_priorities', 'role', 'leaving_academia', 'same_project'],
               ['SigComponent', 'CompComponent', 'TopPriority', 'Sector', 'ConsideredLeaving', 'SameProject']):
    cat_reformat(c, n)

# For the last two, however, convert 'Yes' and 'No' to 1 and 0
binary_dict = {'Yes': 1, 'No': 0}
df['ConsideredLeaving'] = df.ConsideredLeaving.apply(lambda x: binary_dict[x] if x in binary_dict else pd.NA).astype('Int8')
df['SameProject'] = df.SameProject.apply(lambda x: binary_dict[x] if x in binary_dict else pd.NA).astype('Int8')

# Create a column to batch responses for the budget priorities question
priorities = {'Collecting more data': 'Data', 'Refining or cleaning data': 'Data',
             'Hiring researchers': 'Talent', 'Hiring more programmers or engineers': 'Talent',
             'Purchasing more or higher-quality compute': 'Compute',
             'Doing more evaluation or testing': 'Evaluation'}
df['PrioritySimplified'] = df['TopPriority'].apply(lambda x: priorities[x] if x in priorities else pd.NA)

# Reformat the `company_size` column into a categorical binary feature (using ONLY responses from industry, not government)
size_dict = {1: 0, 2: 0, 3: 0, 4: 1}
df['LargeCompany'] = df.apply(lambda x: size_dict[x['company_size']] if x['company_size'] in size_dict and x['Sector'] == 'Industry' else pd.NA, axis=1).astype('Int8')

# Similarly, reformat the `education` column into a categorical binary feature
edu_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1}
df['HasPhD'] = df.education.apply(lambda x: edu_dict[x] if x in edu_dict else pd.NA).astype('Int8')
df.drop(columns = ['company_size', 'education'], inplace=True)


# If questions are ordinal, we need to map recorded values one-by-one to their proper ordering
def reformat_ordinal(col, orig_ids, new_ids=None, new_col_name=None):
    if not new_col_name: new_col_name = re.sub('_', '', col.title())
    if not new_ids: new_ids = range(len(orig_ids))
    df[new_col_name] = df[col].apply(lambda x: new_ids[orig_ids.index(x)] if x in orig_ids else np.nan).astype('Int8')
    df.drop(columns = [col], inplace=True)

# Go through the ordinal data frames and reformat them appropriately, starting each sequence at 0 and
# binning values as needed (note: 'I don't know' responses are converted to NaN)
reformat_ordinal('screener', [4,5,6,7])
reformat_ordinal('tenure', [1,2,3,4], new_ids = [0,0,1,2])
reformat_ordinal('time_managing', [1,4,5,6])
reformat_ordinal('personal_cost', [1,4,5,6,7])
reformat_ordinal('multiple_processors', [1,3,4,5])
for prefix in ['sig', 'comp']:
    reformat_ordinal(f'{prefix}_team_size', list(range(1,6)))
    reformat_ordinal(f'{prefix}_year', [3,4,5,6,7,1,8])
    reformat_ordinal(f'{prefix}_total_cost', list(range(1,7)), new_col_name = f'{prefix.title()}Cost')
reformat_ordinal('sig_training_cost', [1,14,8,9,10,11,12], new_col_name = 'SigGPUs')

# Note that due to some Qualtrics strangeness, both 1 AND 7 correspond to "None" as a response
reformat_ordinal('comp_training_cost', [1,7,14,8,9,10,11,12], new_ids = [0,0,1,2,3,4,5,6], new_col_name = 'CompGPUs')


# Finally, let's rename the Likert scale questions to be more descriptive (Note that some columns fall in the
# range [6,10] due to Qualtrics weirdness, but all should be reformatted to fall into the range [0,4])
def rename_likert(old_name, new_name):
    df[new_name] = df[old_name].apply(lambda x: x - min(df[old_name]) if x > 0 else pd.NA).astype('Int8')
    df.drop(columns = [old_name], inplace = True)

# Work through the various Likert scale questions to rename them
for i, c in enumerate(['SuccessData', 'SuccessTeamSize', 'SuccessTalent', 'SuccessCompute']):
    rename_likert(f'sig_factors_{i+1}', c)

for i, c in enumerate(['Reject', 'Revise', 'Abandon']):
    rename_likert(f'comp_proj_changes_{i+1}', f'Compute{c}')
    rename_likert(f'data_proj_changes_{i+1}', f'Data{c}')
    rename_likert(f'researcher_proj_chan_{i+1}', f'Researcher{c}')

for i, c in enumerate(['Data', 'Compute', 'Algorithms', 'Researchers', 'Support']):
    rename_likert(f'past_AI_progress_{i+1}', f'Past{c}')
    rename_likert(f'future_AI_factors_{i+1}', f'Future{c}')

rename_likert('relative_comp_needed', 'NeedChanges')
rename_likert('relative_comp_access', 'AccessChanges')
rename_likert('contribution_concern', 'ContributionConcern')

for i, c in enumerate(['Salary', 'Data', 'Compute', 'Projects', 'Contribution']):
    rename_likert(f'acad_leaving_factors_{i+1}', f'Leaving{c}')


# Save the results to a new .csv file (not in a public directory)
df.to_csv('../../Private/data_cleaned.csv', index = False)


# Make a table counting the number of respondents in each (sector, field) combination
data = np.zeros((3, len(df.columns[15:70])), 'i')
for i, s in enumerate(['Academia', 'Industry', 'Government']):
    for j, f in enumerate(df.columns[15:70]):
        data[i,j] = df[df.Sector == s][f].sum()

# Convert this table to a dataframe and save it
data = pd.DataFrame({'Academia': data[0, :], 'Industry': data[1, :], 'Government': data[2, :], 'Total': np.sum(data, axis=0),

# Include columns indicating the percentage of each field composed of each sector
                    'PctAcad': (data[0, :] / np.sum(data, axis=0)).round(2),
                    'PctInd': (data[1, :] / np.sum(data, axis=0)).round(2),
                    'PctGov': (data[2, :] / np.sum(data, axis=0)).round(2),

# Include columns indicating the difference (in percentage points) between the expected composition and the actual composition
                    'PctAcadDiff': (data[0, :] / np.sum(data, axis=0) - 311/448).round(2),
                    'PctIndDiff': (data[1, :] / np.sum(data, axis=0) - 121/448).round(2),
                    'PctGovDiff': (data[2, :] / np.sum(data, axis=0) - 15/448).round(2)},
                    index = df.columns[15:70])

# Save the dataframe
data.to_csv('../data/field_composition.csv')


# Finally, generate some synthetic, randomly sampled data to include in the GitHub repo
synthetic_data = {}
for c in df.columns[4:]:
    synthetic_data[c] = df[c].sample(n=30).tolist()
synth_df = pd.DataFrame(synthetic_data)
synth_df.to_csv('../data/synthetic_data.csv', index = False)
