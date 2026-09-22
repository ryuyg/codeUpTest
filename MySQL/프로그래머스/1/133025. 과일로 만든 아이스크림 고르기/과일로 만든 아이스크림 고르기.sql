-- 코드를 입력하세요
SELECT i.FLAVOR
from FIRST_HALF f
JOIN ICECREAM_INFO i
ON i.FLAVOR = f.FLAVOR
where  i.INGREDIENT_TYPE = 'fruit_based' and f.TOTAL_ORDER > 3000 
order by f.TOTAL_ORDER desc;