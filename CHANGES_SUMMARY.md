# Auctionator 优化修改摘要 / Changes Summary

## 修改的文件 / Modified Files

### 1. Source_LegacyAH/FullScan/Mixins/Frame.lua
- **行数 19-46**: 禁用InitiateScan函数，防止全扫描
- **行数 89-95**: 减少批量处理大小从250到50
- **行数 171-175**: 增加批处理延迟从0.01秒到0.1秒

### 2. Source_LegacyAH/AH/Mixins/Throttling.lua
- **行数 28-29**: 减少超时时间从10秒到5秒

### 3. Source_LegacyAH/AH/Mixins/Scan.lua
- **行数 89-107**: 在ProcessSearchResults中添加0.3秒页面间延迟

### 4. Source_LegacyAH/Constants/Main.lua
- **行数 1-2**: 减少MaxResultsPerPage从50到30

### 5. Source/Config/Main.lua
- **行数 89-92**: 确保REPLICATE_SCAN和AUTO_LIST_SEARCH默认禁用

### 6. Source_LegacyAH/Tabs/Cancelling/Mixins/UndercutScan.lua
- **行数 100-131**: 在NextStep函数中添加0.2秒延迟
- **行数 235-240**: 在ProcessScanResult中添加0.3秒延迟

## 新增文件 / New Files

1. **OPTIMIZATION_NOTES_CN.md** - 中文优化说明文档
2. **OPTIMIZATION_NOTES_EN.md** - 英文优化说明文档
3. **CHANGES_SUMMARY.md** - 本文件，修改摘要
4. **.gitignore** - Git忽略文件配置

## 技术要点 / Technical Highlights

### 主要策略 / Main Strategies
1. **禁用全扫描** - 最重要的优化，直接阻止最消耗资源的操作
2. **增加延迟** - 在关键查询点添加延迟，降低API调用频率
3. **减少数据量** - 降低单次请求的数据量
4. **禁用自动功能** - 关闭不必要的自动触发查询

### 延迟策略 / Delay Strategy
- 全扫描批处理: 0.1秒（原0.01秒）
- 搜索页面间: 0.3秒（新增）
- 取消扫描步骤间: 0.2秒（新增）
- 取消扫描处理后: 0.3秒（新增）

### 数据量控制 / Data Volume Control
- 每页结果数: 30（原50）
- 批处理大小: 50（原250）

## 兼容性说明 / Compatibility Notes

这些修改针对的是WotLK Classic（接口版本30405）。理论上也应该适用于：
- Classic Era
- TBC Classic
- 其他使用旧版拍卖行API的服务器

**不适用于**：
- 现代版零售服（Retail/Mainline），因为它们使用完全不同的C_AuctionHouse API

## 测试建议 / Testing Recommendations

1. **测试搜索**: 搜索单个物品，观察响应速度
2. **测试上架**: 逐个上架物品，检查是否顺畅
3. **测试购买**: 购买物品，确认无卡顿
4. **测试取消**: 使用取消被压价拍卖功能
5. **避免全扫描**: 确认全扫描按钮不再触发实际扫描

## 回滚方法 / Rollback Method

如果需要恢复原始功能：
1. 找到注释的原始代码（标记为"原始XXX代码已禁用"）
2. 取消注释并删除新增的return语句
3. 移除添加的延迟代码
4. 恢复原始的数值设置

## 版本信息 / Version Info
- 基础版本: Auctionator v284
- 接口版本: 30405 (WotLK Classic)
- 优化日期: 2024-12
- 目标服务器: 泰坦时光服务器 / Titan Time Walking Servers
