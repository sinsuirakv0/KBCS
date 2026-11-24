# 007cffdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `007cffdc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cffdc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0028.md#compare-59e522efb7f71ba87cc5dffcdc9393ef)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0057.md#review-c3cc2bea2dc7129d18f9ecbc98ecd849)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007cffdc",
  "name": "FUN_007cffdc",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4486bdce8a96cfb25cfb89da48a68ff2b199baccd2a992a51b987b6b41eda3c",
  "source_text_sha256": "f4486bdce8a96cfb25cfb89da48a68ff2b199baccd2a992a51b987b6b41eda3c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007cffdc",
        "007d00cf"
      ]
    ],
    "bytes_sha256": "4392bc9a8f3f7adf0561d14d4b928ada31fad5e216faef699ca52447566a1c4f",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007cffa8](../007cf/007cffa8.md)
- [007d0be0](../007d0/007d0be0.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0081f580](../0081f/0081f580.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb240](../00bdb/00bdb240.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1817 bytes

~~~c

bool FUN_007cffdc(int param_1,int param_2)

{
  long lVar1;
  byte *pbVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  
  if (param_1 == -10) {
    return true;
  }
  lVar1 = FUN_0081f580();
  pbVar3 = *(byte **)(BYTE_ARRAY_003975f1 + lVar1 + 0x17);
  if (*(byte **)(BYTE_ARRAY_003975f1 + lVar1 + 0x17) == (byte *)0x0) {
    pbVar4 = BYTE_ARRAY_003975f1 + lVar1 + 0x17;
    pbVar5 = BYTE_ARRAY_003975f1 + lVar1 + 0x17;
  }
  else {
    do {
      while (pbVar2 = pbVar3, pbVar4 = pbVar2, *(int *)(pbVar2 + 0x1c) <= param_1) {
        if (param_1 <= *(int *)(pbVar2 + 0x1c)) goto LAB_007d00ac;
        pbVar3 = *(byte **)(pbVar2 + 8);
        if (*(byte **)(pbVar2 + 8) == (byte *)0x0) {
          pbVar5 = pbVar2 + 8;
          goto LAB_007d0050;
        }
      }
      pbVar3 = *(byte **)pbVar2;
      pbVar5 = pbVar2;
    } while (*(byte **)pbVar2 != (byte *)0x0);
  }
LAB_007d0050:
  pbVar2 = (byte *)_Znwm(0x1f60);
  *(int *)(pbVar2 + 0x1c) = param_1;
  memset(pbVar2 + 0x20,0,8000);
  pbVar2[0] = 0;
  pbVar2[1] = 0;
  pbVar2[2] = 0;
  pbVar2[3] = 0;
  pbVar2[4] = 0;
  pbVar2[5] = 0;
  pbVar2[6] = 0;
  pbVar2[7] = 0;
  pbVar2[8] = 0;
  pbVar2[9] = 0;
  pbVar2[10] = 0;
  pbVar2[0xb] = 0;
  pbVar2[0xc] = 0;
  pbVar2[0xd] = 0;
  pbVar2[0xe] = 0;
  pbVar2[0xf] = 0;
  *(byte **)(pbVar2 + 0x10) = pbVar4;
  *(byte **)pbVar5 = pbVar2;
  pbVar3 = pbVar2;
  if (**(long **)(BYTE_ARRAY_003975f1 + lVar1 + 0xf) != 0) {
    *(long *)(BYTE_ARRAY_003975f1 + lVar1 + 0xf) = **(long **)(BYTE_ARRAY_003975f1 + lVar1 + 0xf);
    pbVar3 = *(byte **)pbVar5;
  }
  FUN_00419064(*(undefined8 *)(BYTE_ARRAY_003975f1 + lVar1 + 0x17),pbVar3);
  *(long *)(BYTE_ARRAY_003975f1 + lVar1 + 0x1f) = *(long *)(BYTE_ARRAY_003975f1 + lVar1 + 0x1f) + 1;
LAB_007d00ac:
  return *(int *)(pbVar2 + (long)param_2 * 0x10 + 0x2c) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007cffdc"></a> `007cffdc` | `1f 28 00 31` | cmn w0,#0xa | `FALL_THROUGH`
<a id="insn-007cffe0"></a> `007cffe0` | `61 00 00 54` | b.ne 0x007cffec | `CONDITIONAL_JUMP`
<a id="insn-007cffe4"></a> `007cffe4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007cffe8"></a> `007cffe8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007cffec"></a> `007cffec` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-007cfff0"></a> `007cfff0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007cfff4"></a> `007cfff4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007cfff8"></a> `007cfff8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007cfffc"></a> `007cfffc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007d0000"></a> `007d0000` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-007d0004"></a> `007d0004` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-007d0008"></a> `007d0008` | `5e 3d 01 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-007d000c"></a> `007d000c` | `16 5c 4e 91` | add x22,x0,#0x397, LSL #12 | `FALL_THROUGH`
<a id="insn-007d0010"></a> `007d0010` | `c8 06 43 f9` | ldr x8,[x22, #0x608] | `FALL_THROUGH`
<a id="insn-007d0014"></a> `007d0014` | `e8 00 00 b5` | cbnz x8,0x007d0030 | `CONDITIONAL_JUMP`
<a id="insn-007d0018"></a> `007d0018` | `d7 22 18 91` | add x23,x22,#0x608 | `FALL_THROUGH`
<a id="insn-007d001c"></a> `007d001c` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-007d0020"></a> `007d0020` | `0c 00 00 14` | b 0x007d0050 | `UNCONDITIONAL_JUMP`
<a id="insn-007d0024"></a> `007d0024` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-007d0028"></a> `007d0028` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-007d002c"></a> `007d002c` | `28 01 00 b4` | cbz x8,0x007d0050 | `CONDITIONAL_JUMP`
<a id="insn-007d0030"></a> `007d0030` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-007d0034"></a> `007d0034` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-007d0038"></a> `007d0038` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-007d003c"></a> `007d003c` | `4c ff ff 54` | b.gt 0x007d0024 | `CONDITIONAL_JUMP`
<a id="insn-007d0040"></a> `007d0040` | `6a 03 00 54` | b.ge 0x007d00ac | `CONDITIONAL_JUMP`
<a id="insn-007d0044"></a> `007d0044` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-007d0048"></a> `007d0048` | `48 ff ff b5` | cbnz x8,0x007d0030 | `CONDITIONAL_JUMP`
<a id="insn-007d004c"></a> `007d004c` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-007d0050"></a> `007d0050` | `00 ec 83 52` | mov w0,#0x1f60 | `FALL_THROUGH`
<a id="insn-007d0054"></a> `007d0054` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-007d0058"></a> `007d0058` | `fa 2b 10 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-007d005c"></a> `007d005c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007d0060"></a> `007d0060` | `15 1c 00 b9` | str w21,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-007d0064"></a> `007d0064` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-007d0068"></a> `007d0068` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007d006c"></a> `007d006c` | `02 e8 83 52` | mov w2,#0x1f40 | `FALL_THROUGH`
<a id="insn-007d0070"></a> `007d0070` | `74 2c 10 94` | bl 0x00bdb240 | `UNCONDITIONAL_CALL`
<a id="insn-007d0074"></a> `007d0074` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-007d0078"></a> `007d0078` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-007d007c"></a> `007d007c` | `98 0a 00 f9` | str x24,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-007d0080"></a> `007d0080` | `f4 02 00 f9` | str x20,[x23] | `FALL_THROUGH`
<a id="insn-007d0084"></a> `007d0084` | `c8 02 43 f9` | ldr x8,[x22, #0x600] | `FALL_THROUGH`
<a id="insn-007d0088"></a> `007d0088` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-007d008c"></a> `007d008c` | `68 00 00 b4` | cbz x8,0x007d0098 | `CONDITIONAL_JUMP`
<a id="insn-007d0090"></a> `007d0090` | `c8 02 03 f9` | str x8,[x22, #0x600] | `FALL_THROUGH`
<a id="insn-007d0094"></a> `007d0094` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-007d0098"></a> `007d0098` | `c0 06 43 f9` | ldr x0,[x22, #0x608] | `FALL_THROUGH`
<a id="insn-007d009c"></a> `007d009c` | `f2 23 f1 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-007d00a0"></a> `007d00a0` | `c8 0a 43 f9` | ldr x8,[x22, #0x610] | `FALL_THROUGH`
<a id="insn-007d00a4"></a> `007d00a4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-007d00a8"></a> `007d00a8` | `c8 0a 03 f9` | str x8,[x22, #0x610] | `FALL_THROUGH`
<a id="insn-007d00ac"></a> `007d00ac` | `88 d2 33 8b` | add x8,x20,w19, SXTW  #0x4 | `FALL_THROUGH`
<a id="insn-007d00b0"></a> `007d00b0` | `08 2d 40 b9` | ldr w8,[x8, #0x2c] | `FALL_THROUGH`
<a id="insn-007d00b4"></a> `007d00b4` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-007d00b8"></a> `007d00b8` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-007d00bc"></a> `007d00bc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007d00c0"></a> `007d00c0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007d00c4"></a> `007d00c4` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007d00c8"></a> `007d00c8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-007d00cc"></a> `007d00cc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007cffdc`](#insn-007cffdc) 範囲 `[['007cffdc', '007cffe3']]`
  - `CONDITIONAL_JUMP` [`007cffe0`](#insn-007cffe0) → [`007cffec`](#insn-007cffec)
  - `FALL_THROUGH` [`007cffe0`](#insn-007cffe0) → [`007cffe4`](#insn-007cffe4)
- ブロック [`007cffe4`](#insn-007cffe4) 範囲 `[['007cffe4', '007cffeb']]`
- ブロック [`007cffec`](#insn-007cffec) 範囲 `[['007cffec', '007d0017']]`
  - `CONDITIONAL_JUMP` [`007d0014`](#insn-007d0014) → [`007d0030`](#insn-007d0030)
  - `FALL_THROUGH` [`007d0014`](#insn-007d0014) → [`007d0018`](#insn-007d0018)
- ブロック [`007d0018`](#insn-007d0018) 範囲 `[['007d0018', '007d0023']]`
  - `UNCONDITIONAL_JUMP` [`007d0020`](#insn-007d0020) → [`007d0050`](#insn-007d0050)
- ブロック [`007d0024`](#insn-007d0024) 範囲 `[['007d0024', '007d002f']]`
  - `CONDITIONAL_JUMP` [`007d002c`](#insn-007d002c) → [`007d0050`](#insn-007d0050)
  - `FALL_THROUGH` [`007d002c`](#insn-007d002c) → [`007d0030`](#insn-007d0030)
- ブロック [`007d0030`](#insn-007d0030) 範囲 `[['007d0030', '007d003f']]`
  - `CONDITIONAL_JUMP` [`007d003c`](#insn-007d003c) → [`007d0024`](#insn-007d0024)
  - `FALL_THROUGH` [`007d003c`](#insn-007d003c) → [`007d0040`](#insn-007d0040)
- ブロック [`007d0040`](#insn-007d0040) 範囲 `[['007d0040', '007d0043']]`
  - `CONDITIONAL_JUMP` [`007d0040`](#insn-007d0040) → [`007d00ac`](#insn-007d00ac)
  - `FALL_THROUGH` [`007d0040`](#insn-007d0040) → [`007d0044`](#insn-007d0044)
- ブロック [`007d0044`](#insn-007d0044) 範囲 `[['007d0044', '007d004b']]`
  - `CONDITIONAL_JUMP` [`007d0048`](#insn-007d0048) → [`007d0030`](#insn-007d0030)
  - `FALL_THROUGH` [`007d0048`](#insn-007d0048) → [`007d004c`](#insn-007d004c)
- ブロック [`007d004c`](#insn-007d004c) 範囲 `[['007d004c', '007d004f']]`
  - `FALL_THROUGH` [`007d004c`](#insn-007d004c) → [`007d0050`](#insn-007d0050)
- ブロック [`007d0050`](#insn-007d0050) 範囲 `[['007d0050', '007d008f']]`
  - `CONDITIONAL_JUMP` [`007d008c`](#insn-007d008c) → [`007d0098`](#insn-007d0098)
  - `FALL_THROUGH` [`007d008c`](#insn-007d008c) → [`007d0090`](#insn-007d0090)
- ブロック [`007d0090`](#insn-007d0090) 範囲 `[['007d0090', '007d0097']]`
  - `FALL_THROUGH` [`007d0094`](#insn-007d0094) → [`007d0098`](#insn-007d0098)
- ブロック [`007d0098`](#insn-007d0098) 範囲 `[['007d0098', '007d00ab']]`
  - `FALL_THROUGH` [`007d00a8`](#insn-007d00a8) → [`007d00ac`](#insn-007d00ac)
- ブロック [`007d00ac`](#insn-007d00ac) 範囲 `[['007d00ac', '007d00cf']]`

## 命令位置別の参照

- [`007cffe0`](#insn-007cffe0) → [`007cffec`](#insn-007cffec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cffec`](#insn-007cffec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cfff0`](#insn-007cfff0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cfff4`](#insn-007cfff4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cfff8`](#insn-007cfff8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d0008`](#insn-007d0008) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`007d0010`](#insn-007d0010) → `00397608`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`007d0014`](#insn-007d0014) → [`007d0030`](#insn-007d0030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d0020`](#insn-007d0020) → [`007d0050`](#insn-007d0050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d002c`](#insn-007d002c) → [`007d0050`](#insn-007d0050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d003c`](#insn-007d003c) → [`007d0024`](#insn-007d0024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d0040`](#insn-007d0040) → [`007d00ac`](#insn-007d00ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d0048`](#insn-007d0048) → [`007d0030`](#insn-007d0030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d0058`](#insn-007d0058) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`007d0070`](#insn-007d0070) → [`00bdb240`](../00bdb/00bdb240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb240` · 推定シンボル `None` · 推定型 `None`
- [`007d0080`](#insn-007d0080) → `00397608`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`007d0084`](#insn-007d0084) → `00397600`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`007d008c`](#insn-007d008c) → [`007d0098`](#insn-007d0098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d0090`](#insn-007d0090) → `00397600`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`007d0094`](#insn-007d0094) → `00397608`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`007d0098`](#insn-007d0098) → `00397608`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`007d009c`](#insn-007d009c) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`007d00a0`](#insn-007d00a0) → `00397610`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`007d00a8`](#insn-007d00a8) → `00397610`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`007d00bc`](#insn-007d00bc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d00c0`](#insn-007d00c0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d00c4`](#insn-007d00c4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007d00c8`](#insn-007d00c8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007cffe0`](#insn-007cffe0)

~~~json
{
  "source": "007cffe0",
  "target": "007cffec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cffec`](#insn-007cffec)

~~~json
{
  "source": "007cffec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cfff0`](#insn-007cfff0)

~~~json
{
  "source": "007cfff0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cfff4`](#insn-007cfff4)

~~~json
{
  "source": "007cfff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cfff8`](#insn-007cfff8)

~~~json
{
  "source": "007cfff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d0008`](#insn-007d0008)

~~~json
{
  "source": "007d0008",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007d0010`](#insn-007d0010)

~~~json
{
  "source": "007d0010",
  "target": "00397608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003975f1",
  "offset": 23,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e8001600c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "003975f1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007d0014`](#insn-007d0014)

~~~json
{
  "source": "007d0014",
  "target": "007d0030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d0020`](#insn-007d0020)

~~~json
{
  "source": "007d0020",
  "target": "007d0050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d002c`](#insn-007d002c)

~~~json
{
  "source": "007d002c",
  "target": "007d0050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d003c`](#insn-007d003c)

~~~json
{
  "source": "007d003c",
  "target": "007d0024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d0040`](#insn-007d0040)

~~~json
{
  "source": "007d0040",
  "target": "007d00ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d0048`](#insn-007d0048)

~~~json
{
  "source": "007d0048",
  "target": "007d0030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d0058`](#insn-007d0058)

~~~json
{
  "source": "007d0058",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007d0070`](#insn-007d0070)

~~~json
{
  "source": "007d0070",
  "target": "00bdb240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007d0080`](#insn-007d0080)

~~~json
{
  "source": "007d0080",
  "target": "00397608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003975f1",
  "offset": 23,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e8001600c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "003975f1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007d0084`](#insn-007d0084)

~~~json
{
  "source": "007d0084",
  "target": "00397600",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003975f1",
  "offset": 15,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e8001600c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "003975f1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007d008c`](#insn-007d008c)

~~~json
{
  "source": "007d008c",
  "target": "007d0098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d0090`](#insn-007d0090)

~~~json
{
  "source": "007d0090",
  "target": "00397600",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003975f1",
  "offset": 15,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e8001600c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "003975f1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007d0094`](#insn-007d0094)

~~~json
{
  "source": "007d0094",
  "target": "00397608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003975f1",
  "offset": 23,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e8001600c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "003975f1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007d0098`](#insn-007d0098)

~~~json
{
  "source": "007d0098",
  "target": "00397608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003975f1",
  "offset": 23,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e8001600c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "003975f1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007d009c`](#insn-007d009c)

~~~json
{
  "source": "007d009c",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007d00a0`](#insn-007d00a0)

~~~json
{
  "source": "007d00a0",
  "target": "00397610",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003975f1",
  "offset": 31,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e8001600c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "003975f1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007d00a8`](#insn-007d00a8)

~~~json
{
  "source": "007d00a8",
  "target": "00397610",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003975f1",
  "offset": 31,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e8001600c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "003975f1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`007d00bc`](#insn-007d00bc)

~~~json
{
  "source": "007d00bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d00c0`](#insn-007d00c0)

~~~json
{
  "source": "007d00c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d00c4`](#insn-007d00c4)

~~~json
{
  "source": "007d00c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007d00c8`](#insn-007d00c8)

~~~json
{
  "source": "007d00c8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
