# 00bbfdc4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbfdc4.md)

## 関数情報

~~~json
{
  "address": "00bbfdc4",
  "name": "FUN_00bbfdc4",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04960c511ab904e9629f5663a140cdc7cd081523e5561e6a6938e6da75ab0daa",
  "source_text_sha256": "04960c511ab904e9629f5663a140cdc7cd081523e5561e6a6938e6da75ab0daa"
}
~~~
## 呼び出し元

- [00bbd1fc](../00bbd/00bbd1fc.md)

## 呼び出し先

- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

## 疑似コード 1/1 / UTF-8 1432 bytes

~~~c

void FUN_00bbfdc4(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
  pvVar3 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbfde0 to 00cbfdeb has its CatchHandler @ 00bc82e8 */
  lVar2 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00bbfdec to 00cbfdf7 has its CatchHandler @ 00bc82d8 */
  puVar1 = pvVar3;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbfdf8 to 00cbfe03 has its CatchHandler @ 00bc82c8 */
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      std::terminate();
    }
    lVar2 = 0;
                    /* try { // try from 00bbfe04 to 00cbfe6b has its CatchHandler @ 00bbf464 */
    *puVar1 = pvVar3;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c197e8;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 10;
  uVar5 = param_2[1];
  uVar4 = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x28) = uVar5;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar4;
  return;
}

~~~
