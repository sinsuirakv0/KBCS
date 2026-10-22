# 00bb9bac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bb9bac.md)

## 関数情報

~~~json
{
  "address": "00bb9bac",
  "name": "FUN_00bb9bac",
  "size": 268,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a475acc83716e8a86887cbc399562fd7f46e3baef07d9fcde45f791841287a91",
  "source_text_sha256": "a475acc83716e8a86887cbc399562fd7f46e3baef07d9fcde45f791841287a91"
}
~~~
## 呼び出し元

- [00b8d1a8](../00b8d/00b8d1a8.md)
- [00b90628](../00b90/00b90628.md)

## 呼び出し先

- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)
- [00bdb170](../00bdb/00bdb170.md)
- [00be1470](../00be1/00be1470.md)
- [00be1ca0](../00be1/00be1ca0.md)

## 疑似コード 1/1 / UTF-8 1337 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

double FUN_00bb9bac(char *param_1,char *param_2,undefined4 *param_3)

{
  int iVar1;
  int iVar2;
  int *piVar3;
  double dVar4;
  double dVar5;
  char *local_48;
  
  dVar5 = _DAT_002b1870;
  if (param_1 == param_2) {
                    /* try { // try from 00bb9c34 to 00cb9ca7 has its CatchHandler @ 00bbad98 */
    *param_3 = 4;
  }
  else {
    piVar3 = (int *)__errno();
    iVar1 = *piVar3;
    *piVar3 = 0;
                    /* try { // try from 00bb9be8 to 00cb9bfb has its CatchHandler @ 00bbaaf0 */
    if (((DAT_010a2898 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_010a2898), iVar2 != 0)) {
      DAT_010a2890 = newlocale(0x1fbf,"C",(__locale_t)0x0);
      __cxa_guard_release(&DAT_010a2898);
    }
    dVar4 = strtold_l(param_1,&local_48,DAT_010a2890);
    if (*piVar3 == 0) {
      *piVar3 = iVar1;
      dVar5 = _DAT_002b1870;
      if (local_48 == param_2) {
        return dVar4;
      }
    }
    else {
      dVar5 = _DAT_002b1870;
                    /* try { // try from 00bb9c28 to 00cb9c33 has its CatchHandler @ 00bbad64 */
      if ((local_48 == param_2) && (dVar5 = dVar4, *piVar3 != 0x22)) {
        return dVar4;
      }
    }
    *param_3 = 4;
  }
  return dVar5;
}

~~~
