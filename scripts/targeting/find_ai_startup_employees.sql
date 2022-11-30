WITH
  companies_to_check AS (
  SELECT
    DISTINCT company_name
  FROM
  -- using a list of US AI startups from CBInsights
    compute_survey.cbinsights_ai_startups),
  -- Our data source calls some of the startups different names than CBInsights does
  -- A lot of thems this is because they are x company name dba y company name
  -- So we swap the names here
  companies_in_revelio AS (
  SELECT
    DISTINCT REPLACE(REPLACE(REPLACE(COALESCE(company,
            company_raw), "Express Lien, Inc.", "Levelset"), "Fancy Chap, Inc.", "Flywheel"), "The Start Exchange, Inc.", "The Innovation Scout") AS company,
    user_id,
    title
  FROM
    gcp_cset_revelio.position
  INNER JOIN
    companies_to_check
  ON
  -- There are two company name fields in our data source; we're happy to link on either
    (LOWER(company_raw) = LOWER(company_name)
      OR LOWER(company) = LOWER(company_name))),
  company_users AS (
  SELECT
    DISTINCT company,
    user_id,
    title
  FROM
    companies_in_revelio
  WHERE
  -- Since we know everyone at our startups works at an AI startup company, we're a bit more flexible with our job titles than we are in our query
  -- where we look just for machine learning engineers and similar; there are less likely to be lots of non-AI tech employees at an AI startup
  -- We also screen everyone in the survey to be sure they actually do AI, so if we email a few people who don't it's not the end of the world
    REGEXP_CONTAINS(title, r'(?i)((analytics)|(r.?d)|(research\s+.?\s+development)|(research\s+and\s+development))\s+specialist')
    OR REGEXP_CONTAINS(title, r'(?i)((cloud)|(infrastructure))\s+architect')
    OR REGEXP_CONTAINS(title, r'(?i)((analyst\s+)|(statistical\s+))?programmer')
    OR REGEXP_CONTAINS(title, r'(?i)technical\s+((architect)|(lead)|(product\s+manager)|(project\s+manager))')
    OR REGEXP_CONTAINS(title, r'(?i)((information)|(infrastructure)|(programmer)|(quantitative))\s+analyst')
    OR REGEXP_CONTAINS(title, r'(?i)((etl\s+)|(full\s+stack\s+)|(java\s+)|(software\s+))?developer')
    OR REGEXP_CONTAINS(title, r'(?i)data\s+((analyst)|(analytics)|(architect)|(center\s+operator)|(scientist))')
    OR REGEXP_CONTAINS(title, r'(?i)((automation)|(data)|(development)|(machine\s+learning)|(infrastructure)|(software)|(r.?d)|(research\s+.?\s+development)|(research\s+and\s+development))\s+engineer')
    OR REGEXP_CONTAINS(title, r'(?i)((advisory\s+software\s+engineer)|(researcher)|(scientist)|(sde)|(software\s+designer)|(statistician)|(technology\s+lead))') )
SELECT
  DISTINCT company,
  title,
  firstname,
  lastname,
  user_li_url,
  country
FROM
  company_users
INNER JOIN
  gcp_cset_revelio.user
USING
  (user_id)
WHERE
  country = "United States"
