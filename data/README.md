# Interpreting Data Results

This folder contains three files: a `synthetic_data.csv`, which contains fake data in the same layout as our final, real cleaned dataset, `answer_key.csv`, which is used to interpret some of the results, and `field_composition.csv`, which shows the breakdown by sector for each field and subfield. The synthetic data was randomly generated by independently sampling each column of our final cleaned dataset; in some places this generates impossible results (e.g. someone who does not identify as an academic would not be shown questions about reasons for considering leaving academia, but our random sampling ignores this restriction). This file is provided to 1) understand the layout of data and 2) provide readers with a very rough sense of the general distribution and missingness of each question.

### Field Names

This README file explains the meaning of each column in the `synthetic_data.csv` file, of which there are 125. Fifty-five of these columns are binary variables that indicate whether a respondent identified as a researcher working in different fields or subfields within AI. These fields are as follows (names are Pascal Case versions of the exact text shown to respondents, with each Pascal Case version being a column title in `synthetic_data.csv`):

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

A breakdown of the total number of researchers in our sample working in each of these fields from industry and academia is provided in `fields_breakdown.csv`.

### Column Meanings in `synthetic_data.csv`

The meanings of each column in `synthetic_data.csv` are as follows:

```
DistributionChannel       <- 'email' or 'anonymous'; whether the respondent was reached by a targeted email or via snowball sampling
CloudUser                 <- 0 or 1; whether the respondent used cloud compute in the previous year (0 if question skipped)
OnPremise                 <- 0 or 1; whether the respondent used on-premise compute in the previous year (0 if question skipped)
UsedFree                  <- 0 or 1; whether the respondent used free compute in the previous year (0 if question skipped)
UsedPersonal              <- 0 or 1; whether the respondent used personal funds to pay for compute in the previous year (0 if skipped)
EmployerPaid              <- 0 or 1; whether the respondent's employer paid for compute in the previous year (0 if skipped)
WantsData                 <- 0 or 1; whether the respondent indicated that NAIRR-provided data resources would be useful (0 if skipped)
WantsCompute              <- 0 or 1; whether the respondent indicated that NAIRR-provided compute resources would be useful (0 if skipped)
WantsStaff                <- 0 or 1; whether the respondent indicated that NAIRR-provided technical staff would be useful (0 if skipped)
WantsGrants               <- 0 or 1; whether the respondent indicated that NAIRR-provided grant funding would be useful (0 if skipped)
WantsStandards            <- 0 or 1; whether the respondent indicated that NAIRR-provided guidelines, standards, and frameworks would be useful (0 if skipped)
CV ... NoneOfThese        <- 55 columns; 0 or 1 for each; whether the respondent indicated working in this subfield (0 if skipped)
NoSigProject              <- 0 or 1; whether the respondent answered 'N/A' when asked to think about a significant project
SigComponent              <- Text categorical; the component of respondent's most significant project that was indicated as requiring the most compute (blank if skipped)
CompComponent             <- Text categorical; the component of respondent's most compute-intensive project that was indicated as requiring the most compute (blank if skipped)
TopPriority               <- Text categorical; the plain text of the selected response for respondent's top priority if most recent project budget were doubled (blank if skipped)
PrioritySimplified        <- Text categorical; responses to TopPriority binned into simpler categories of "Data", "Compute", "Talent", and "Evaluation"
Sector                    <- Text categorical; the sector in which respondent works (blank if skipped)
ConsideredLeaving         <- 0, 1, or blank; whether the respondent considered leaving academia to work in industry (blank if not shown or skipped)
SameProject               <- 0, 1, or blank; whether the respondent's most significant project was also their most compute-intensive one (blank if 'N/A' selected for most significant project or if question skipped)
LargeCompany              <- 0, 1, or blank; whether the respondent works at a company over 500 employees (1) or under 500 employees (0) (blank if not in industry or skipped)
HasPhD                    <- 0, 1, or blank; whether the respondent has a PhD or some lower level of education (blank if skipped)
Screener                  <- Numerical ordinal [0,3]; how much time respondent spends working on AI systems (see answer_key.csv for meanings)
Tenure                    <- Numerical ordinal [0,2]: how long respondent has worked in AI (see answer_key.csv for meanings)
TimeManaging              <- Numerical ordinal [0,3]: what percent of respondent's time is spent managing compute resources (see answer_key.csv for meanings; blank if skipped)
PersonalCost              <- Numerical ordinal [0,4]; if respondent paid for compute using personal money in the previous year, how much money they spent (see answer_key.csv for meanings; blank if skipped)
MultipleProcessors        <- Numerical ordinal [0,3]; the number of processors that the respondent typically uses for an AI project (see answer_key.csv for meanings; blank if skipped)
{Sig,Comp}TeamSize        <- Numerical ordinal [0,4]; the size of the team for respondent's most significant or most compute-intensive project (see answer_key.csv for meanings; blank if skipped)
{Sig,Comp}Year            <- Numerical ordinal [0,6]; the year in which respondent's most significant or most compute-intensive project was completed (see answer_key.csv for meanings; blank if skipped)
{Sig,Comp}Cost            <- Numerical ordinal [0,5]; the compute cost of respondent's most significant or most compute-intensive project in dollars (see answer_key.csv for meanings; blank if skipped)
{Sig,Comp}GPUs            <- Numerical ordinal [0,6]; the compute cost of respondent's most significant or most compute-intensive project in GPU-hours (see answer_key.csv for meanings; blank if skipped)
Success{Data,TeamSize,Talent,Compute}                         <- Numerical ordinal [0,4]; how important each factor was to the success of respondent's most significant project (0 = Not at all important, 4 = Extremely important, blank if skipped or not shown)
{Compute,Data,Researcher}{Reject,Revise,Abandon}              <- Numerical ordinal [0,4]; how frequently the researcher rejected, revised, or abandoned projects due to lack of compute, data, or researcher availability (0 = Never, 4 = All the time, blank if skipped)
{Past,Future}{Data,Compute,Algorithms,Researchers,Support}    <- Numerical ordinal [0,4]; how strongly the researcher agrees that each factor either contributed or will contribute to AI progress (0 = Strongly disagree, 4 = Strongly agree, blank if skipped)
{Need,Access}Changes                                          <- Numerical ordinal [0,4]; how much compute the respondent reports needing or having access to, relative to two years ago (0 = Much less, 4 = Much more, blank if skipped)
ContributionConcern                                           <- Numerical ordinal [0,4]; respondent's concern that a lack of compute resources will be an obstacle to their AI contributions over the next decade (0 = Not at all concerned, 4 = Extremely concerned, blank if skipped)
Leaving{Salary,Data,Compute,Projects,Contribution}            <- Numerical ordinal [0,4]; how important each factor was in making an academic consider leaving academia (0 = Not at all important, 4 = Extremely important, blank if skipped)
```


### `field_composition.csv`

The script `data_cleaner.py` takes a dataset consisting of all screened responses from an external directory, reformats it to align with the layout of `synthetic_data.csv`, and saves it to the same external directory. It also randomly samples columns to produce `synthetic_data.csv` and generates a summary table about the demographics of respondents called `field_composition.csv`. This .csv file contains, for each field, 10 columns: The first four are raw counts for the total number of respondents identifying as working in that field, as well as the number from academia, industry, and government respectively. The next three fields contain the percentage of respondents in the field from each sector. The final three fields contain the difference in percentage points between the actual composition of the field and the expected composition of the field (assuming perfectly proportional representation in each field) for each sector. 