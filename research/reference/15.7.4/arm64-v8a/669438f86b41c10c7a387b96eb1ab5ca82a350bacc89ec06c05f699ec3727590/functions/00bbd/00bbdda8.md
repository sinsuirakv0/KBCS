# 00bbdda8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bbdda8",
  "name": "FUN_00bbdda8",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00f27cd095b4476f2db0815c911732569118e349223c58c32c8728d9b9e55a55",
  "source_text_sha256": "00f27cd095b4476f2db0815c911732569118e349223c58c32c8728d9b9e55a55"
}
~~~

## 呼び出し元

- [00bbcc10](../00bbc/00bbcc10.md)
- [00bbd308](../00bbd/00bbd308.md)

## 呼び出し先

- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

## 疑似コード / UTF-8 1611 bytes

~~~c

undefined8 * FUN_00bbdda8(long param_1,char *param_2,undefined8 *param_3)

{
  undefined8 *puVar1;
  size_t sVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  void *pvVar6;
  
                    /* try { // try from 00bbddb8 to 00cbddbf has its CatchHandler @ 00bbe198 */
  pvVar6 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbddc0 to 00cbddc7 has its CatchHandler @ 00bbe02c */
  lVar3 = *(long *)((long)pvVar6 + 8);
  puVar1 = pvVar6;
  if (lVar3 - 0xfc0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar3 = 0;
    *puVar1 = pvVar6;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
                    /* try { // try from 00bbde04 to 00cbde0f has its CatchHandler @ 00bbe028 */
  *(long *)((long)puVar1 + 8) = lVar3 + 0x30;
  sVar2 = strlen(param_2);
                    /* try { // try from 00bbde10 to 00cbde1f has its CatchHandler @ 00bbe014 */
  uVar4 = *param_3;
  puVar5 = (undefined8 *)((long)puVar1 + lVar3 + 0x10);
  *puVar5 = &PTR_FUN_00c177a8;
                    /* try { // try from 00bbde20 to 00cbde33 has its CatchHandler @ 00bbdffc */
  *(char **)((long)puVar1 + lVar3 + 0x20) = param_2;
  *(size_t *)((long)puVar1 + lVar3 + 0x28) = sVar2;
  *(undefined1 *)((long)puVar1 + lVar3 + 0x18) = 0x15;
  *(ushort *)((long)puVar1 + lVar3 + 0x19) =
       *(ushort *)((long)puVar1 + lVar3 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar3 + 0x30) = uVar4;
  return puVar5;
}

~~~
