--1) Listar os nomes e cidades de todos os clientes em uma só consulta
SELECT 
	c.nome,
	c.cidade 
FROM 
	Clientes c;

--2) Listar os pedidos com valor acima de R$100
SELECT
	*
FROM
	Pedidos p 
WHERE
	p.valor > 100;

--3) Listar os pedidos ordenados pelo valor (decrescente)
SELECT
	*
FROM
	Pedidos p 
ORDER BY
	p.valor DESC;
	
--4) Listar os 3 primeiros produtos cadastrados
SELECT
	*
FROM
	Produtos p 
LIMIT 3;

--5) Listar o total de valor gasto por cada cliente em pedidos.
SELECT
	c.nome As 'Cliente',
	SUM(p.valor) AS 'Total valor gasto'
FROM
	Pedidos p LEFT JOIN Clientes c ON c.id_cliente = p.id_cliente
GROUP BY
	c.nome;
	
--6) Encontrar o cliente com o maior valor gasto
SELECT
	sub_tabela.Cliente,
	MAX(sub_tabela.Total) AS 'maior valor gasto'
FROM 
	(SELECT c.nome As 'Cliente', SUM(p.valor) AS 'Total' FROM Pedidos p LEFT JOIN Clientes c ON c.id_cliente = p.id_cliente GROUP BY c.nome) sub_tabela;

--7) Utilizar CTE para calcular o total de vendas por produto	
WITH cte AS
(SELECT 
	p.nome_produto, 
	SUM(ip.quantidade) as qtde, 
	p.preco  
FROM 
	Produtos p INNER JOIN ItensPedido ip ON ip.id_produto = p.id_produto 
GROUP BY 
	p.nome_produto)
SELECT cte.nome_produto, (cte.qtde * cte.preco) 'total de vendas' FROM cte;

--8) Listar todos os produtos comprados por cada cliente  
SELECT 
	c.nome,
	GROUP_CONCAT(pr.nome_produto, ', ') AS 'Produtos comprados'
FROM 
	Pedidos p 
	INNER JOIN ItensPedido ip ON ip.id_pedido = p.id_pedido 
	INNER JOIN Produtos pr ON pr.id_produto = ip.id_produto
	INNER JOIN Clientes c ON c.id_cliente  = p.id_cliente
GROUP BY 
	c.nome;

--9) Ranquear clientes pelo valor total gasto começando pelo rank 1 para o maior valor.
SELECT
	RANK() OVER (ORDER BY SUM(p.valor) DESC) ranque,
	c.nome As 'Cliente',
	SUM(p.valor) AS 'Total_gasto'
FROM
	Pedidos p LEFT JOIN Clientes c ON c.id_cliente = p.id_cliente
GROUP BY
	c.nome
ORDER BY 
	Total_gasto DESC;
	
--10) Número de pedidos por cliente, considerando apenas aqueles com mais de 1 pedido
SELECT 
	c.nome,
	COUNT(p.id_pedido) AS qtde_pedido
FROM 
	Pedidos p INNER JOIN Clientes c ON c.id_cliente = p.id_cliente
GROUP BY
	c.nome
HAVING
	qtde_pedido > 1;
	
--11) Calcular para cada cliente a quantidade de dias entre um pedido e o pedido imediatamente anterior 
WITH cte1 AS (
SELECT 
    p.id_cliente,
    p.data_pedido,
    p.id_pedido,
    LAG(p.data_pedido) OVER (PARTITION BY p.id_cliente ORDER BY p.data_pedido) AS data_anterior
FROM 
	Pedidos p)
SELECT 
	c.nome, 
	ct.id_pedido,
 	CAST((JulianDay(ct.data_pedido) - JulianDay(ct.data_anterior)) AS Integer) AS dif_datas_dias
 FROM 
 	Clientes c INNER JOIN cte1 ct ON c.id_cliente = ct.id_cliente;

--12)Crie uma consulta que retorne um relatórios contedo as seguintes colunas (obs: use o padrão que preferir para nomear as colunas):
    -- ID do cliente 
    -- Nome do cliente
    -- Cidade do cliente 
    -- ID do pedido 
    -- Data do pedido 
    -- Valor do pedido 
    -- Preço do pedido sem desconto (pode ser recuperado somando a coluna "preço" de cada produto dentro do pedido)
    -- Quantidade de dias entre o pedido e seu pedido imediatamente anterior
WITH cte1 AS (
SELECT 
    p.id_cliente,
    p.data_pedido,
    p.id_pedido,
    p.valor,
    LAG(p.data_pedido) OVER (PARTITION BY p.id_cliente ORDER BY p.data_pedido) AS data_anterior
FROM 
	Pedidos p)
SELECT
	c.id_cliente AS 'ID do cliente',
	c.nome AS 'Nome do cliente',
	c.cidade AS 'Cidade do cliente',
	ct.id_pedido AS 'ID do pedido',
	ct.data_pedido AS 'Data do pedido',
	ct.valor AS 'Valor do pedido',
	(SELECT SUM(pr.preco) FROM Produtos pr INNER JOIN ItensPedido ip ON ip.id_produto = pr.id_produto INNER JOIN Pedidos p ON p.id_pedido  = ip.id_pedido WHERE p.id_pedido = ct.id_pedido GROUP BY p.id_pedido) AS 'Preço do pedido sem desconto',
 	CAST((JulianDay(ct.data_pedido) - JulianDay(ct.data_anterior)) AS Integer) AS 'Quantidade de dias'
 FROM 
 	Clientes c INNER JOIN cte1 ct ON c.id_cliente = ct.id_cliente;
