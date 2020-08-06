**1. показать клиентов *(только их полные имена, идентификатор клиента и страну)*, которые не находятся в США.**
```SQL
SELECT 
    FirstName,
    LastName,
    CustomerId,
    Country
FROM Customer
WHERE Country != "USA"
 			--OR
SELECT 
    cus.CustomerID,
    cus.FirstName || ' ' || cus.LastName AS FullName,
    cus.Country 
FROM Customer as cus 
WHERE Country <> "USA";
```
**2. показать только клиентов из США.**
```SQL
SELECT 
    FirstName,
    LastName,
    CustomerId,
    Country
FROM Customer
WHERE Country = "USA"
 			--OR
SELECT 
    cus.CustomerID,
    cus.FirstName || ' ' || cus.LastName AS FullName,
    cus.Country 
FROM Customer as cus 
WHERE Country == "USA";
 ```
**3. показать счета-фактуры клиентов, которые находятся в США.**
<br>*В результирующей таблице должно быть указано полное имя клиента, идентификатор счета, дата выставления счета и страна выставления счета.*
```SQL
SELECT
    c.FirstName || " " || c.LastName AS FullName,
    i.InvoiceId,
    i.InvoiceDate,
    i.BillingCountry
FROM Customer c
INNER JOIN Invoice i  ON c.CustomerId = i.CustomerId
WHERE c.Country = 'USA'
		--or
SELECT 
    cus.FirstName || ' ' || cus.LastName as FullName, 
    inv.InvoiceId,
    inv.InvoiceDate,
    inv.BillingCountry 
FROM Customer as cus 
INNER JOIN Invoice as inv ON cus.CustomerId = inv.CustomerId 
WHERE Country == "USA";
```

**4. Показать только тех сотрудников, которые являются торговыми агентами.**
```SQL
SELECT 
* 
FROM Employee e
WHERE e.Title = "Sales Support Agent"
		--or
SELECT 
    emp.EmployeeId,
    emp.FirstName || ' ' || emp.LastName as FullName,
    emp.Title 
FROM Employee as emp 
WHERE Title == "Sales Support Agent";
```

**5. Уникальный список стран выставления счетов из таблицы счетов - Invoice.**
```SQL
SELECT DISTINCT inv.BillingCountry 
FROM Invoice as inv;
```

**6. Cчета-фактуры, связанные с каждым торговым агентом.**
<br>*Результирующая таблица должна содержать полное имя торгового агента.*
```SQL
SELECT
    e.FirstName || " " || e.LastName AS SalesAgent,
    i.*
FROM Employee e
INNER JOIN Customer c ON e.EmployeeID = c.SupportRepId
INNER JOIN Invoice  i ON c.CustomerId = i.CustomerId
WHERE e.Title = "Sales Support Agent"
ORDER BY SalesAgent
		--or
SELECT 
    emp.FirstName || ' ' || emp.LastName as AssociatedRepName, 
    inv.InvoiceId,
    inv.Total 
FROM Customer as cust 
INNER JOIN Employee as emp ON cust.SupportRepId = emp.EmployeeId 
INNER JOIN Invoice  as inv ON cust.CustomerId = inv.CustomerId 
WHERE Title == "Sales Support Agent";
```
**7. Покажите общую сумму счета, имя клиента, страну и имя агента по продаже для всех счетов-фактур и клиентов.**
```SQL
SELECT
    c.FirstName || " " || c.LastName AS Customer,
    i.Total AS InvoiceTotal,
    i.BillingCountry,
    e.FirstName || " " || e.LastName AS SalesAgent
FROM Employee e
INNER JOIN Customer c ON e.EmployeeID = c.SupportRepId
INNER JOIN Invoice  i ON c.CustomerId = i.CustomerId
WHERE e.Title = "Sales Support Agent"
ORDER BY Customer
```

**8. Сколько счетов было выставлено в 2009 и 2011 годах? Каковы соответствующие суммарные продажи за каждый из этих лет?**
```SQL
SELECT COUNT(*) 
FROM Invoice 
WHERE InvoiceDate 
LIKE '%2009%'
--83 total invoices for 2009.
SELECT COUNT(*) 
FROM Invoice 
WHERE InvoiceDate 
LIKE '%2011%'
--83 total invoices for 2011.
SELECT SUM(Total) AS [2009 Total Sales] 
FROM Invoice 
WHERE InvoiceDate 
LIKE '%2009%'
--449.46 total sales for 2009.
SELECT SUM(Total) AS [2011 Total Sales] 
FROM Invoice 
WHERE InvoiceDate 
LIKE '%2011%'
--469.58 total sales for 2011.

```

