-- Select all merged_ids for the relevant conferences and journals
create or replace table compute_survey.conference_emails as
WITH
  conference_papers AS (
  SELECT
    DISTINCT merged_id
  FROM
    gcp_cset_links_v2.paper_sources_merged
  WHERE
    -- The list of top conferences and journals (see paper for explanation of derivation). Regular expressions selected using DBLP to find all possibilities, and evaluating results produced to avoid false positives.
    REGEXP_CONTAINS(source_name, r'(?i)AAAI Conference on Artificial Intelligence')
    OR REGEXP_CONTAINS(source_name, r'(?i)\(AAAI-')
    OR (REGEXP_CONTAINS(source_name, r'(?i)International Joint Conference on Artificial Intelligence')
      OR REGEXP_CONTAINS(source_name, r'(?i)IJCAI'))
    AND NOT REGEXP_CONTAINS(source_name, r'(?i)Multimedia for Cooking and Eating Activities')
    OR REGEXP_CONTAINS(source_name, r'(?i)IEEE Conference on Computer Vision and Pattern Recognition')
    OR REGEXP_CONTAINS(source_name, r'(?i)\bCVPR')
    AND NOT REGEXP_CONTAINS(source_name, r'(?i)旷视科技征战')
    OR REGEXP_CONTAINS(source_name, r'(?i)European Conference on Computer Vision')
    OR REGEXP_CONTAINS(source_name, r'(?i)ECCV ')
    OR REGEXP_CONTAINS(source_name, r'(?i)IEEE.*International Conference on Computer Vision')
    OR REGEXP_CONTAINS(source_name, r'(?i)ICCV\b')
    OR (REGEXP_CONTAINS(source_name, r'(?i)International Conference on Machine Learning')
      AND NOT REGEXP_CONTAINS(source_name, r'(?i)(and)|(technologies)|(cybernetics)'))
    OR (REGEXP_CONTAINS(source_name, r'(?i)\bICML\b')
      AND NOT REGEXP_CONTAINS(source_name, r'(?i)(medical|lugano)'))
    OR REGEXP_CONTAINS(source_name, r'(?i)International Conference on Knowledge Discovery [a|\&]n?d? Data Mining')
    OR REGEXP_CONTAINS(source_name, r'(?i)SIGKDD')
    OR REGEXP_CONTAINS(source_name, r'(?i)Neural Information Processing Systems')
    OR REGEXP_CONTAINS(source_name, r'(?i)\bNeurIPS\b')
    OR REGEXP_CONTAINS(source_name, r'(?i)Annual Meeting of the Association for Computational Linguistics')
    OR ( REGEXP_CONTAINS(source_name, r'\bACL\b')
      AND conference = 1
      AND NOT REGEXP_CONTAINS(source_name, r'(?i)(injur)|(special interest)|(coling)'))
    OR REGEXP_CONTAINS(source_name, r'(?i)North American Chapter of the Association for Computational Linguistics')
    OR REGEXP_CONTAINS(source_name, r'(?i)\bNAACL\b')
    OR REGEXP_CONTAINS(source_name, r'(?i)Conference on Empirical Methods in Natural Language Processing')
    OR REGEXP_CONTAINS(source_name, r'(?i)\bEMNLP\b')
    OR REGEXP_CONTAINS(source_name, r'(?i)International Conference on Learning Representations')
    OR REGEXP_CONTAINS(source_name, r'(?i)\bTransactions On Systems.? Man And Cybernetics Part B')
    OR REGEXP_CONTAINS(source_name, r'(?i)\bTransactions on Neural Networks and Learning Systems')
    OR REGEXP_CONTAINS(source_name, r'(?i)^Neurocomputing$')
    OR REGEXP_CONTAINS(source_name, r'(?i)\bExpert Systems with Applications')
    OR (REGEXP_CONTAINS(source_name, r'(?i)\bApplied Soft Computing')
      AND NOT REGEXP_CONTAINS(source_name, r'(?i)\btechnologies'))
    OR REGEXP_CONTAINS(source_name, r'(?i)\bTransactions on Pattern Analysis and Machine Intelligence')
    OR REGEXP_CONTAINS(source_name, r'(?i)\bIEEE Transactions on Image Processing')
    OR ((REGEXP_CONTAINS(source_name, r'(?i)\bInternational Conference on Robotics and Automation')
        OR REGEXP_CONTAINS(source_name, r'(?i)\bICRA\b'))
      AND NOT REGEXP_CONTAINS(source_name, r'(?i)((\bRAHA\b)|(\bICRAS\b)|(\bICRAE\b)|(\bICRAI\b)|(\bRoboMaster\b)|(Radiations))'))),
-- Get the WOS ids for any of them that are in WOS
-- We use WOS because it is a datasource that provides email addresses along with paper data
  wos_papers AS (
  SELECT
    orig_id
  FROM
    conference_papers
  LEFT JOIN
    gcp_cset_links_v2.article_links
  USING
    (merged_id)
  WHERE
    REGEXP_CONTAINS(orig_id, r'WOS:')),
-- Get country data for all WOS papers we care about; only select the papers that have country data from USA
-- Also select the addr_ids for any paper with country = USA, as this will let us link to authors with those addr_ids
-- which theoretically should be the US authors (in the case of coauthors)
  wos_countries AS (
  SELECT
    DISTINCT orig_id,
    addr_id AS address_id,
    country
  FROM
    wos_papers
  LEFT JOIN
    gcp_cset_clarivate.wos_addresses_latest
  ON
    orig_id = id
  WHERE
    country = "USA"),
-- Link these to emails and organization names
-- WOS has a ton of duplicate organization names. We aren't going to try to clean these all up.
-- However, one of the most common problems is duplicating University and Univ for the same org; we'll clean that up.
  email_org AS (
  SELECT
    DISTINCT orig_id,
    email_addr,
    first_name,
    last_name,
    REGEXP_REPLACE(organization, r'(?i)\bUniv\b', 'University') AS organization
  FROM
    wos_countries
  LEFT JOIN
    gcp_cset_clarivate.wos_address_names_email_addr_latest email
  ON
    orig_id = email.id
    AND address_id = email.addr_id
  LEFT JOIN
    gcp_cset_clarivate.wos_address_organizations_latest orgs
  ON
    orig_id = orgs.id
    AND address_id = orgs.addr_id
  LEFT JOIN
    gcp_cset_clarivate.wos_address_names_latest names
  ON
    orig_id = names.id
    AND address_id = names.addr_id
    AND email.name_id = names.name_id
  WHERE
    email_addr IS NOT NULL
  ORDER BY
    orig_id)
-- Distinct our email addresses, and group our organizations. 
-- Since these are the organizations of individuals, ideally most of the time there will be just one and all the duplicates will just be name variants
-- Also limit our selection to the years 2016-2021, as we said we would
SELECT
  DISTINCT email_addr,
  MAX(first_name) AS first_name,
  MAX(last_name) AS last_name,
  STRING_AGG(DISTINCT organization, "; ") AS organization,
  MAX(CAST(pubyear AS INT64)) as most_recent_year
FROM
  email_org
LEFT JOIN
  gcp_cset_clarivate.cset_wos_id_pubyear_times_cited
ON
  orig_id = id
WHERE
  CAST(pubyear AS INT64) >= 2016
  AND CAST(pubyear AS INT64) < 2022
GROUP BY
  email_addr
