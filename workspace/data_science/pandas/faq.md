# pandas常见问题汇总

## 安装

* windows `pip3 install pandas`安装pandas报如下错误

  ```bash
  Could not fetch URL https://pypi.org/simple/pandas/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pandas/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:997)'))) - skipping
  ```

  本地安装有科学上网的代理软件导致的，关闭代理即可。