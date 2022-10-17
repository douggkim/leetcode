# Write your MySQL query statement below
SELECT E.left_operand, E.operator, E.right_operand, (CASE (CASE WHEN E.operator='<' THEN V1.value-V2.value<0 WHEN E.operator='>' THEN V1.value-V2.value>0 ELSE V1.value-V2.value=0 END) WHEN 1 THEN 'true' ELSE 'false' END) AS value
FROM Expressions E
INNER JOIN Variables V1
ON V1.name = E.left_operand 
INNER JOIN Variables V2 
ON V2.name = E.right_operand 




