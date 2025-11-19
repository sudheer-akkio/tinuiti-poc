# Table Name: EFFECT_CURVE_LONG

## Table Description
Estimated marketing effect scores by budget, objective, and channel in long format, representing how incremental effect changes across budget levels for each media channel and campaign objective; used to build effect curves for media mix modeling and budget allocation decisions. | :ui-name:Channel Effect Curves :short-name:effect_curve |<

## Data Dictionary

### Fields:

- `budget` (INTEGER): Planned or allocated monetary spend for the scenario point on the effect curve. Business purpose: represents the investment level used to evaluate marginal impact and to make budget-allocation decisions. Typical use: treated as the independent variable in modeling and scenario analysis, used for optimization, forecasting, and comparing spend across channels and objectives.
- `objective` (STRING): Marketing or campaign objective associated with the effect measurement (e.g., awareness, consideration). Business purpose: segments result sets by goal to align KPIs and prioritization. Typical use: filter/group/report on effect curves by campaign goal and join to objective reference metadata for KPI definitions; can serve as a categorical lookup key to an objectives reference table. | :lower |<
- `channel` (STRING): Marketing channel or media type through which the budget is spent (e.g., TV, social, search). Business purpose: identifies where spend is applied so performance can be attributed and channels compared. Typical use: segment and compare effect curves by channel, join to channel metadata (targeting, ad formats, cost metrics), and inform channel-level allocation decisions. | :lower |<
- `effect_score` (FLOAT): Estimated effect or incremental impact measured at the given budget, objective, and channel (expressed in the model's effect units). Business purpose: quantifies the marginal benefit or lift used to judge campaign effectiveness and ROI. Typical use: treated as the dependent variable in analyses, plotted as effect curves, and consumed by optimization and reporting processes.

## (OPTIONAL) Table Relationships

## (Optional) Business Context

## (Optional) Notes

