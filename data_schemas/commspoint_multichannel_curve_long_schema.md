# Table Name: COMMSPOINT_MULTICHANNEL_CURVE_LONG

## Table Description
Long-format table showing estimated effect scores by budget level, reach threshold, and individual channel, representing how incremental effect changes across budget levels for each media channel at different reach thresholds (1+ and 3+). Includes overall channel mix effect scores. Used to build multichannel effect curves for media mix modeling, budget allocation decisions, and understanding channel synergies. | :ui-name:COMMSPOINT Multichannel Effect Curves :short-name:commspoint_multichannel_curve |<

## Data Dictionary

### Fields:

- `reach_threshold` (STRING): Reach threshold identifier indicating the minimum number of channel exposures required (e.g., 1plus for 1+ reach, 3plus for 3+ reach). Business purpose: segments effect curves by reach frequency to understand how channel performance varies with exposure levels. Typical usage: filter and compare effect curves by reach threshold, analyze frequency impact on effectiveness, and inform frequency planning decisions. | :lower |<
- `budget` (INTEGER): Planned or allocated monetary spend for the scenario point on the effect curve. Business purpose: represents the investment level used to evaluate marginal impact and to make budget-allocation decisions. Typical use: treated as the independent variable in modeling and scenario analysis, used for optimization, forecasting, and comparing spend across channels and reach thresholds.
- `channel` (STRING): Marketing channel or media type through which the budget is spent (e.g., tv_ads, avod_ads, facebook_ads, youtube_ads). Business purpose: identifies where spend is applied so performance can be attributed and channels compared. Typical use: segment and compare effect curves by channel, join to channel metadata (targeting, ad formats, cost metrics), and inform channel-level allocation decisions. | :lower |<
- `channel_mix` (FLOAT): Overall combined effect score for the channel mix at the given budget level and reach threshold. Business purpose: quantifies the synergistic effect of the combined channel strategy, accounting for cross-channel interactions and multichannel exposure benefits. Typical usage: compare overall mix effectiveness across budget levels, assess multichannel synergies, and inform holistic media mix optimization.
- `effect_score` (FLOAT): Estimated effect or incremental impact measured at the given budget, reach threshold, and channel (expressed in the model's effect units). Business purpose: quantifies the marginal benefit or lift used to judge channel effectiveness and ROI at different frequency levels. Typical use: treated as the dependent variable in analyses, plotted as effect curves, consumed by optimization and reporting processes, and compared across channels and reach thresholds.

## (OPTIONAL) Table Relationships

## (Optional) Business Context
This table combines multichannel curve data for different reach thresholds (1+ and 3+ exposures) to enable analysis of how frequency impacts channel effectiveness. The channel_mix column captures synergistic effects when multiple channels are used together, which is critical for understanding multichannel media planning.

## (Optional) Notes
The reach_threshold dimension allows analysts to compare how channel effectiveness changes when requiring higher frequency (3+ vs 1+ exposures), which is important for understanding the impact of frequency on campaign performance.