**9. Глядя на таблицу InvoiceLine, подсчитайте количество позиций строки для идентификатора счета-фактуры ID 37.**
```SQL
SELECT COUNT(*) 
FROM InvoiceLine 
WHERE InvoiceId = 37
--total of 4 records.
```

**10. Глядя на таблицу InvoiceLine, подсчитaйте количество позиций строки для каждого счета-фактуры.**
```SQL
SELECT
    InvoiceId, 
    COUNT(InvoiceLineId)  AS TotalInvoiceCount
FROM InvoiceLine
GROUP BY InvoiceId
```
**11. Предоставьте запрос, который включает имя трека для каждой строки счета-фактуры.**
```SQL
SELECT il.InvoiceLineId, Track.Name
FROM InvoiceLine AS il
INNER JOIN Track ON Track.TrackId = il.TrackId 
ORDER BY InvoiceLineId
```

**12. Предоставьте запрос, который включает в себя название купленного трека, имя исполнителя для каждого id счета-фактуры.**
```SQL
SELECT
    InvoiceLine.InvoiceLineId, 
    Track.Name  AS [TrackName], 
    Artist.Name AS [ArtistName] 
FROM InvoiceLine 
INNER JOIN Track ON Track.TrackId = InvoiceLine.TrackId
INNER JOIN Album ON Album.AlbumId = Track.AlbumId
INNER JOIN Artist ON Artist.ArtistId = Album.ArtistId 
ORDER BY InvoiceLineId
```

**13. Предоставьте запрос, который показывает количество счетов-фактур в каждой стране.**
```SQL
SELECT 
    Invoice.BillingCountry, 
    COUNT(Invoice.InvoiceId) AS [Total number of Invoices] 
FROM Invoice 
GROUP BY Invoice.BillingCountry
```

 **14. Предоставьте запрос, который показывает общее количество треков в каждом плейлисте**.
<br>*Имя плейлиста должно быть включено в результирующую таблицу.*
```SQL
SELECT 
    Playlist.Name AS [Playlist Name],
    Playlist.PlaylistId,
    COUNT(PlaylistTrack.PlaylistId) AS [Total number of Tracks] 
FROM Playlist 
INNER JOIN PlaylistTrack ON PlaylistTrack.PlaylistId = Playlist.PlaylistId 
GROUP BY Playlist.PlaylistId
```

**15. Предоставьте запрос, который показывает все треки, но не отображает никаких идентификаторов.**
<br>*Результирующая таблица должна содержать название альбома, тип носителя и жанр.*
```SQL
SELECT
    Track.Name  AS [Track],
    Album.Title AS [Album],
    MediaType.Name [Media Type],
    Genre.Name [Genre]
FROM Track 
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
INNER JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId
```

**16.Предоставьте запрос, который показывает заказы из таблицы Invoices и включает в себя количество купленных элементов InvoiceLine.**
```SQL
SELECT 
    Invoice.InvoiceId,
    COUNT(InvoiceLine.InvoiceId) 
FROM Invoice 
INNER JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId 
GROUP BY Invoice.InvoiceId

```
**17. Предоставьте запрос, который показывает общий объем продаж, произведенных каждым торговым агентом.**
```SQL
SELECT
    Employee.FirstName || " " || Employee.LastName AS [Sales Agent],
    SUM(Invoice.Total) AS [Total Sales]
FROM Employee 
INNER JOIN Customer ON Employee.EmployeeID = Customer.SupportRepId
INNER JOIN Invoice  ON Customer.CustomerId = Invoice.CustomerId
WHERE Employee.Title = "Sales Support Agent"
GROUP BY [Sales Agent]
--Steve Johnson: $720.16
--Margaret Park: $775.40
--Jane Peacock:  $833.04
```

