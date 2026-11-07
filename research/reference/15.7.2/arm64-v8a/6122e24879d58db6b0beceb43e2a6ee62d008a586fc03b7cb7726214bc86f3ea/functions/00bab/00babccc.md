# 00babccc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00babdd8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babdd8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00babccc",
  "name": "_ZNSt6__ndk17codecvtIDsc9mbstate_tED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d5d4551cf9d9fb9df6959d8cb5ae81c06f30a9ff4eb013381c4db66b06bda58",
  "source_text_sha256": "0d5d4551cf9d9fb9df6959d8cb5ae81c06f30a9ff4eb013381c4db66b06bda58"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1ab0](../00be1/00be1ab0.md)

## 疑似コード / UTF-8 143 bytes

~~~c

void _ZNSt6__ndk17codecvtIDsc9mbstate_tED0Ev(void *param_1)

{
  _ZNSt6__ndk116__narrow_to_utf8ILm32EED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
