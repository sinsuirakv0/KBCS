# 00adb5fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adb5fc.md)

## 関数情報

~~~json
{
  "address": "00adb5fc",
  "name": "FUN_00adb5fc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "127c4855a7c0b2114604d32c4670deaa063cc27b533b843c90106b21a0378a38",
  "source_text_sha256": "127c4855a7c0b2114604d32c4670deaa063cc27b533b843c90106b21a0378a38"
}
~~~
## 呼び出し元

- [00adb4c4](../00adb/00adb4c4.md)

## 呼び出し先

- [00bdb100](../00bdb/00bdb100.md)

## 疑似コード 1/1 / UTF-8 1957 bytes

~~~c

long * FUN_00adb5fc(long param_1,undefined8 *param_2,byte *param_3)

{
  void *__s2;
  size_t __n;
  ulong uVar1;
  byte *__s1;
  bool bVar2;
  ulong uVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  
  plVar6 = (long *)(param_1 + 8);
  plVar5 = (long *)*plVar6;
  plVar7 = plVar6;
  if (plVar5 != (long *)0x0) {
    uVar1 = *(ulong *)(param_3 + 8);
    __s1 = *(byte **)(param_3 + 0x10);
    if ((*param_3 & 1) == 0) {
      __s1 = param_3 + 1;
      uVar1 = (ulong)(*param_3 >> 1);
    }
    do {
      while( true ) {
        plVar7 = plVar5;
                    /* try { // try from 00adb65c to 00bdb663 has its CatchHandler @ 00adb8dc */
                    /* try { // try from 00adb664 to 00bdb6b7 has its CatchHandler @ 00adafd0 */
        __s2 = (void *)((long)plVar7 + 0x21);
        uVar3 = (ulong)(*(byte *)(plVar7 + 4) >> 1);
        if ((*(byte *)(plVar7 + 4) & 1) != 0) {
          __s2 = (void *)plVar7[6];
          uVar3 = plVar7[5];
        }
        __n = uVar3;
        if (uVar1 <= uVar3) {
          __n = uVar1;
        }
        iVar4 = memcmp(__s1,__s2,__n);
        bVar2 = uVar1 < uVar3;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
        if (bVar2) break;
        iVar4 = memcmp(__s2,__s1,__n);
                    /* try { // try from 00adb6b8 to 00bdb6c3 has its CatchHandler @ 00adb9b4 */
        bVar2 = uVar3 < uVar1;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
                    /* try { // try from 00adb6c4 to 00bdba33 has its CatchHandler @ 00adafd0 */
        if (!bVar2) goto LAB_00adb6e0;
        plVar6 = plVar7 + 1;
        plVar5 = (long *)*plVar6;
        if ((long *)*plVar6 == (long *)0x0) goto LAB_00adb6e0;
      }
      plVar5 = (long *)*plVar7;
      plVar6 = plVar7;
    } while ((long *)*plVar7 != (long *)0x0);
  }
LAB_00adb6e0:
  *param_2 = plVar7;
  return plVar6;
}

~~~
