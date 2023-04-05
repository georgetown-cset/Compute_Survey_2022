# Interpreting Data Results

### `fake_data.csv`

The file `fake_data.csv` contains 30 rows of randomly shuffled data, which is included in this repository so that the reader can visualize the data structure and layout of the primary data file after preprocessing. This is meant to provide an aid to the reader who is interested in working through the analysis presented in `codebook.ipynb`, but it is important to emphasize that to generate this file, 30 answers were randomly selected from each column at random. This in effect destroys the relationships between the columns (e.g. some questions may not have been asked to people who provided specific answers at earlier stages, but this is not taken account of in the random generation process). The secondary purpose of including this fake data is for the reader to visually assess the rough proportion of null values in different columns (where a cell may be null because a respondent only partially completed the survey, skipped the relevant question, or was not presented the relevant question due to a previous response). 

### Field Names

This README file explains the meaning of each column in the primary data file produced by the preprocessing steps at the start of `codebook.ipynb`, of which there are 125. Fifty-five of these columns are binary variables that indicate whether a respondent identified as a researcher working in different fields or subfields within AI. These fields are as follows (names are Pascal Case versions of the exact text shown to respondents):

```
CV [Computer Vision]
├── ImageRecognition
├── SaliencyDetection
├── ObjectTrackingAndOrReIdentification
├── FacialRecognition
├── AutonomousVehicles
├── ImageOrVideoGeneration
├── CaptioningAndSummarization
├── Reconstruction
└── CVOther

Robotics
├── Localization
├── Mapping
├── Manipulation
├── SimultaneousLocalizationAndMappingSlam
├── Navigation
├── AutonomousDriving
├── RobotPerception
├── ContinuousControl
└── RobotOther

NLP [Natural Language Processing]
├── CommonSenseInference
├── ComputerVisionAndNlp
├── CrossLingualTasks
├── Dialogue
├── InformationExtraction
├── LanguageAndKnowledgeBases
├── LanguageModeling
├── MachineTranslation
├── NamedEntityRecognition
├── OpticalCharacterRecognitionOcr
├── NLPOther
├── PartOfSpeechTagging
├── QuestionAnswering
├── SentimentAnalysis
├── Summarization
├── TextClassification
└── TextGeneration

RL [Reinforcement Learning]
├── ProgramLearning
├── EnvironmentsWithLanguage
├── ProcedurallyGeneratedEnvironments
├── GamePlaying
├── 3DWorlds
├── RLOther
└── SimulationDesign

Other
├── RecommenderSystems
├── Speech
├── TimeSeriesData
├── MusicAndAudio
├── GraphAnalysis
├── AlgorithmicOrArchitectureAnalysis
└── NoneOfThese
```

