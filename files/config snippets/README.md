###Forcing a cable modem into partial mode

```
rr-lwr-cbr8#scm f81d.0f01.15b0 wide rc
Load for five secs: 14%/1%; one minute: 13%; five minutes: 14%
Time source is NTP, 13:11:32.445 EDT Fri Aug 7 2020
CM              DS-CTRL  RF   CH ID  STATUS        TYPE      PRIM-CHAN
--------------  -------  ---  -----  ------------  --------  ---------

f81d.0f01.15b0  2/0/6    0    1      UP            SC-QAM    YES
                         1    2      UP            SC-QAM    NO
                         2    3      UP            SC-QAM    NO
                         3    4      UP            SC-QAM    NO
                         4    5      UP            SC-QAM    NO
                         5    6      UP            SC-QAM    NO
                         6    7      UP            SC-QAM    NO
                         7    8      UP            SC-QAM    NO
                         8    9      UP            SC-QAM    NO
                         9    10     UP            SC-QAM    NO
                         10   11     UP            SC-QAM    NO
                         11   12     UP            SC-QAM    NO
                         12   13     UP            SC-QAM    NO
                         13   14     UP            SC-QAM    NO
                         14   15     UP            SC-QAM    NO
                         15   16     UP            SC-QAM    NO
                         16   17     UP            SC-QAM    NO
                         17   18     UP            SC-QAM    NO
                         18   19     UP            SC-QAM    NO
                         19   20     UP            SC-QAM    NO
                         20   21     UP            SC-QAM    NO
                         21   22     UP            SC-QAM    NO
                         22   23     UP            SC-QAM    NO
                         23   24     UP            SC-QAM    NO
                         24   25     UP            SC-QAM    NO
                         25   26     UP            SC-QAM    NO
                         26   27     UP            SC-QAM    NO
                         27   28     UP            SC-QAM    NO
                         28   29     UP            SC-QAM    NO
                         29   30     UP            SC-QAM    NO
                         30   31     UP            SC-QAM    NO
                         31   32     UP            SC-QAM    NO
```

```
test cable cm-status f81d.0f01.15b0 1 2 0103040102
```
Here are the available CM-STATUS types. Use 1 and 2 for failures and 4 and 5 for recoveries
```
rr-lwr-cbr8#test cable cm-status f81d.0f01.15b0 ?
  <0-65535>  Transaction ID

rr-lwr-cbr8#test cable cm-status f81d.0f01.15b0 1 ?
  1   NP Channel MDD timeout
  10  CM returned to A/C power
  11  MAC Removal Event
  16  DS OFDM profile failure
  17  Primary Downstream Change
  18  DPD Mismatch
  2   QAM/FEC lock failure
  20  NCP profile failure
  21  Loss of FEC Lock on PLC
  22  NCP profile recovery
  23  FEC recovery on PLC channel
  24  FEC recovery on OFDM profile
  25  OFDMA Profile failure
  26  MAP Storage overflow indicator
  27  MAP Storage almost full indicator
  3   Sequence out of range
  4   NP Channel MDD recovery
  5   QAM/FEC lock recovery
  6   T4 timeout
  7   T3 re-tries exceeded
  8   Successful ranging
  9   CM on battery backup
```

syntax: test cable cm-status <mac> <transaction ID> <CM-STATUS ID> 01030401<DS Ch ID in hex (2 digits)>
```
rr-lwr-cbr8#scm f81d.0f01.15b0 wide rc
Load for five secs: 16%/1%; one minute: 13%; five minutes: 14%
Time source is NTP, 13:11:57.360 EDT Fri Aug 7 2020
CM              DS-CTRL  RF   CH ID  STATUS        TYPE      PRIM-CHAN
--------------  -------  ---  -----  ------------  --------  ---------

f81d.0f01.15b0  2/0/6    0    1      UP            SC-QAM    YES
                         1    2      DOWN_PENDING  SC-QAM    NO
                         2    3      UP            SC-QAM    NO
                         3    4      UP            SC-QAM    NO
                         4    5      UP            SC-QAM    NO
                         5    6      UP            SC-QAM    NO
                         6    7      UP            SC-QAM    NO
                         7    8      UP            SC-QAM    NO
                         8    9      UP            SC-QAM    NO
                         9    10     UP            SC-QAM    NO
                         10   11     UP            SC-QAM    NO
                         11   12     UP            SC-QAM    NO
                         12   13     UP            SC-QAM    NO
                         13   14     UP            SC-QAM    NO
                         14   15     UP            SC-QAM    NO
                         15   16     UP            SC-QAM    NO
                         16   17     UP            SC-QAM    NO
                         17   18     UP            SC-QAM    NO
                         18   19     UP            SC-QAM    NO
                         19   20     UP            SC-QAM    NO
                         20   21     UP            SC-QAM    NO
                         21   22     UP            SC-QAM    NO
                         22   23     UP            SC-QAM    NO
                         23   24     UP            SC-QAM    NO
                         24   25     UP            SC-QAM    NO
                         25   26     UP            SC-QAM    NO
                         26   27     UP            SC-QAM    NO
                         27   28     UP            SC-QAM    NO
                         28   29     UP            SC-QAM    NO
                         29   30     UP            SC-QAM    NO
                         30   31     UP            SC-QAM    NO
                         31   32     UP            SC-QAM    NO
```


increment the transaction ID by at least 1 for every new message
power cycle / reseting the modem will clear current failures
If you send CM-STATUS 1 (MDD timeout) you can "clear" that error with CM-STATUS 4 (MDD recovery)
If you send CM-STATUS 2 (QAM failure) you can "clear" that error with CM-STATUS 5 (QAM recovery)
Channels will first move to DOWN_PENDING on failures or UP_PENDING on recoveries for "cable rf-change-dampen-time" seconds (default 30) then change to DOWN or UP
You can simulate failures / recoveries for multiple channels
It isn’t a valid condition to simulate failures / recoveries for the primary channel
The downstream channel ID always needs to be 2 hex digits (i.e. 15 = 0F, 16 = 10). Convert the number in the "CH ID" column of the "wide rcs" output to hex, not the "RF" channel number