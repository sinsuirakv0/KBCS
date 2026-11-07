# 00baef4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00baf058`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf058.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00baef4c",
  "name": "_ZNSt6__ndk18numpunctIcED1Ev",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7cec6f8788b4bdca7f80d4e0a9e2838a97ecf76a7855f614ccfde4f50273397",
  "source_text_sha256": "f7cec6f8788b4bdca7f80d4e0a9e2838a97ecf76a7855f614ccfde4f50273397"
}
~~~

## 呼び出し元

- [00be1b30](../00be1/00be1b30.md)
- [00be1b40](../00be1/00be1b40.md)
- [00be1b90](../00be1/00be1b90.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb3b0](../00bdb/00bdb3b0.md)

## 疑似コード / UTF-8 265 bytes

~~~c

void _ZNSt6__ndk18numpunctIcED1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk18numpunctIcEE_00c1beb8 + 0x10);
  if ((*(byte *)(param_1 + 3) & 1) != 0) {
    _ZdlPv((void *)param_1[5]);
  }
  _ZNSt6__ndk119__shared_weak_countD2Ev(param_1);
  return;
}

~~~
