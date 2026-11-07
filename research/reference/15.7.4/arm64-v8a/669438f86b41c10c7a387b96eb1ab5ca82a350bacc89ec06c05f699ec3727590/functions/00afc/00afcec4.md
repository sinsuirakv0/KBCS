# 00afcec4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00afcdb8`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcdb8.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00afcec4",
  "name": "_INIT_273",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed2407d1fecac19070c8fa3707bcafd87a42391a30f22b0ad0fed4214b1af04e",
  "source_text_sha256": "ed2407d1fecac19070c8fa3707bcafd87a42391a30f22b0ad0fed4214b1af04e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdde20](../00bdd/00bdde20.md)

## 疑似コード / UTF-8 337 bytes

~~~c

void _INIT_273(void)

{
  undefined8 uVar1;
  
  uVar1 = _Znwm(0x28);
  _ZN8firebase5MutexC2ENS0_4ModeE(uVar1,1);
                    /* try { // try from 00afcef0 to 00bfcf07 has its CatchHandler @ 00aff3f0 */
  *(undefined8 *)PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b998 =
       uVar1;
  return;
}

~~~
