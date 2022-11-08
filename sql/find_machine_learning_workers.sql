SELECT
  MIN(user.firstname),
  MIN(user.lastname),
  MIN(position.title),
  user.user_li_url AS url
FROM
  gcp_cset_revelio.user
JOIN
  gcp_cset_revelio.position
ON
  user.user_id = position.user_id
WHERE
-- We want anyone whose position is very specifically related to machine learning or artificial intelligence, because
-- we are not limiting by company at all, so these employees could work anywhere at all
  (REGEXP_CONTAINS(position.title, r'(?i)machine learning.+(engineer|architect|analyst|lead)')
    OR REGEXP_CONTAINS(position.title, r'(?i)(artificial intelligence|(^|\s)ai)\s.*(engineer|architect|analyst|lead)'))
  AND user.country = 'United States'
  -- We're sampling down a bit for a few reasons
  -- We can't get every possible person because we don't get emails automatically/for free from this data
  -- We have to either find them manually (slow and expensive) or pay for them (expensive and unreliable)
  -- Given this, we want to somewhat match the size of our startup sample so we ensure our final sample has
  -- a reasonable number of employees from small companies (since this query makes no distinction on company size).
  AND RAND() < 0.35
GROUP BY
  url
