# 00adb9dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adb914`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb914.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/alignment_unresolved-0001.md#compare-193ef5575f7590fbd1813f085c148a22)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adb9dc",
  "name": "FUN_00adb9dc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7cdc4072a912f287d5a993e6fac7487fa226f6c14d1ff5d841c709f9a16d0691",
  "source_text_sha256": "7cdc4072a912f287d5a993e6fac7487fa226f6c14d1ff5d841c709f9a16d0691"
}
~~~

## 呼び出し元

- [00adacc8](../00ada/00adacc8.md)
- [00adad88](../00ada/00adad88.md)
- [00adae94](../00ada/00adae94.md)

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)

## 疑似コード / UTF-8 1838 bytes

~~~c

long * FUN_00adb9dc(long param_1,byte *param_2)

{
  void *pvVar1;
  long lVar2;
  ulong uVar3;
  size_t sVar4;
  ulong uVar5;
  byte *__s2;
  bool bVar6;
  int iVar7;
  long *plVar8;
  long *plVar9;
  long *plVar10;
  
                    /* catch() { ... } // from try @ 00adb54c with catch @ 00adb9e4 */
                    /* catch() { ... } // from try @ 00adb53c with catch @ 00adb9e8 */
  plVar8 = (long *)(param_1 + 8);
  plVar10 = (long *)*plVar8;
  if (plVar10 != (long *)0x0) {
    uVar5 = *(ulong *)(param_2 + 8);
    __s2 = *(byte **)(param_2 + 0x10);
    plVar9 = plVar8;
    if ((*param_2 & 1) == 0) {
      __s2 = param_2 + 1;
      uVar5 = (ulong)(*param_2 >> 1);
    }
    do {
      pvVar1 = (void *)((long)plVar10 + 0x21);
      uVar3 = (ulong)(*(byte *)(plVar10 + 4) >> 1);
      if ((*(byte *)(plVar10 + 4) & 1) != 0) {
        pvVar1 = (void *)plVar10[6];
        uVar3 = plVar10[5];
      }
      sVar4 = uVar5;
      if (uVar3 <= uVar5) {
        sVar4 = uVar3;
      }
      iVar7 = memcmp(pvVar1,__s2,sVar4);
      bVar6 = uVar3 < uVar5;
      if (iVar7 != 0) {
        bVar6 = iVar7 < 0;
      }
      lVar2 = 8;
      if (!bVar6) {
        lVar2 = 0;
        plVar9 = plVar10;
      }
      plVar10 = *(long **)((long)plVar10 + lVar2);
    } while (plVar10 != (long *)0x0);
    if (plVar9 != plVar8) {
      uVar3 = (ulong)(*(byte *)(plVar9 + 4) >> 1);
      pvVar1 = (void *)((long)plVar9 + 0x21);
      if ((*(byte *)(plVar9 + 4) & 1) != 0) {
        uVar3 = plVar9[5];
        pvVar1 = (void *)plVar9[6];
      }
      sVar4 = uVar3;
      if (uVar5 <= uVar3) {
        sVar4 = uVar5;
      }
      iVar7 = memcmp(__s2,pvVar1,sVar4);
      bVar6 = uVar5 < uVar3;
      if (iVar7 != 0) {
        bVar6 = iVar7 < 0;
      }
      if (!bVar6) {
        plVar8 = plVar9;
      }
    }
  }
  return plVar8;
}

~~~
