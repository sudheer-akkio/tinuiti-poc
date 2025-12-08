# Table Name: PATHMATICS_CHOMPS_COMPETITIVE_REPORT

## Table Description
Competitive advertising intelligence data from Pathmatics showing advertising spend, impressions, and placement details for Chomps competitors and related brands across digital channels. Includes advertiser hierarchy, publisher, channel, placement type, category, date, spend, and impressions. Used for competitive analysis, market share assessment, channel benchmarking, and strategic media planning. | :ui-name:Competitive Advertising Intelligence (Pathmatics) :short-name:pathmatics_competitive |<

## Data Dictionary

### Fields:

- `advertiser` (STRING): Name of the company or entity that paid for the media placement. Used to identify competitors and attribute spend to parent organizations for competitive analysis and market share calculations. Can be joined to advertiser reference tables for hierarchical reporting and portfolio analysis.
- `brand_root` (STRING): Top-level brand hierarchy classification or parent brand name. Used to group brands under common ownership or strategic groupings for portfolio-level competitive analysis and spend aggregation. Typically used as a categorical dimension for filtering and grouping rather than a strict foreign key.
- `brand_major` (STRING): Major brand classification within the brand hierarchy. Used for brand-level segmentation and analysis, enabling comparison of major brand investments across competitors. Supports brand portfolio analysis and strategic brand positioning insights.
- `brand_minor` (STRING): Minor brand classification within the brand hierarchy, providing more granular brand segmentation. Used for detailed brand-level analysis and to drill down into specific brand performance within competitive sets. Supports sub-brand and product line analysis.
- `brand_leaf` (STRING): Most granular brand classification or specific product brand name in the hierarchy. Used for product-level competitive analysis and to identify specific brand competitors at the most detailed level. Enables precise competitive benchmarking and product positioning analysis.
- `publisher` (STRING): Name of the publisher or platform where the advertisement was displayed (e.g., Facebook, YouTube, Hulu). Used to identify media partners, analyze publisher-level spend distribution, and assess competitive presence across platforms. Can be joined to publisher reference tables for platform categorization and analysis.
- `date` (DATE): Date on which the advertising activity occurred or was recorded. Used for time-series analysis, trend reporting, seasonal pattern identification, and temporal competitive analysis. Enables date-based filtering, aggregation, and alignment with campaign calendars and business periods.
- `channel` (STRING): Marketing channel or media type through which the advertisement was delivered (e.g., Facebook, YouTube, Instagram, OTT). Used to segment competitive spend by channel for channel-level benchmarking, competitive share analysis, and media mix comparison. Can be joined to channel taxonomy tables for standardized channel classification.
- `top_level_category` (STRING): High-level industry or product category classification (e.g., Consumer Packaged Goods, Food & Dining Services). Used to filter and group competitive data by category for category-level competitive analysis and market share assessment. Supports category benchmarking and industry trend analysis.
- `placement` (STRING): Specific placement type or ad format within the channel (e.g., Feed, Reels, Stories, In-Stream, Marketplace). Used to analyze competitive ad format preferences, placement-level performance, and creative strategy insights. Enables granular competitive analysis at the placement level for tactical media planning.
- `spend_usd` (FLOAT): Monetary amount spent on advertising for the record, denominated in US dollars. Used in competitive spend analysis, market share calculations, budget benchmarking, and ROI comparisons. Enables aggregation of total competitive spend across dimensions for strategic insights and budget planning.
- `impressions` (INTEGER): Count of ad impressions delivered for the record. Used to measure competitive advertising volume, calculate cost per impression (CPI), assess reach and frequency, and compare impression volumes across competitors and channels. Supports competitive media efficiency analysis and audience exposure assessment.

## (OPTIONAL) Table Relationships

## (Optional) Business Context
This table provides competitive advertising intelligence from Pathmatics, enabling analysis of competitor advertising strategies, spend patterns, and channel mix. The data supports competitive benchmarking, market share analysis, and strategic media planning by revealing how competitors allocate budgets across channels, publishers, and placements.

## (Optional) Notes

