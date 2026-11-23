# 00a9abdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a3cce8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cce8.md) · 移動量 `+0x5def4`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0051.md#compare-05e7b36133f6cce308504705fb2c9cda)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9abdc",
  "name": "FUN_00a9abdc",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4fd6fd907f67fb8444b1af77b193780eb54cf747bd116f880f117e4ef6f0a48",
  "source_text_sha256": "b4fd6fd907f67fb8444b1af77b193780eb54cf747bd116f880f117e4ef6f0a48"
}
~~~

## 呼び出し元

- [00a8e3bc](../00a8e/00a8e3bc.md)
- [00a917e4](../00a91/00a917e4.md)

## 呼び出し先

- [00764344](../00764/00764344.md)
- [00887790](../00887/00887790.md)
- [00887798](../00887/00887798.md)
- [008877a0](../00887/008877a0.md)
- [00b32d28](../00b32/00b32d28.md)
- [00b358d8](../00b35/00b358d8.md)
- [00b38f88](../00b38/00b38f88.md)
- [00b390b8](../00b39/00b390b8.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"jkdblt56ptkw"
~~~

## 疑似コード / UTF-8 1614 bytes

~~~c

void FUN_00a9abdc(long param_1,char *param_2)

{
  char *pcVar1;
  long lVar2;
  long lVar3;
  undefined8 uVar4;
  byte local_50;
  char local_4f [8];
  undefined4 local_47;
  undefined1 local_43;
  char *local_40;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  lVar3 = *(long *)(param_1 + 8);
  if (*param_2 == '\0') {
    FUN_00b390b8(0);
    FUN_00b358d8(0);
    FUN_00887790(*(undefined8 *)(lVar3 + 0x22a0),0);
  }
  else {
    FUN_00b390b8(1);
    FUN_00b358d8(1);
    FUN_00887790(*(undefined8 *)(lVar3 + 0x22a0),1);
    local_50 = 0x18;
    local_47 = 0x776b7470;
    local_4f[0] = s_jkdblt56ptkw_002af15d[0];
    local_4f[1] = s_jkdblt56ptkw_002af15d[1];
    local_4f[2] = s_jkdblt56ptkw_002af15d[2];
    local_4f[3] = s_jkdblt56ptkw_002af15d[3];
    local_4f[4] = s_jkdblt56ptkw_002af15d[4];
    local_4f[5] = s_jkdblt56ptkw_002af15d[5];
    local_4f[6] = s_jkdblt56ptkw_002af15d[6];
    local_4f[7] = s_jkdblt56ptkw_002af15d[7];
    local_43 = 0;
    FUN_00b32d28(&local_50,&DAT_01123d08);
    if ((local_50 & 1) != 0) {
      _ZdlPv(local_40);
    }
  }
  FUN_00b38f88(*(int *)(lVar3 + 0x1dd8) == -1);
  FUN_00887798(*(undefined8 *)(lVar3 + 0x22a0),*(int *)(lVar3 + 0x1dd8) == -1);
  uVar4 = *(undefined8 *)(lVar3 + 0x22a0);
  FUN_00764344(&local_50,lVar3);
  pcVar1 = local_40;
  if ((local_50 & 1) == 0) {
    pcVar1 = local_4f;
  }
  FUN_008877a0(uVar4,pcVar1);
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