It is important to emphasize that, for all subfields, respondents were **only** given the option to indicate that they worked on that subfield if they first indicated that they worked in the field in which that subfield was located. Note also that many subfields are highly similar, e.g. because some subfields (autonomous vehicles, image captioning, optical character recognition) cross multiple level-one fields. This taxonomy of AI fields was adapted from Stateoftheart AI (https://www.stateoftheart.ai/datasets) and further adjusted during the course of cognitive interviews.

### Column Meanings

The columns used in the final data file and their meanings are as follows:

```
DistributionChannel       <- 'email' or 'anonymous'; whether the respondent was reached by a targeted email or via snowball sampling—not present in `fake_data.csv`
Screener                  <- Numerical ordinal [0,3]; how much time respondent spends working on AI systems (see INSTRUMENT.pdf for meanings)
Tenure                    <- Numerical ordinal [0,2]: how long respondent has worked in AI (see INSTRUMENT.pdf for meanings)
TimeManaging              <- Numerical ordinal [0,3]: what percent of respondent's time is spent managing compute resources (see INSTRUMENT.pdf for meanings; blank if skipped)
CloudUser                 <- 0 or 1; whether the respondent used cloud compute in the previous year (blank if question skipped)
OnPremise                 <- 0 or 1; whether the respondent used on-premise compute in the previous year (blank if question skipped)
LocationUnk               <— 0 or 1; whether the respondent answered "I don't know" about compute location (blank if question skipped) 
UsedFree                  <- 0 or 1; whether the respondent used free compute in the previous year (blank if question skipped)
UsedPersonal              <- 0 or 1; whether the respondent used personal funds to pay for compute in the previous year (blank if skipped)
UsedGrants 		          <— 0 or 1; whether the respondent used grants to pay for compute in the previous year (blank if skipped) 
EmployerPaid              <- 0 or 1; whether the respondent's employer paid for compute in the previous year (blank if skipped)
PaymentUnk                <— 0 or 1; whether the respondent answered "I don't know" about the source of funding for compute (blank if skipped)
PersonalCost              <- Numerical ordinal [0,4]; if UsedPersonal == 1, how much money they spent (see INSTRUMENT.pdf for meanings; blank if skipped)
MultipleProcessors        <- Numerical ordinal [0,3]; the number of processors that the respondent typically uses for an AI project (see INSTRUMENT.pdf for meanings; blank if skipped)
NoSigProject              <- 1 if the respondent answered 'N/A' when asked to think about a significant project else blank
{Sig,Comp}TeamSize        <- Numerical ordinal [0,4]; the size of the team for respondent's most significant or most compute-intensive project (see INSTRUMENT.pdf for meanings; blank if skipped)
{Sig,Comp}Year            <- Numerical ordinal [0,6]; the year in which respondent's most significant or most compute-intensive project was completed (see INSTRUMENT.pdf for meanings; blank if skipped)
{Sig,Comp}Component       <— Numerical categorical; the component of respondent's most significnt or most compute-intensive project that required the most compute (see INSTRUMENT.pdf for meanings; blank if skipped)
{Sig,Comp}Cost            <- Numerical ordinal [0,5]; the compute cost of respondent's most significant or most compute-intensive project in dollars (see INSTRUMENT.pdf for meanings; blank if skipped)
{Sig,Comp}GPUs            <- Numerical ordinal [0,6]; the compute cost of respondent's most significant or most compute-intensive project in GPU-hours (see INSTRUMENT.pdf for meanings; blank if skipped)
Success{Data,TeamSize,Talent,Compute}                         <- Numerical ordinal [0,4]; how important each factor was to the success of respondent's most significant project (blank if skipped or not shown)
SameProject               <- 0, 1, or blank; whether the respondent's most significant project was also their most compute-intensive one (blank if 'N/A' selected for most significant project or if question skipped)
TopPriority               <- Text categorical; the plain text of the selected response for respondent's top priority if most recent project budget were doubled (blank if skipped)
{Need,Access}Changes      <- Numerical ordinal [0,4]; how much compute the respondent reports needing or having access to, relative to two years ago (blank if skipped)
{Compute,Data,Researcher}{Reject,Revise,Abandon}              <- Numerical ordinal [0,4]; how frequently the researcher rejected, revised, or abandoned projects due to lack of compute, data, or researcher availability (blank if skipped)
{Past,Future}{Data,Compute,Algorithms,Researchers,Support}    <- Numerical ordinal [0,4]; how strongly the researcher agrees that each factor either contributed or will contribute to AI progress (blank if skipped)
ContributionConcern       <- Numerical ordinal [0,4]; respondent's concern that a lack of compute resources will be an obstacle to their AI contributions over the next decade (blank if skipped)
WantsData                 <- 0 or 1; whether the respondent indicated that NAIRR-provided data resources would be useful (blank if skipped)
WantsCompute              <- 0 or 1; whether the respondent indicated that NAIRR-provided compute resources would be useful (blnak if skipped)
WantsStaff                <- 0 or 1; whether the respondent indicated that NAIRR-provided technical staff would be useful (blank if skipped)
WantsGrants               <- 0 or 1; whether the respondent indicated that NAIRR-provided grant funding would be useful (blank if skipped)
WantsStandards            <- 0 or 1; whether the respondent indicated that NAIRR-provided guidelines, standards, and frameworks would be useful (blank if skipped)
Sector                    <- Text categorical; the sector in which respondent works (blank if skipped)
ConsideredLeaving         <- 0, 1, or blank; whether the respondent considered leaving academia to work in industry (blank if not shown or skipped)
Leaving{Salary,Data,Compute,Projects,Contribution}            <- Numerical ordinal [0,4]; how important each factor was in making an academic consider leaving academia (blank if skipped)
CompanySize               <– Text categorical; the plain text of the selected response for the respondent's organization size (blank if skipped or not shown)
Education                 <— Numerical ordinal [0,6]; respondent's reported level of education (see INSTRUMENT.pdf for meanings)
CV ... NoneOfThese        <- 55 columns; 0 or 1 for each; whether the respondent indicated working in this subfield (0 if skipped)
PrioritySimplified        <- Text categorical; responses to TopPriority binned into simpler categories of "Data", "Compute", "Talent", and "Evaluation"
```


### `field_composition.csv`

This folder also contains a file named `field_composition.csv`. The notebook `codebook.ipynb` takes a dataset consisting of all screened responses from an external directory, reformats it to align with the layout described above, and saves it to the same external directory. It also generates a summary table about the demographics of respondents called `field_composition.csv`. This .csv file contains, for each field, 10 columns: The first four are raw counts for the total number of respondents identifying as working in that field, as well as the number from academia, industry, and government respectively. The next three fields contain the percentage of respondents in the field from each sector. The final three fields contain the difference in percentage points between the actual composition of the field and the expected composition of the field (assuming perfectly proportional representation in each field) for each sector. 
