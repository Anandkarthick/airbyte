# Clari

## Overview

Clari is the heartbeat of your revenue organization and holds your most important revenue data. The Clari API enables you to retrieve revenue data out of the Clari platform and enrich downstream reporting and revenue systems. 

### Resulting schema

The API returns JSON-encoded responses and uses standard HTTP response codes, authentication, and verbs. The response is split into five lists and is
structured similar to look up tables.

``` response

entries":[...],
users":[...],
fields":[...],
timePeriods":[...],
timeFrames":[...]

```
1. entries: values for specific fields for a given user. Each entry includes a userId, fieldId, timePeriodId, and timeFrameId for easy mapping.
2. users: are all the users that fall into the requested scope of the export request.
3. fields: include all columns from the grid in Forecasting.
4. timePeriods: maps to the quarter the forecast entry was made.
5. timeFrames: for current forecasts, this is the week in which the data was pulled.

### Table considerations

Airbyte creates following 5 tables for each request. 

- entries
- users
- fields
- timeperiods
- timeframes

Entries schema could differ depending on typesToExport, refer API documentation [here] (https://developer.clari.com/documentation/external_spec#/Forecast%20API/externalFcwResource)