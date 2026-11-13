# 00c3cddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00c3cddc",
  "name": "FUN_00c3cddc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f565b9ac631e6ef9ce58d928405b84b1bb76969478079c9eabffecccd10c9194",
  "source_text_sha256": "f565b9ac631e6ef9ce58d928405b84b1bb76969478079c9eabffecccd10c9194"
}
~~~

## 呼び出し元

- [00c3a214](../00c3a/00c3a214.md)

## 呼び出し先

- [00c580f0](../00c58/00c580f0.md)
- [00c5a0f0](../00c5a/00c5a0f0.md)

## 疑似コード / UTF-8 1296 bytes

~~~c

void FUN_00c3cddc(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
                    /* try { // try from 00c3cde4 to 00d3cdeb has its CatchHandler @ 00c3d174 */
  pvVar3 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00c3cdf4 to 00d3cdff has its CatchHandler @ 00c3d118 */
  lVar2 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00c3ce00 to 00d3ce9b has its CatchHandler @ 00c3cb74 */
  puVar1 = pvVar3;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar2 = 0;
    *puVar1 = pvVar3;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c99760;
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
