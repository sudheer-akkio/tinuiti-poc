# Table Name: MEDIA_CONSUMPTION_DAY_STANDARDIZED

## Table Description
Standardized per-channel distribution of daily media usage showing the proportion of respondents who report not using or spending various hours per day on each media channel (don't use, <1h, 1–3h, 3–5h, >5h); values are fractional shares by channel. This behavioral table is intended to inform media planning and audience segmentation and is suitable for audience generation. | :ui-name:Daily Media Consumption by Channel :short-name:media_consumption_day |<

## Data Dictionary

### Fields:

- `channel` (STRING): Name of the media channel or platform (e.g., TV, radio, newspapers) for which time-on-media metrics are reported. Business purpose: identifies the channel dimension used for segmentation, reporting and campaign planning. Typical use: group, filter or join to channel master data for cross-channel analysis, media mix and audience measurement. | :lower |<
- `don_t_use_on_reg_day` (FLOAT): Proportion of the audience that does not use this channel on a typical/regular day. Business purpose: indicates non-usage to inform reach, penetration and opportunity for activation. Typical use: input to reach/frequency models, channel prioritization, gap analysis and reporting.
- `less_than_an_hour_a_day` (FLOAT): Proportion of the audience that spends less than one hour per day on this channel. Business purpose: measures low-engagement audience share to inform targeting and content scheduling. Typical use: segment audiences by engagement level, inform time-budgeting and performance benchmarking.
- `1_to_3_hours_a_day` (FLOAT): Proportion of the audience that spends between one and three hours per day on this channel. Business purpose: captures moderate engagement for planning reach and frequency and allocating media weight. Typical use: used in audience segmentation, forecasting, and campaign effectiveness analysis.
- `3_to_5_hours_a_day` (FLOAT): Proportion of the audience that spends between three and five hours per day on this channel. Business purpose: identifies high-engagement users to inform premium placements, longer-form creative and frequency settings. Typical use: used for targeting high-engagement cohorts, inventory planning and ROI analysis.
- `more_than_5_hours_a_day` (FLOAT): Proportion of the audience that spends more than five hours per day on this channel. Business purpose: highlights very high engagement and potential saturation or heavy-user segments for strategy decisions. Typical use: used in advanced audience segmentation, churn/saturation analysis and optimizing heavy-user outreach.

## (OPTIONAL) Table Relationships

## (Optional) Business Context

## (Optional) Notes

