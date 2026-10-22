# 006fbcec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](006fbcec.md)

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
  "source_sha256": "152b910f2e91956432c2de2b1b983dfe1a0746a998bc35dcd884b70da223762a",
  "source_text_sha256": "152b910f2e91956432c2de2b1b983dfe1a0746a998bc35dcd884b70da223762a"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 1248 bytes

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
        operator_delete(pvVar1);
      }
      pvVar1 = *(void **)((long)pvVar3 + -0x30);
      if (pvVar1 != (void *)0x0) {
        *(void **)((long)pvVar3 + -0x28) = pvVar1;
                    /* try { // try from 006fbd44 to 007fbd57 has its CatchHandler @ 006fbfbc */
        operator_delete(pvVar1);
      }
      pvVar3 = (void *)((long)pvVar3 + -0x88);
    } while (pvVar3 != pvVar2);
    pvVar1 = *(void **)(param_1 + 0x38);
  }
  *(void **)(param_1 + 0x40) = pvVar2;
                    /* try { // try from 006fbd5c to 007fbdb3 has its CatchHandler @ 006fbff4 */
  operator_delete(pvVar1);
  return;
}

~~~
