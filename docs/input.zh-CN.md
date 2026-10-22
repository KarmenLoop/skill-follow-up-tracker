# 输入与输出

[English](INPUT.md) | 简体中文 · [教程](tutorial.zh-CN.md)

对应 **v0.2.1**。输入为 UTF-8 JSON 对象，最大 10 MiB。支持 --input 文件路径与 --input -；拒绝重复 JSON 键和非有限常量。

| 字段 | 约定 |
| --- | --- |
| now | 带 UTC 偏移的本次检查时间。 |
| max_attempts | 正整数，最多跟进次数。 |
| contacts | 数组，每项含唯一 id、name、status（waiting / replied / closed）、整数 attempts、带时区的 next_check；可选 expires 截止时间。 |

## 样例

```json
{
  "now": "2026-10-19T12:00:00Z",
  "max_attempts": 3,
  "contacts": [
    {
      "id": "c1",
      "name": "Example partner",
      "status": "waiting",
      "attempts": 1,
      "next_check": "2026-10-19T10:00:00Z"
    },
    {
      "id": "c2",
      "name": "Former lead",
      "status": "replied",
      "attempts": 1,
      "next_check": "2026-10-18T10:00:00Z"
    }
  ]
}
```

[完整预期结果](../examples/expected.json)。JSON 键名保留英文以匹配程序接口；字符串内容使用你的实际记录。退出码 0 代表处理完成，不代表所报告问题已经通过。

## 错误与副作用

工具不联网，不执行提交的命令。只读取输入及约定中明确指出的本地路径；默认向终端输出，只在明确 --output 时写入新文件。无效输入退出码为 2，已有结果文件不覆盖。写入失败可能留下不完整新文件，应先检查。安装是独立的明确操作。
