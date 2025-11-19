# Table Name: MAXIMUM_REACH

## Table Description
Channel-level maximum potential audience reach expressed as proportions (0–1); each row lists a media channel and its maximum_reach value. This table is used to compare channel coverage for media planning, campaign allocation, and audience generation/segmentation. | :ui-name:Maximum Reach by Channel :short-name:max_reach |<

## Data Dictionary

### Fields:

- `channel` (STRING): The name/label of the marketing or media channel (e.g., TV, internet, YouTube) used to classify where advertising or content is delivered. Business purpose: identifies the distribution vehicle for campaigns and reporting. Usage: serves as a categorical dimension for segmentation, performance comparison, media planning, and joining to channel reference or attribution tables when available. | :lower |<
- `maximum_reach` (FLOAT): Estimated maximum audience reach for the channel expressed as a proportion or percentage of the target population. Business purpose: quantifies the upper bound of unique audience exposure provided by the channel for planning, forecasting, and prioritization. Usage: used in media planning, reach–frequency modeling, channel selection and budget allocation, and in estimating combined reach across channels.

## (OPTIONAL) Table Relationships

## (Optional) Business Context

## (Optional) Notes

