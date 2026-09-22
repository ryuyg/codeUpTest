-- 코드를 입력하세요
SELECT BOOK_ID, PUBLISHED_DATE
from BOOK 
where category = '인문' and year(PUBLISHED_DATE) = 2021
order by PUBLISHED_DATE asc;