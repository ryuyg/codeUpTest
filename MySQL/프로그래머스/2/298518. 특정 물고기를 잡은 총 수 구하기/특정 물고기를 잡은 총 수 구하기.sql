-- 코드를 작성해주세요
select count(*) as FISH_COUNT
from FISH_INFO i
join FISH_NAME_INFO n
on n.FISH_TYPE = i.FISH_TYPE
where n.FISH_NAME = 'BASS' or n.FISH_NAME = 'SNAPPER'
