# 006fbcec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `006fbcec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fbcec.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "006fbcec",
  "name": "FUN_006fbcec",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4cb8cf68fd69e8b34eff77943f0633469018559ed8ad1dc122543b6d9bc92dce",
  "source_text_sha256": "4cb8cf68fd69e8b34eff77943f0633469018559ed8ad1dc122543b6d9bc92dce"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード / UTF-8 1182 bytes

~~~c

void FUN_006fbcec(long param_1)

{
  void *pvVar1;
  void *pvVar2;
  void *pvVar3;
  
                    /* try { // try from 006fbcf4 to 007fbd03 has its CatchHandler @ 006fbf70 */
  pvVar2 = *(void **)(param_1 + 0x38);
  if (pvVar2 == (void *)0x0) {
    return;
  }
                    /* try { // try from 006fbd04 to 007fbd13 has its CatchHandler @ 006fbf6c */
  pvVar3 = *(void **)(param_1 + 0x40);
  pvVar1 = pvVar2;
  if (pvVar3 != pvVar2) {
    do {
      pvVar1 = *(void **)((long)pvVar3 + -0x18);
      if (pvVar1 != (void *)0x0) {
        *(void **)((long)pvVar3 + -0x10) = pvVar1;
        _ZdlPv(pvVar1);
      }
      pvVar1 = *(void **)((long)pvVar3 + -0x30);
      if (pvVar1 != (void *)0x0) {
        *(void **)((long)pvVar3 + -0x28) = pvVar1;
                    /* try { // try from 006fbd44 to 007fbd57 has its CatchHandler @ 006fbfbc */
        _ZdlPv(pvVar1);
      }
      pvVar3 = (void *)((long)pvVar3 + -0x88);
    } while (pvVar3 != pvVar2);
    pvVar1 = *(void **)(param_1 + 0x38);
  }
  *(void **)(param_1 + 0x40) = pvVar2;
                    /* try { // try from 006fbd5c to 007fbdb3 has its CatchHandler @ 006fbff4 */
  _ZdlPv(pvVar1);
  return;
}

~~~
