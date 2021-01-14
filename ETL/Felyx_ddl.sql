CREATE TABLE dbo.location (
	sr_no INT
	,id INT
	,wgs84_polygon NVARCHAR(1000)
	)

CREATE TABLE dbo.reservation (
	sr_no INT
	,id INT
	,customer_id INT
	,start_latitude NVARCHAR(1000)
	,start_longitude NVARCHAR(1000)
	,srid INT
	,net_price DECIMAL(5, 2)
	)


select * from dbo.location
select * from dbo.reservation