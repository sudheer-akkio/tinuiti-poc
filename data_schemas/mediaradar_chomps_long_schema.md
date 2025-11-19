# Table Name: MEDIARADAR_CHOMPS_LONG

## Table Description
Itemized TV advertising placements and spend for the Chomps brand from Mediaradar, listing advertiser/brand, media group and owner, program and genre, market, daypart, day-of-week, flight date, spend_usd and units for each placement; rows are at the program/daypart/market level. Used for media planning, campaign measurement and spend allocation—enables aggregation and analysis of spend by program, market, daypart or media owner. | :ui-name:Chomps Media Spend (Mediaradar) :short-name:chomps_media_spend |<

## Data Dictionary

### Fields:

- `advertiser` (STRING): Name of the company or entity that paid for the media placement. Used to attribute spend and performance to the advertiser, filter and roll up campaign-level reporting, and reconcile to advertiser master data. | :lower |<
- `brand` (STRING): Brand name associated with the advertised product or campaign. Used for brand-level reporting, segmentation of spend and creative performance, and aggregation across advertiser portfolios. Can be joined to brand reference data for hierarchical reporting. | :lower |<
- `media_group` (STRING): High-level media channel classification (e.g., Television). Used to group placements by broad channel for budgeting, channel mix analysis and strategic planning. Not typically a technical foreign key but may be mapped to a media taxonomy. | :lower |<
- `media` (STRING): More specific media type within the group (e.g., Cable TV, Broadcast). Used for channel segmentation, inventory planning and performance comparisons across media types. Usually used as a descriptive field for grouping rather than a strict foreign key. | :lower |<
- `media_owner` (STRING): Organization that owns or supplies the media inventory (e.g., network or publisher). Used to attribute spend and relationships to vendors, negotiate rates, and join to vendor or partner reference tables for procurement and reconciliation. | :lower |<
- `dow` (STRING): Day of week on which the media aired. Used for scheduling analysis, daypart optimization, and temporal reporting to identify performance patterns by weekday. Not a relational key. | :upper |<
- `national_local` (STRING): Indicates whether the placement targeted a national audience or local market. Used to segment spend and performance by geographic scope for planning and reporting, and to route analysis between national and local buys. Not a relational key. | :upper |<
- `market` (STRING): Geographic market or designated market area (DMA) where the media was delivered. Used for market-level analysis, planning, budget allocation and to join with market reference tables for geo-based insights. | :all-unique-vals :lower |<
- `program` (STRING): Title of the TV program or show where the ad aired. Used to attribute spend and creative performance to specific programming, analyze content-level effectiveness, and optionally join to program metadata catalogs. Not typically a synthetic key. | :lower |<
- `program_genre` (STRING): Genre or content category of the program (e.g., Entertainment, News). Used to analyze performance by content type, inform audience/contextual targeting, and map to genre reference lists for reporting. | :all-unique-vals :lower |<
- `daypart` (STRING): Time-of-day block in which the ad aired (e.g., Prime, Early Fringe). Used for scheduling analysis, optimization of ad timing, and grouping placements by viewing windows for performance comparisons. | :all-unique-vals :lower |<
- `property` (STRING): Broadcast property or network carrying the placement (e.g., network brand). Used to attribute spend and inventory to specific properties, negotiate network-level deals, and join to property/network reference tables for reporting. | :all-unique-vals :upper |<
- `flight_date` (DATETIME): Date associated with the ad flight or aggregated record for that day's placements. Used for time-series analysis, trend reporting, and aligning spend/units to calendar dates for forecasting and reconciliation.
- `spend_usd` (FLOAT): Monetary amount spent for the record, denominated in US dollars. Used in financial reporting, budget tracking, ROI and CPA calculations, and to aggregate total media spend across dimensions.
- `units` (FLOAT): Count of ad units or spots associated with the record (e.g., number of spots). Used to measure delivery volume, compute average cost per spot, and as an input to reach/frequency calculations and operational reconciliation.

## (OPTIONAL) Table Relationships

## (Optional) Business Context

## (Optional) Notes

