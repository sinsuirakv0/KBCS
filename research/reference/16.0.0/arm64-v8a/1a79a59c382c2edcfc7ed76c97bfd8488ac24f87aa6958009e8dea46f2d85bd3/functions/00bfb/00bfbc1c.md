# 00bfbc1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfbc1c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5gbumpEi",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "47b19452d05e66a35de33bbf920d6544362c648cca1e548d9785c8a85daffc15",
  "source_text_sha256": "47b19452d05e66a35de33bbf920d6544362c648cca1e548d9785c8a85daffc15"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 182 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5gbumpEi(long param_1,int param_2)

{
  *(long *)(param_1 + 0x18) = *(long *)(param_1 + 0x18) + (long)param_2;
  return;
}

~~~
