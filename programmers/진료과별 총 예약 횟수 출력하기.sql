SELECT MCDP_CD 진료과코드, COUNT(MCDP_CD) 5월예약건수 FROM APPOINTMENT WHERE APNT_YMD BETWEEN DATE('2022-05-01') AND DATE('2022-05-31') GROUP BY MCDP_CD ORDER BY COUNT(MCDP_CD), MCDP_CD;