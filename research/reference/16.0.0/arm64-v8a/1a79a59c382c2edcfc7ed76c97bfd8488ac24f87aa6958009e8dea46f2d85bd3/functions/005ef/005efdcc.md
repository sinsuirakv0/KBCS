# 005efdcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0111.md#review-558a74d939d111b12f3421af213875b6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005efdcc",
  "name": "FUN_005efdcc",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d2a27ed9070afd5d2e9fb6fe7a40d2a24e20bd22d5f02995e439a0953438ef7",
  "source_text_sha256": "2d2a27ed9070afd5d2e9fb6fe7a40d2a24e20bd22d5f02995e439a0953438ef7"
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)
- [00720050](../00720/00720050.md)
- [00a47d08](../00a47/00a47d08.md)
- [00a51580](../00a51/00a51580.md)

## 呼び出し先

- [005ed758](../005ed/005ed758.md)
- [00936428](../00936/00936428.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"battle_zoom_castle_y"
~~~

## 疑似コード / UTF-8 2523 bytes

~~~c

void FUN_005efdcc(long param_1)

{
  undefined4 uVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  undefined8 uVar6;
  int iVar7;
  int iVar8;
  byte local_70;
  char local_6f [8];
  undefined7 uStack_67;
  char cStack_60;
  undefined4 uStack_5f;
  undefined1 uStack_5b;
  undefined2 uStack_5a;
  long local_58;
  
  uVar6 = s_battle_zoom_castle_y_002b3d1f._8_8_;
  local_6f = (char  [8])s_battle_zoom_castle_y_002b3d1f._0_8_;
                    /* try { // try from 005efde4 to 006efe3f has its CatchHandler @ 005efde4
                       catch() { ... } // from try @ 005efde4 with catch @ 005efde4
                       catch() { ... } // from try @ 005efe48 with catch @ 005efde4
                       catch() { ... } // from try @ 005efee4 with catch @ 005efde4
                       catch() { ... } // from try @ 005f00f0 with catch @ 005efde4
                       catch() { ... } // from try @ 005f01b4 with catch @ 005efde4
                       catch() { ... } // from try @ 005f023c with catch @ 005efde4 */
  lVar5 = tpidr_el0;
  local_58 = *(long *)(lVar5 + 0x28);
  uVar1 = *(undefined4 *)(param_1 + 0x3534);
  iVar2 = *(int *)(param_1 + 0x359c);
  local_70 = 0x28;
  uStack_5f = 0x795f656c;
  *(undefined4 *)(param_1 + 0x3534) = 10000;
  uStack_67 = (undefined7)uVar6;
  cStack_60 = SUB81(uVar6,7);
  uStack_5b = 0;
                    /* try { // try from 005efe40 to 006efe47 has its CatchHandler @ 005f02ac */
  iVar7 = FUN_00936428(param_1 + 0x1588,&local_70,0);
                    /* try { // try from 005efe48 to 006efea3 has its CatchHandler @ 005efde4 */
  if (*(char *)(param_1 + 0x14ed) == '\0') {
    iVar8 = 0;
  }
  else {
    iVar8 = FUN_005ed758(param_1);
  }
  iVar3 = *(int *)(param_1 + 0x359c);
  iVar4 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + param_1);
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT26(uStack_5a,CONCAT15(uStack_5b,CONCAT41(uStack_5f,cStack_60))));
  }
  *(undefined4 *)(param_1 + 0x3534) = uVar1;
                    /* try { // try from 005efea4 to 006efeaf has its CatchHandler @ 005f0298 */
  iVar8 = (iVar8 - iVar3) + iVar4 + 0x8a;
  iVar3 = 0;
  if (iVar8 != 0) {
    iVar3 = ((iVar7 - iVar2) * 10000 + 0x11da50) / iVar8;
  }
  if (9999 < iVar3) {
    iVar3 = 10000;
  }
  if (*(long *)(lVar5 + 0x28) == local_58) {
                    /* try { // try from 005efedc to 006efee3 has its CatchHandler @ 005f027c */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(iVar3);
}

~~~
