# Follow-up Tracker · 跟进清单

[English](README.md) | 简体中文

把仍在等回复的对话整理清楚：哪些到复查时间、哪些尚未到期，哪些已回复、关闭、过期或达到次数上限，可以停止跟进。

[下载 v0.2.1](https://github.com/KarmenLoop/skill-follow-up-tracker/releases/tag/v0.2.1) · [完整教程](docs/tutorial.zh-CN.md) · [输入参考（英文）](docs/INPUT.md) · [反馈问题](https://github.com/KarmenLoop/skill-follow-up-tracker/issues)

## 能做什么

样例中等待回复的合作方进入 due，已标记 replied 的联系人进入 stopped。

本包不会联系任何人，也不会在后台定时运行。复查时间和当前时间由你提供，是否实际联系另行决定。

![跟进清单 0.2.1 版本样例的真实 JSON 输出](docs/images/example-output-v0.2.1.svg)

*图片来自 v0.2.1 的真实本地输出，采用英文键名；[完整结果](examples/expected.json) · [图片来源记录](docs/images/provenance.json)。*

## 开始使用

在发行页下载 `karmen-follow-up-tracker-v0.2.1.zip` 与对应 `.sha256` 文件，核对哈希后解压。在解压目录中使用 Python 3.9 或更新版本：

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

预期版本：`karmen-follow-up-tracker 0.2.1`。样例中等待回复的合作方进入 due，已标记 replied 的联系人进入 stopped。

如果宿主读取 `~/.agents/skills`，可安装完整技能：

```sh
python3 install.py --host agents
```

目标目录已存在时安装器会拒绝覆盖。宿主发现和调用方式可能不同，见[安装与实践教程](docs/tutorial.zh-CN.md)。不使用 AI 宿主也能直接运行本地工具。

## 用于自己的任务

next_check 与 now 都要带 UTC 偏移。准确记录 attempts，设置有限的 max_attempts；事项确有截止时间时填写 expires。

分别尝试 closed、已过截止时间和次数耗尽的情况，查看 stop_reason，再判断是否需要准备下一次联系。

准备新输入前可查看[字段约定（英文）](docs/INPUT.md)。工具只依赖 Python 标准库，本身不需要模型账号、API 密钥或网络。使用 AI 宿主时，宿主有自己的数据与权限设置。

## 常见问题

**能自动发邮件吗？** 不能。它只生成待审阅清单，发送消息需要独立通信工具及相应授权。

**结果保存在哪里？** 默认向终端输出 JSON；使用 `--output` 时只创建新文件，已有输出文件会保留。工具只读取提交的记录和输入约定中明确列出的本地路径。

## 文档与支持

- [下载、安装、配置、练习、升级与卸载](docs/tutorial.zh-CN.md)
- [输入输出约定](docs/INPUT.md)与[兼容性说明](docs/COMPATIBILITY.md)（英文参考）
- [更新记录](CHANGELOG.md)、[参与贡献](CONTRIBUTING.md)、[支持](SUPPORT.md)和[安全反馈](SECURITY.md)

## 许可证

[MIT](LICENSE)。再分发时保留许可证和[声明](NOTICE.md)。由 [KarmenLoop](https://karmenloop.com) 维护。
