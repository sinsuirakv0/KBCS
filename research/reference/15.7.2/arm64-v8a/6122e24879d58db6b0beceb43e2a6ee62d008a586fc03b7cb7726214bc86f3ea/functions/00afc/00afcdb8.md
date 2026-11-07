# 00afcdb8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00afcec4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcec4.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00afcdb8",
  "name": "_INIT_273",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d506302ef376401ac49ad7ee34fb2d0f6cf3bd7c6532c48bf713383b5003cdf7",
  "source_text_sha256": "d506302ef376401ac49ad7ee34fb2d0f6cf3bd7c6532c48bf713383b5003cdf7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bddd20](../00bdd/00bddd20.md)

## 疑似コード / UTF-8 434 bytes

~~~c

void _INIT_273(void)

{
  undefined8 uVar1;
  
                    /* try { // try from 00afcdc8 to 00bfcddf has its CatchHandler @ 00aff3b8 */
  uVar1 = _Znwm(0x28);
  _ZN8firebase5MutexC2ENS0_4ModeE(uVar1,1);
                    /* try { // try from 00afcde0 to 00bfce7b has its CatchHandler @ 00af560c */
  *(undefined8 *)PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b898 =
       uVar1;
  return;
}

~~~
