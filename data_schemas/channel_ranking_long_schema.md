# Table Name: CHANNEL_RANKING_LONG

## Table Description
Per-strategy, per-channel ranking table that lists marketing strategy identifiers, channel names, and numeric channel_ranking scores (long format) to indicate relative effectiveness or priority of each channel for a given campaign/audience segment. Used to compare and prioritize media channels for planning, optimization, and audience/segmentation decisions; suitable for audience generation.

## Data Dictionary

### Fields:

- `strategy` (STRING): Identifier for the marketing strategy, campaign configuration, or audience/segment used to evaluate channel performance. Business purpose: groups channel rankings by the specific strategy or plan to enable strategy-level reporting and decision-making. Typical usage: filter, aggregate and compare channel rankings across strategies; join to a strategy or campaign dimension to pull additional metadata (e.g., objectives, time window, audience). May serve as a foreign key to a strategy/campaign reference table. | :lower |<
- `channel` (STRING): Human-readable name of the media or marketing channel being evaluated (e.g., TV, AVOD, in-store, outdoor). Business purpose: identifies the delivery vehicle whose performance or priority is being measured. Typical usage: report and visualize channel-level rankings, drive media planning and allocation, and join to a channel master/lookup table for standardized attributes. May map to a channel dimension or lookup. | :lower |<
- `channel_ranking` (FLOAT): Numeric score representing the channel's relative rank, effectiveness, or priority within the specified strategy. Business purpose: quantifies how channels compare within a strategy to support prioritization, budget allocation, and optimization. Typical usage: sort and filter channels by rank, feed into allocation models or optimization algorithms, and surface top channels in dashboards and reports.

## (OPTIONAL) Table Relationships

## (Optional) Business Context

## (Optional) Notes

