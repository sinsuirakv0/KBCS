# 00ababd0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abab60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aba/00abab60.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0064.md#compare-33759bc39f88ed796e17258643689ef3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0076.md#compare-cb0801467a300418ebcc0b4149a40e09)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ababd0",
  "name": "FUN_00ababd0",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0a5d7a715e7299efb119dc5d9fa16ce3bdf2317732f130f7be9fc50e2fd8254d",
  "source_text_sha256": "0a5d7a715e7299efb119dc5d9fa16ce3bdf2317732f130f7be9fc50e2fd8254d"
}
~~~

## 呼び出し元

- [005fe6ac](../005fe/005fe6ac.md)

## 呼び出し先

- [00851550](../00851/00851550.md)
- [00ab9228](../00ab9/00ab9228.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 疑似コード / UTF-8 2370 bytes

~~~c

void FUN_00ababd0(int param_1,int param_2)

{
  int iVar1;
  int iVar2;
  long lVar3;
  undefined *puVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  int iVar8;
  int local_98 [2];
  void *local_90;
  void *local_88;
  long local_68;
  
                    /* try { // try from 00ababe0 to 00bbad53 has its CatchHandler @ 00aba9b0 */
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  if ((param_1 == 3) ||
     (lVar6 = FUN_00851550(), puVar4 = PTR_DAT_00c9b5a0, lVar6 = lVar6 + (long)param_1 * 0x18,
     (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) - *(long *)(&uleb128_0029a6e0 + lVar6)) >> 4
          ) * -0x55555555 < 1)) {
    iVar5 = 0;
  }
  else {
    iVar8 = 0;
    do {
      lVar6 = 0;
      while( true ) {
        lVar7 = FUN_00851550();
                    /* catch() { ... } // from try @ 00ababc8 with catch @ 00abac6c */
        FUN_00ab9228(local_98,&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        lVar7 = (long)local_98[0];
        if (local_90 != (void *)0x0) {
          local_88 = local_90;
          _ZdlPv(local_90);
        }
        if (lVar7 <= lVar6) break;
        lVar7 = FUN_00851550();
        FUN_00ab9228(local_98,&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        iVar1 = *(int *)(puVar4 + (long)param_2 * 4);
                    /* catch() { ... } // from try @ 00abaaa4 with catch @ 00abacb0 */
        iVar2 = *(int *)((long)local_90 + lVar6 * 4);
        local_88 = local_90;
        _ZdlPv(local_90);
        lVar6 = lVar6 + 1;
        iVar5 = iVar8;
        if (iVar2 == iVar1) goto LAB_00abad14;
      }
                    /* catch() { ... } // from try @ 00abaa80 with catch @ 00abaccc */
      iVar8 = iVar8 + 1;
      lVar6 = FUN_00851550();
                    /* catch() { ... } // from try @ 00abaafc with catch @ 00abacd4 */
      lVar6 = lVar6 + (long)param_1 * 0x18;
                    /* catch() { ... } // from try @ 00ababa8 with catch @ 00abacdc */
                    /* catch() { ... } // from try @ 00abab20 with catch @ 00abace4 */
      iVar5 = 0;
    } while (iVar8 < (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) -
                                  *(long *)(&uleb128_0029a6e0 + lVar6)) >> 4) * -0x55555555);
  }
LAB_00abad14:
  if (*(long *)(lVar3 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(iVar5);
  }
  return;
}

~~~
