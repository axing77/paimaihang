# Auctionator Performance Optimization Notes

## Problem Description
When using the Auctionator addon on Titan/Time Walking servers (Chinese WoW), severe lag occurs:
- Slow item searches
- Sluggish item posting
- Delayed purchase operations

This is likely due to Blizzard implementing API throttling measures to combat "auction house goblins" (players using addons to frequently manipulate the auction house for profit).

## Optimization Measures

### 1. Disable Full Scan Feature (Most Important)
**File**: `Source_LegacyAH/FullScan/Mixins/Frame.lua`
**Change**: Return immediately at the start of `InitiateScan()` function to avoid calling `QueryAuctionItems()` for full auction house scanning
**Reason**: Full scans request all auction house data at once, which is the most likely operation to trigger official throttling

### 2. Reduce Batch Processing Speed
**File**: `Source_LegacyAH/FullScan/Mixins/Frame.lua`
**Changes**: 
- Reduced batch size from 250 to 50
- Increased delay between batches from 0.01s to 0.1s
**Reason**: Lower instantaneous API call frequency

### 3. Reduce Throttle Timeout
**File**: `Source_LegacyAH/AH/Mixins/Throttling.lua`
**Change**: Reduced timeout from 10 seconds to 5 seconds
**Reason**: Improve responsiveness while avoiding throttling triggers

### 4. Add Delay Between Scan Pages
**File**: `Source_LegacyAH/AH/Mixins/Scan.lua`
**Change**: Added 0.3 second delay before querying next page
**Reason**: Reduce continuous query frequency to avoid throttling

### 5. Reduce Results Per Page
**File**: `Source_LegacyAH/Constants/Main.lua`
**Change**: Reduced MaxResultsPerPage from 50 to 30
**Reason**: Lower data volume per query and server load

### 6. Disable Default Auto List Search
**File**: `Source/Config/Main.lua`
**Change**: Set `AUTO_LIST_SEARCH` default to false
**Reason**: Reduce unnecessary automatic queries

### 7. Ensure Full Scan Option Disabled by Default
**File**: `Source/Config/Main.lua`
**Change**: Explicitly set `REPLICATE_SCAN` to false
**Reason**: Prevent users from accidentally triggering full scans

### 8. Optimize Cancellation Scan Speed
**File**: `Source_LegacyAH/Tabs/Cancelling/Mixins/UndercutScan.lua`
**Changes**: 
- Added 0.2 second delay in NextStep function
- Added 0.3 second delay in ProcessScanResult
**Reason**: Cancellation scan needs to query prices for each player's auction; delays prevent continuous rapid queries

## Usage Recommendations

1. **Avoid frequent searches**: Minimize repeated searches within short time periods
2. **Process one at a time**: Don't post or purchase many items in rapid succession
3. **Be patient**: If you encounter delays, wait rather than clicking repeatedly
4. **Disable other AH addons**: Avoid multiple addons calling APIs simultaneously

## Preserved Features

The following core features remain functional:
- Single item searches
- Manual individual item posting
- Current price viewing
- Price history (based on cached data)
- Shopping lists (manual trigger required)
- Keyboard shortcuts
- Tooltip price display

## Removed/Limited Features

- ❌ Full auction house scan (Full Scan/Replicate)
- ⚠️ Automatic batch searches (manual trigger required)
- ⚠️ Rapid continuous operations (delays added)

## Technical Notes

These modifications work primarily through:
1. Directly disabling the most resource-intensive full scan feature
2. Adding delays (throttling) at key query points
3. Reducing data volume per request
4. Disabling automatically triggered queries

All modifications preserve the original code (commented out) for easy future adjustment or restoration.

## Version Information
Optimized version based on: Auctionator v284 for Interface 30405 (WotLK Classic)
Optimization date: 2024
