# 安装腾讯云 CLI（可选）
# pip install tccli

# 配置密钥
# tccli configure set secretId YOUR_SECRET_ID
# tccli configure set secretKey YOUR_SECRET_KEY
# tccli configure set region ap-beijing  # HunYuan 目前仅支持北京/上海
#
# # 调用测试
# tccli hunyuan ChatCompletions --cli-unfold-argument \
#     --Model hunyuan-lite \
#     --Messages '[{"Role":"user","Content":"你好"}]'