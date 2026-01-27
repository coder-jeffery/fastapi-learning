#!/bin/bash

# 脚本名称: rewrite-author.sh
# 功能: 使用 git filter-repo 修正错误的作者/提交者信息
# 作者: Jeffery (根据你的需求定制)
# 注意: 此操作会重写 Git 历史，请确保在副本中运行！

set -e  # 遇到错误立即退出

# === 配置区（按需修改）===
OLD_AUTHOR_NAME="19901712802"        # 注意 $ 是特殊字符，需转义
OLD_AUTHOR_EMAIL="123456jcm$"
NEW_AUTHOR_NAME="jeffery"
NEW_AUTHOR_EMAIL="19901712802@163.com"

# === 检查依赖 ===
if ! command -v git &> /dev/null; then
    echo "❌ 错误: 未找到 'git' 命令。"
    exit 1
fi

if ! command -v git-filter-repo &> /dev/null; then
    echo "❌ 错误: 未找到 'git-filter-repo'。"
    echo "   请安装: pip3 install git-filter-repo"
    exit 1
fi

# === 确保不在裸仓库或子模块中运行 ===
if [ ! -d ".git" ]; then
    echo "❌ 错误: 当前目录不是 Git 仓库根目录。"
    echo "   请 cd 到你的 Git 项目根目录后再运行此脚本。"
    exit 1
fi

# === 检查是否已存在 filter-repo 备份（防止重复运行）===
if [ -d ".git/filter-repo" ]; then
    echo "⚠️  警告: 检测到之前运行过 git-filter-repo。"
    echo "   建议在一个干净的克隆副本中运行此脚本。"
    read -p "是否继续？(y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =～ ^[Yy]$ ]]; then
        echo "已取消。"
        exit 0
    fi
fi

# === 构造 commit-callback 的 Python 代码 ===
# 注意：字节串 b"" 必须保留，且 $ 在 Shell 中需转义为 \$
CALLBACK_CODE="
if commit.author_name == b\"${OLD_AUTHOR_NAME//\$/\\\$}\" and commit.author_email == b\"$OLD_AUTHOR_EMAIL\":
    commit.author_name = b\"$NEW_AUTHOR_NAME\"
    commit.author_email = b\"$NEW_AUTHOR_EMAIL\"
    commit.committer_name = b\"$NEW_AUTHOR_NAME\"
    commit.committer_email = b\"$NEW_AUTHOR_EMAIL\"
"

# === 执行 git filter-repo ===
echo "🔧 正在重写提交历史..."
git filter-repo --force --commit-callback "$CALLBACK_CODE"

echo "✅ 提交历史已成功重写！"
echo "新作者信息:"
echo "  名称: $NEW_AUTHOR_NAME"
echo "  邮箱: $NEW_AUTHOR_EMAIL"
echo ""
echo "📌 重要提示:"
echo "  - 如果该仓库已推送到远程，请强制推送（谨慎操作）："
echo "      git push --force --all origin"
echo "      git push --force --tags origin"
echo "  - 协作者需要重新克隆仓库，避免历史冲突。"