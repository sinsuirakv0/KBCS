# 00bcff7c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcff38`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcff38.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0012.md#compare-84ebf4fb127a22f99fe205face13182a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4c9c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9c4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0020.md#compare-f11e32068fb23c3cf4f21e42c3a9b301)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcff7c",
  "name": "FUN_00bcff7c",
  "size": 280,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3fdf24343c0a0f0b0b608cf5b66fe640db640d3861eb4ca3ed9ee50cf6273e97",
  "source_text_sha256": "3fdf24343c0a0f0b0b608cf5b66fe640db640d3861eb4ca3ed9ee50cf6273e97",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcff7c",
        "00bd0093"
      ]
    ],
    "bytes_sha256": "6c8d5f3f1c4dd6758d3e184b9d88b0f0c90545a6ee4c05aa98fb90df36ec1db5",
    "instruction_count": 70,
    "instruction_bytes": 280,
    "body_bytes": 280,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
"::friend "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2397 bytes

~~~c

void FUN_00bcff7c(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 uVar2;
  void *__ptr;
  long lVar3;
  size_t __size;
  long *plVar4;
  
  plVar4 = *(long **)(param_1 + 0x10);
                    /* try { // try from 00bcff98 to 00cd000f has its CatchHandler @ 00bcff98
                       catch() { ... } // from try @ 00bcff98 with catch @ 00bcff98
                       catch() { ... } // from try @ 00bd0070 with catch @ 00bcff98 */
  (**(code **)(*plVar4 + 0x20))(plVar4);
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  }
  lVar3 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 9U) {
    __size = param_2[2] * 2;
    uVar1 = lVar3 + 0x3e9;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  uVar2 = s___friend_0029577f._0_8_;
                    /* try { // try from 00bd0010 to 00cd0017 has its CatchHandler @ 00bd0250 */
                    /* try { // try from 00bd0018 to 00cd001f has its CatchHandler @ 00bd0230 */
                    /* try { // try from 00bd0020 to 00cd0027 has its CatchHandler @ 00bd0210 */
  ((char *)((long)__ptr + lVar3))[8] = ' ';
  *(undefined8 *)((long)__ptr + lVar3) = uVar2;
                    /* try { // try from 00bd0028 to 00cd002f has its CatchHandler @ 00bd01f0 */
  plVar4 = *(long **)(param_1 + 0x18);
                    /* try { // try from 00bd0030 to 00cd0053 has its CatchHandler @ 00bd01d0 */
  lVar3 = *plVar4;
  param_2[1] = param_2[1] + 9;
  (**(code **)(lVar3 + 0x20))(plVar4,param_2);
                    /* try { // try from 00bd0054 to 00cd005f has its CatchHandler @ 00bd0164 */
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) == 0x40) {
                    /* try { // try from 00bd0060 to 00cd006f has its CatchHandler @ 00bd0154 */
    return;
  }
                    /* try { // try from 00bd0070 to 00cd025f has its CatchHandler @ 00bcff98 */
                    /* WARNING: Could not recover jumptable at 0x00bd008c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcff7c"></a> `00bcff7c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcff80"></a> `00bcff80` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcff84"></a> `00bcff84` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcff88"></a> `00bcff88` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcff8c"></a> `00bcff8c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcff90"></a> `00bcff90` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcff94"></a> `00bcff94` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcff98"></a> `00bcff98` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcff9c"></a> `00bcff9c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcffa0"></a> `00bcffa0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcffa4"></a> `00bcffa4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcffa8"></a> `00bcffa8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcffac"></a> `00bcffac` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcffb0"></a> `00bcffb0` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcffb4"></a> `00bcffb4` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcffb8"></a> `00bcffb8` | `c0 00 00 54` | b.eq 0x00bcffd0 | `CONDITIONAL_JUMP`
<a id="insn-00bcffbc"></a> `00bcffbc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcffc0"></a> `00bcffc0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcffc4"></a> `00bcffc4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcffc8"></a> `00bcffc8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcffcc"></a> `00bcffcc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcffd0"></a> `00bcffd0` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcffd4"></a> `00bcffd4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcffd8"></a> `00bcffd8` | `0a 25 00 91` | add x10,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bcffdc"></a> `00bcffdc` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcffe0"></a> `00bcffe0` | `49 01 00 54` | b.ls 0x00bd0008 | `CONDITIONAL_JUMP`
<a id="insn-00bcffe4"></a> `00bcffe4` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcffe8"></a> `00bcffe8` | `08 a5 0f 91` | add x8,x8,#0x3e9 | `FALL_THROUGH`
<a id="insn-00bcffec"></a> `00bcffec` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcfff0"></a> `00bcfff0` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcfff4"></a> `00bcfff4` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfff8"></a> `00bcfff8` | `96 34 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfffc"></a> `00bcfffc` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd0000"></a> `00bd0000` | `80 04 00 b4` | cbz x0,0x00bd0090 | `CONDITIONAL_JUMP`
<a id="insn-00bd0004"></a> `00bd0004` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd0008"></a> `00bd0008` | `29 b6 ff b0` | adrp x9,0x295000 | `FALL_THROUGH`
<a id="insn-00bd000c"></a> `00bd000c` | `29 fd 1d 91` | add x9,x9,#0x77f | `FALL_THROUGH`
<a id="insn-00bd0010"></a> `00bd0010` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bd0014"></a> `00bd0014` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bd0018"></a> `00bd0018` | `0a 04 80 52` | mov w10,#0x20 | `FALL_THROUGH`
<a id="insn-00bd001c"></a> `00bd001c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd0020"></a> `00bd0020` | `0a 21 00 39` | strb w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bd0024"></a> `00bd0024` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bd0028"></a> `00bd0028` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd002c"></a> `00bd002c` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bd0030"></a> `00bd0030` | `08 25 00 91` | add x8,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bd0034"></a> `00bd0034` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bd0038"></a> `00bd0038` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd003c"></a> `00bd003c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd0040"></a> `00bd0040` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bd0044"></a> `00bd0044` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd0048"></a> `00bd0048` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bd004c"></a> `00bd004c` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bd0050"></a> `00bd0050` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bd0054"></a> `00bd0054` | `c1 00 00 54` | b.ne 0x00bd006c | `CONDITIONAL_JUMP`
<a id="insn-00bd0058"></a> `00bd0058` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd005c"></a> `00bd005c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0060"></a> `00bd0060` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd0064"></a> `00bd0064` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd0068"></a> `00bd0068` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd006c"></a> `00bd006c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd0070"></a> `00bd0070` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd0074"></a> `00bd0074` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd0078"></a> `00bd0078` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd007c"></a> `00bd007c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd0080"></a> `00bd0080` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0084"></a> `00bd0084` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd0088"></a> `00bd0088` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd008c"></a> `00bd008c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bd0090"></a> `00bd0090` | `8c 38 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcff7c`](#insn-00bcff7c) 範囲 `[['00bcff7c', '00bcff97']]`
  - `FALL_THROUGH` [`00bcff94`](#insn-00bcff94) → [`00bcff98`](#insn-00bcff98)
- ブロック [`00bcff98`](#insn-00bcff98) 範囲 `[['00bcff98', '00bcffbb']]`
  - `CONDITIONAL_JUMP` [`00bcffb8`](#insn-00bcffb8) → [`00bcffd0`](#insn-00bcffd0)
  - `FALL_THROUGH` [`00bcffb8`](#insn-00bcffb8) → [`00bcffbc`](#insn-00bcffbc)
- ブロック [`00bcffbc`](#insn-00bcffbc) 範囲 `[['00bcffbc', '00bcffcf']]`
  - `FALL_THROUGH` [`00bcffcc`](#insn-00bcffcc) → [`00bcffd0`](#insn-00bcffd0)
- ブロック [`00bcffd0`](#insn-00bcffd0) 範囲 `[['00bcffd0', '00bcffe3']]`
  - `CONDITIONAL_JUMP` [`00bcffe0`](#insn-00bcffe0) → [`00bd0008`](#insn-00bd0008)
  - `FALL_THROUGH` [`00bcffe0`](#insn-00bcffe0) → [`00bcffe4`](#insn-00bcffe4)
- ブロック [`00bcffe4`](#insn-00bcffe4) 範囲 `[['00bcffe4', '00bd0003']]`
  - `CONDITIONAL_JUMP` [`00bd0000`](#insn-00bd0000) → [`00bd0090`](#insn-00bd0090)
  - `FALL_THROUGH` [`00bd0000`](#insn-00bd0000) → [`00bd0004`](#insn-00bd0004)
- ブロック [`00bd0004`](#insn-00bd0004) 範囲 `[['00bd0004', '00bd0007']]`
  - `FALL_THROUGH` [`00bd0004`](#insn-00bd0004) → [`00bd0008`](#insn-00bd0008)
- ブロック [`00bd0008`](#insn-00bd0008) 範囲 `[['00bd0008', '00bd000f']]`
  - `FALL_THROUGH` [`00bd000c`](#insn-00bd000c) → [`00bd0010`](#insn-00bd0010)
- ブロック [`00bd0010`](#insn-00bd0010) 範囲 `[['00bd0010', '00bd0017']]`
  - `FALL_THROUGH` [`00bd0014`](#insn-00bd0014) → [`00bd0018`](#insn-00bd0018)
- ブロック [`00bd0018`](#insn-00bd0018) 範囲 `[['00bd0018', '00bd001f']]`
  - `FALL_THROUGH` [`00bd001c`](#insn-00bd001c) → [`00bd0020`](#insn-00bd0020)
- ブロック [`00bd0020`](#insn-00bd0020) 範囲 `[['00bd0020', '00bd0027']]`
  - `FALL_THROUGH` [`00bd0024`](#insn-00bd0024) → [`00bd0028`](#insn-00bd0028)
- ブロック [`00bd0028`](#insn-00bd0028) 範囲 `[['00bd0028', '00bd002f']]`
  - `FALL_THROUGH` [`00bd002c`](#insn-00bd002c) → [`00bd0030`](#insn-00bd0030)
- ブロック [`00bd0030`](#insn-00bd0030) 範囲 `[['00bd0030', '00bd0053']]`
  - `FALL_THROUGH` [`00bd0050`](#insn-00bd0050) → [`00bd0054`](#insn-00bd0054)
- ブロック [`00bd0054`](#insn-00bd0054) 範囲 `[['00bd0054', '00bd0057']]`
  - `CONDITIONAL_JUMP` [`00bd0054`](#insn-00bd0054) → [`00bd006c`](#insn-00bd006c)
  - `FALL_THROUGH` [`00bd0054`](#insn-00bd0054) → [`00bd0058`](#insn-00bd0058)
- ブロック [`00bd0058`](#insn-00bd0058) 範囲 `[['00bd0058', '00bd005f']]`
  - `FALL_THROUGH` [`00bd005c`](#insn-00bd005c) → [`00bd0060`](#insn-00bd0060)
- ブロック [`00bd0060`](#insn-00bd0060) 範囲 `[['00bd0060', '00bd006b']]`
- ブロック [`00bd006c`](#insn-00bd006c) 範囲 `[['00bd006c', '00bd006f']]`
  - `FALL_THROUGH` [`00bd006c`](#insn-00bd006c) → [`00bd0070`](#insn-00bd0070)
- ブロック [`00bd0070`](#insn-00bd0070) 範囲 `[['00bd0070', '00bd008f']]`
- ブロック [`00bd0090`](#insn-00bd0090) 範囲 `[['00bd0090', '00bd0093']]`

## 命令位置別の参照

- [`00bcff80`](#insn-00bcff80) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff84`](#insn-00bcff84) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff88`](#insn-00bcff88) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffb8`](#insn-00bcffb8) → [`00bcffd0`](#insn-00bcffd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffe0`](#insn-00bcffe0) → [`00bd0008`](#insn-00bd0008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfff8`](#insn-00bcfff8) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bd0000`](#insn-00bd0000) → [`00bd0090`](#insn-00bd0090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0014`](#insn-00bd0014) → `0029577f`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd0054`](#insn-00bd0054) → [`00bd006c`](#insn-00bd006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0058`](#insn-00bd0058) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd005c`](#insn-00bd005c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0060`](#insn-00bd0060) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd007c`](#insn-00bd007c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0080`](#insn-00bd0080) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0084`](#insn-00bd0084) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0090`](#insn-00bd0090) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcff80`](#insn-00bcff80)

~~~json
{
  "source": "00bcff80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff84`](#insn-00bcff84)

~~~json
{
  "source": "00bcff84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff88`](#insn-00bcff88)

~~~json
{
  "source": "00bcff88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffb8`](#insn-00bcffb8)

~~~json
{
  "source": "00bcffb8",
  "target": "00bcffd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffe0`](#insn-00bcffe0)

~~~json
{
  "source": "00bcffe0",
  "target": "00bd0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfff8`](#insn-00bcfff8)

~~~json
{
  "source": "00bcfff8",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0000`](#insn-00bd0000)

~~~json
{
  "source": "00bd0000",
  "target": "00bd0090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0014`](#insn-00bd0014)

~~~json
{
  "source": "00bd0014",
  "target": "0029577f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029577f",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "3a3a667269656e642000",
  "capture_start": "0029577f",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd0054`](#insn-00bd0054)

~~~json
{
  "source": "00bd0054",
  "target": "00bd006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0058`](#insn-00bd0058)

~~~json
{
  "source": "00bd0058",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd005c`](#insn-00bd005c)

~~~json
{
  "source": "00bd005c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0060`](#insn-00bd0060)

~~~json
{
  "source": "00bd0060",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd007c`](#insn-00bd007c)

~~~json
{
  "source": "00bd007c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0080`](#insn-00bd0080)

~~~json
{
  "source": "00bd0080",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0084`](#insn-00bd0084)

~~~json
{
  "source": "00bd0084",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0090`](#insn-00bd0090)

~~~json
{
  "source": "00bd0090",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
