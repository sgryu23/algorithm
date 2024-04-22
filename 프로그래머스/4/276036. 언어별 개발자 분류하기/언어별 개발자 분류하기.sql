WITH FE AS (
    SELECT BIT_OR(CODE) AS SKILL_CODE
    FROM SKILLCODES
    GROUP BY CATEGORY
    HAVING CATEGORY = 'Front End'
), DEV_GRADE AS (
    SELECT
        CASE
            WHEN DEV.SKILL_CODE & FE.SKILL_CODE
                AND DEV.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python')
                    THEN 'A'
            WHEN DEV.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#')
                THEN 'B'
            WHEN DEV.SKILL_CODE & FE.SKILL_CODE
                THEN 'C'
            ELSE NULL
        END AS GRADE
        , ID
        , EMAIL
    FROM DEVELOPERS DEV
    , FE
)

SELECT GRADE, ID, EMAIL
FROM DEV_GRADE
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID