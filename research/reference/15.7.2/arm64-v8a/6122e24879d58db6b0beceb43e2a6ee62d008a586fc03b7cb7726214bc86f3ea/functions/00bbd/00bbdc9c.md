# 00bbdc9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbdc9c.md)

## 関数情報

~~~json
{
  "address": "00bbdc9c",
  "name": "FUN_00bbdc9c",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d01464f985326215edcc110087bf63ee268baa7bbf607ce9ef7d21fc6c310d9",
  "source_text_sha256": "2d01464f985326215edcc110087bf63ee268baa7bbf607ce9ef7d21fc6c310d9"
}
~~~
## 呼び出し元

- [00bbcb04](../00bbc/00bbcb04.md)
- [00bbd1fc](../00bbd/00bbd1fc.md)

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

## 疑似コード 1/1 / UTF-8 1654 bytes

~~~c

undefined8 * FUN_00bbdc9c(long param_1,char *param_2,undefined8 *param_3)

{
  undefined8 *puVar1;
  size_t sVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  void *pvVar6;
  
                    /* try { // try from 00bbdcac to 00cbdcb3 has its CatchHandler @ 00bbe08c */
  pvVar6 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbdcb4 to 00cbdcbb has its CatchHandler @ 00bbdf20 */
  lVar3 = *(long *)((long)pvVar6 + 8);
  puVar1 = pvVar6;
  if (lVar3 - 0xfc0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      std::terminate();
    }
    lVar3 = 0;
    *puVar1 = pvVar6;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
                    /* try { // try from 00bbdcf8 to 00cbdd03 has its CatchHandler @ 00bbdf1c */
  *(long *)((long)puVar1 + 8) = lVar3 + 0x30;
  sVar2 = strlen(param_2);
                    /* try { // try from 00bbdd04 to 00cbdd13 has its CatchHandler @ 00bbdf08 */
  uVar4 = *param_3;
  puVar5 = (undefined8 *)((long)puVar1 + lVar3 + 0x10);
  *puVar5 = &PTR_FUN_00c176a8;
                    /* try { // try from 00bbdd14 to 00cbdd27 has its CatchHandler @ 00bbdef0 */
  *(char **)((long)puVar1 + lVar3 + 0x20) = param_2;
  *(size_t *)((long)puVar1 + lVar3 + 0x28) = sVar2;
  *(undefined1 *)((long)puVar1 + lVar3 + 0x18) = 0x15;
  *(ushort *)((long)puVar1 + lVar3 + 0x19) =
       *(ushort *)((long)puVar1 + lVar3 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar3 + 0x30) = uVar4;
  return puVar5;
}

~~~