**18. Какой торговый агент сделал больше всего продаж в 2009 году?**
```SQL
SELECT
    SalesAgent, 
    Max(TotalSales)
FROM
(SELECT
    e.FirstName || " " || e.LastName AS SalesAgent,
    SUM(i.Total) AS TotalSales
FROM Employee e
INNER JOIN Customer c ON e.EmployeeID = c.SupportRepId
INNER JOIN Invoice  i ON c.CustomerId = i.CustomerId
WHERE e.Title = "Sales Support Agent" AND i.InvoiceDate LIKE "2009%"
GROUP BY SalesAgent)
```

**19. Какой торговый агент сделал больше всего в продажах за все время?**
```SQL
SELECT
    SalesAgent, 
    Max(TotalSales)
FROM
(SELECT
    e.FirstName || " " || e.LastName AS SalesAgent,
    SUM(i.Total) AS TotalSales
FROM Employee e
INNER JOIN Customer c ON e.EmployeeID = c.SupportRepId
INNER JOIN Invoice  i ON c.CustomerId = i.CustomerId
WHERE e.Title = "Sales Support Agent"
GROUP BY SalesAgent)
```

**20. Предоставьте запрос, который показывает количество клиентов, назначенных каждому торговому агенту.**
```SQL
SELECT 
    Employee.FirstName || ' ' || Employee.LastName AS [Sales Agent],
    COUNT(Customer.SupportRepId) AS [# of Customers] 
FROM  Employee 
INNER JOIN Customer ON Customer.SupportRepId = Employee.EmployeeId 
GROUP BY Employee.LastName
```

**21. Предоставьте запрос, который показывает общий объем продаж в каждой стране.
<br>В какой стране клиенты тратят больше всего?**
```SQL
SELECT 
    Invoice.BillingCountry AS [Country], 
    SUM(Invoice.Total) AS [Total Sales] 
FROM Invoice 
GROUP BY Invoice.BillingCountry 
ORDER BY [Total Sales] DESC
```
**22. Предоставьте запрос, который показывает самый покупаемый трек 2013 года.**
```SQL
SELECT 
    Track.TrackId, 
    Track.Name AS [Track Name], 
    COUNT(InvoiceLine.TrackId) AS [Times Purchased] 
FROM Track 
INNER JOIN InvoiceLine ON InvoiceLine.TrackId = Track.TrackId 
INNER JOIN Invoice     ON Invoice.InvoiceId = InvoiceLine.InvoiceId 
WHERE Invoice.InvoiceDate LIKE '%2013%' 
GROUP BY Track.TrackId 
ORDER BY [Times Purchased] DESC
```

**23. Предоставьте запрос, который показывает топ-5 самых покупаемых треков за все время.**
```SQL
SELECT
    t.Name AS Trackname,
    COUNT(il.InvoiceLineId) AS TotalPurchases
FROM Track t
INNER JOIN InvoiceLine il ON t.TrackId = il.TrackId
INNER JOIN Invoice i ON il.InvoiceId = i.InvoiceId
WHERE i.InvoiceDate 
GROUP BY t.Name
ORDER BY TotalPurchases DESC
LIMIT 5
```

**24. Предоставьте запрос, который показывает топ-3 самых продаваемых исполнителя.**
```SQL
SELECT 
    Artist.Name,
    SUM(InvoiceLine.UnitPrice) AS [Total Sales] 
FROM Track 
INNER JOIN InvoiceLine ON InvoiceLine.TrackId = Track.TrackId 
INNER JOIN Invoice ON Invoice.InvoiceId = InvoiceLine.InvoiceId 
INNER JOIN Album ON Album.AlbumId = Track.AlbumId 
INNER JOIN Artist ON Artist.ArtistId = Album.ArtistId 
GROUP BY Artist.Name 
ORDER BY [Total Sales] DESC LIMIT 3
```

**25. Предоставьте запрос, который показывает наиболее покупаемый тип носителя.**
```SQL
SELECT 
    MediaType.Name AS [Media Type], 
    COUNT(InvoiceLine.InvoiceLineId) AS [Times Purchased] 
FROM MediaType 
INNER JOIN Track ON Track.MediaTypeId = MediaType.MediaTypeId 
INNER JOIN InvoiceLine ON InvoiceLine.TrackId = Track.TrackId 
GROUP BY MediaType.Name 
ORDER BY [Times Purchased] DESC LIMIT 1
```