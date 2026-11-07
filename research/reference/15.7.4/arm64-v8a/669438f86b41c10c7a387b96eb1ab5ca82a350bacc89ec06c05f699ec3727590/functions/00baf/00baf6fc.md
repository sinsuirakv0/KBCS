# 00baf6fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00baf5f0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf5f0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00baf6fc",
  "name": "_ZNSt6__ndk115numpunct_bynameIcED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "073c302c2409df54ca7c43bbc1a1ae51eeadc21200bb1121eeb63aaa1c094f50",
  "source_text_sha256": "073c302c2409df54ca7c43bbc1a1ae51eeadc21200bb1121eeb63aaa1c094f50"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1c90](../00be1/00be1c90.md)

## 疑似コード / UTF-8 666 bytes

~~~c

void _ZNSt6__ndk115numpunct_bynameIcED0Ev(void *param_1)

{
                    /* try { // try from 00baf700 to 00caf70b has its CatchHandler @ 00baf710 */
                    /* catch() { ... } // from try @ 00baf58c with catch @ 00baf70c
                       try { // try from 00baf70c to 00caf73b has its CatchHandler @ 00baf554 */
                    /* catch() { ... } // from try @ 00baf700 with catch @ 00baf710 */
  _ZNSt6__ndk18numpunctIcED1Ev();
                    /* catch() { ... } // from try @ 00baf5c8 with catch @ 00baf714 */
                    /* catch() { ... } // from try @ 00baf5ec with catch @ 00baf718 */
  _ZdlPv(param_1);
  return;
}

~~~
