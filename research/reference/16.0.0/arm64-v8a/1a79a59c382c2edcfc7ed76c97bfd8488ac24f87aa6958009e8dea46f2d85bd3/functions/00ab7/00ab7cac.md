# 00ab7cac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0161.md#review-eed2ca62cb98a36ba1bded07a933ae4e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ab7cac",
  "name": "FUN_00ab7cac",
  "size": 540,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35006a8305655a0f6249d86bb946ef2acc38b3bec5b169c540eefea63a7ebd9b",
  "source_text_sha256": "35006a8305655a0f6249d86bb946ef2acc38b3bec5b169c540eefea63a7ebd9b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0046c984](../0046c/0046c984.md)
- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [00800320](../00800/00800320.md)
- [00800338](../00800/00800338.md)
- [008005ec](../00800/008005ec.md)
- [008070c4](../00807/008070c4.md)
- [0085b294](../0085b/0085b294.md)
- [008b9134](../008b9/008b9134.md)
- [008b924c](../008b9/008b924c.md)
- [009dcca4](../009dc/009dcca4.md)
- [00ab8fbc](../00ab8/00ab8fbc.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 3580 bytes

~~~c

void FUN_00ab7cac(long param_1,undefined8 *param_2)

{
  undefined4 *puVar1;
  int iVar2;
  long lVar3;
  int iVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  int iVar7;
  ulong uVar8;
  long lVar9;
  undefined8 uVar10;
  undefined1 auStack_78 [8];
  void *local_70;
  void *local_68;
  long local_48;
  
                    /* try { // try from 00ab7cb4 to 00bb7dbf has its CatchHandler @ 00ab7c48 */
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  uVar10 = *param_2;
  lVar9 = *(long *)(param_1 + 8);
  iVar4 = FUN_008b924c(uVar10);
  if ((iVar4 != 0) && (iVar4 = FUN_008b924c(uVar10), iVar4 != 2)) {
    iVar4 = FUN_0046c984(lVar9);
    iVar7 = *(int *)((long)&fde_table_entry_00333c08.data_loc + lVar9);
    if (iVar4 < 0) {
      iVar4 = iVar4 + 1;
    }
    iVar2 = iVar7 + 3;
    if (-1 < iVar7) {
      iVar2 = iVar7;
    }
    uVar8 = FUN_009dcca4(lVar9,(iVar7 % 4) * 0x7f + (iVar4 >> 1) + -0xf6,(iVar2 >> 2) * 0x5a + 0x150
                         ,0x70,0x58);
    if ((uVar8 & 1) != 0) {
      *(undefined1 *)((long)&fde_table_entry_00332a28.initial_loc + lVar9 + 1) = 1;
      uVar8 = FUN_0085b294(lVar9);
      if ((uVar8 & 1) != 0) {
        puVar1 = (undefined4 *)((long)&fde_table_entry_00333970.data_loc + lVar9);
                    /* catch() { ... } // from try @ 00ab7ca8 with catch @ 00ab7d78 */
        uVar5 = FUN_00800320(*puVar1);
        if (*(int *)(lVar9 + 0x8dc) == *(int *)((long)&fde_table_entry_00333c08.data_loc + lVar9)) {
          iVar4 = *(int *)(lVar9 + 0x8e4);
          *(undefined4 *)(lVar9 + 0x8dc) = 0xffffffff;
          uVar6 = FUN_00800338();
          uVar5 = FUN_008005ec(uVar5);
          iVar7 = FUN_008070c4(uVar6,uVar5,0,0);
          if (iVar7 < iVar4) {
            uVar10 = FUN_0047acb4();
            if (*(long *)(lVar3 + 0x28) == local_48) {
              FUN_0047cd94(uVar10,0xf,0);
              return;
            }
          }
          else {
            *(undefined1 *)(lVar9 + 0x921) = 1;
            *(undefined4 *)((long)&fde_table_entry_00331680.initial_loc + lVar9) =
                 *(undefined4 *)(lVar9 + 0x8e4);
            if (*(long *)(lVar3 + 0x28) == local_48) {
                    /* try { // try from 00ab7ea8 to 00bb7ec3 has its CatchHandler @ 00ab7ed4 */
              FUN_008b9134(uVar10);
              return;
            }
          }
          goto LAB_00ab7ec4;
        }
        FUN_00ab8fbc(auStack_78,&uleb128_0029a6e0 + lVar9,*puVar1,
                     *(undefined4 *)((long)&fde_table_entry_00333c08.initial_loc + lVar9));
        local_68 = local_70;
        *(undefined4 *)(lVar9 + 0x8e4) =
             (&DAT_00ca3d8c)
             [*(int *)((long)local_70 +
                      (long)*(int *)((long)&fde_table_entry_00333c08.data_loc + lVar9) * 4)];
        _ZdlPv(local_70);
        uVar5 = *(undefined4 *)((long)&fde_table_entry_00333c08.data_loc + lVar9);
        *(undefined4 *)(lVar9 + 0x8e0) = 0;
        *(undefined4 *)(lVar9 + 0x8dc) = uVar5;
        uVar10 = FUN_0047acb4();
        FUN_0047cd94(uVar10,10,0);
      }
    }
  }
                    /* try { // try from 00ab7e60 to 00bb7ea7 has its CatchHandler @ 00ab7e60
                       catch() { ... } // from try @ 00ab7e60 with catch @ 00ab7e60
                       catch() { ... } // from try @ 00ab7ec4 with catch @ 00ab7e60 */
  if (*(long *)(lVar3 + 0x28) == local_48) {
    return;
  }
LAB_00ab7ec4:
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00ab7ec4 to 00bb7ee7 has its CatchHandler @ 00ab7e60 */
  __stack_chk_fail();
}

~~~
