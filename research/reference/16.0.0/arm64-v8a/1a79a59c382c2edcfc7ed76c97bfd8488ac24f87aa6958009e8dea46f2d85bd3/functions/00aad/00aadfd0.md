# 00aadfd0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aadfd0",
  "name": "FUN_00aadfd0",
  "size": 268,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4bcc36f1cf5a4b7d1dc7a01680c5248d1f6f7989b02d86ff9c538f8c7031d28f",
  "source_text_sha256": "4bcc36f1cf5a4b7d1dc7a01680c5248d1f6f7989b02d86ff9c538f8c7031d28f"
}
~~~

## 呼び出し元

- [00aa76e4](../00aa7/00aa76e4.md)
- [00aa82a8](../00aa8/00aa82a8.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [0043bb64](../0043b/0043bb64.md)
- [00aae100](../00aae/00aae100.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 2433 bytes

~~~c

undefined8 * FUN_00aadfd0(long *param_1,undefined8 param_2,undefined8 param_3,undefined4 *param_4)

{
  byte bVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined8 uVar7;
  undefined1 auStack_70 [8];
  undefined8 local_68;
  undefined8 *local_60;
  long *plStack_58;
  undefined1 local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
                    /* try { // try from 00aadff0 to 00badff7 has its CatchHandler @ 00aae0a8 */
  local_48 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00aadff8 to 00bae0cf has its CatchHandler @ 00aadf94 */
  puVar3 = (undefined8 *)FUN_00aae100(param_1,param_2,&local_68,auStack_70,param_3);
  puVar6 = (undefined8 *)*puVar3;
  if (puVar6 == (undefined8 *)0x0) {
    puVar6 = (undefined8 *)_Znwm(0x40);
    bVar1 = *(byte *)(param_4 + 2);
    local_50 = 0;
    *(undefined4 *)(puVar6 + 4) = *param_4;
    local_60 = puVar6;
    plStack_58 = param_1 + 1;
    if ((bVar1 & 1) == 0) {
      uVar7 = *(undefined8 *)(param_4 + 2);
      uVar4 = *(undefined8 *)(param_4 + 6);
      puVar6[6] = *(undefined8 *)(param_4 + 4);
      puVar6[5] = uVar7;
      puVar6[7] = uVar4;
    }
    else {
      FUN_0043bae0(puVar6 + 5,*(undefined8 *)(param_4 + 6),*(undefined8 *)(param_4 + 4));
    }
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = local_68;
    *puVar3 = puVar6;
    puVar5 = puVar6;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar5 = (undefined8 *)*puVar3;
    }
    puVar3 = (undefined8 *)FUN_0043bb64(param_1[1],puVar5);
    uVar4 = 1;
                    /* catch() { ... } // from try @ 00aadff0 with catch @ 00aae0a8 */
    param_1[2] = param_1[2] + 1;
  }
  else {
    uVar4 = 0;
  }
  if (*(long *)(lVar2 + 0x28) == local_48) {
                    /* try { // try from 00aae0d0 to 00bae13f has its CatchHandler @ 00aae0d0
                       catch() { ... } // from try @ 00aae0d0 with catch @ 00aae0d0
                       catch() { ... } // from try @ 00aae194 with catch @ 00aae0d0
                       catch() { ... } // from try @ 00aae200 with catch @ 00aae0d0
                       catch() { ... } // from try @ 00aae2b0 with catch @ 00aae0d0
                       catch() { ... } // from try @ 00aae404 with catch @ 00aae0d0 */
    return puVar6;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(puVar3,uVar4);
}

~~~
