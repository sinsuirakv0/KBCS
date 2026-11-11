# 00bef9cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bef9cc",
  "name": "_ZNSt6__ndk16chrono12system_clock9to_time_tERKNS0_10time_pointIS1_NS0_8durationIxNS_5ratioILl1ELl1000000EEEEEEE",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52977bd100fe8d4c83044b13210764ff197a9588662d3fb95e5eac04529addde",
  "source_text_sha256": "52977bd100fe8d4c83044b13210764ff197a9588662d3fb95e5eac04529addde"
}
~~~

## 呼び出し元

- [00c589a0](../00c58/00c589a0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 184 bytes

~~~c

long _ZNSt6__ndk16chrono12system_clock9to_time_tERKNS0_10time_pointIS1_NS0_8durationIxNS_5ratioILl1ELl1000000EEEEEEE
               (long *param_1)

{
  return *param_1 / 1000000;
}

~~~
